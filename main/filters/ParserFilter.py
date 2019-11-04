from compressor.filters import CompilerFilter
from compressor.filters.base import (
    NamedTemporaryFile, subprocess, shell_quote, FilterError, smart_text, io
)


class ParserFilter(CompilerFilter):
    def output(self, **kwargs):
        vas = 'sasas'
        return super().output(**kwargs)

    command = "parcel build"

    def input(self, **kwargs):

        encoding = self.default_encoding
        options = dict(self.options)

        if self.infile is None and "{infile}" in self.command:
            # create temporary input file if needed
            if self.filename is None:
                self.infile = NamedTemporaryFile(mode='wb')
                self.infile.write(self.content.encode(encoding))
                self.infile.flush()
                options["infile"] = self.infile.name
            else:
                # we use source file directly, which may be encoded using
                # something different than utf8. If that's the case file will
                # be included with charset="something" html attribute and
                # charset will be available as filter's charset attribute
                encoding = self.charset  # or self.default_encoding
                self.infile = open(self.filename)
                options["infile"] = self.filename

        if "{outfile}" in self.command and "outfile" not in options:
            # create temporary output file if needed
            ext = self.type and ".%s" % self.type or ""
            self.outfile = NamedTemporaryFile(mode='r+', suffix=ext)
            options["outfile"] = self.outfile.name
            options["outfile_css"] = self.outfile.name.replace(ext, '.css')

        # Quote infile and outfile for spaces etc.
        if "infile" in options:
            options["infile"] = shell_quote(options["infile"])
        if "outfile" in options:
            options["outfile"] = shell_quote(options["outfile"])
            options["outfile_css"] = shell_quote(options["outfile_css"])

        try:
            command = self.command.format(**options)
            proc = subprocess.Popen(
                command, shell=True, cwd=self.cwd, stdout=self.stdout,
                stdin=self.stdin, stderr=self.stderr)
            if self.infile is None:
                # if infile is None then send content to process' stdin
                filtered, err = proc.communicate(
                    self.content.encode(encoding))
            else:
                filtered, err = proc.communicate()
            filtered, err = filtered.decode(encoding), err.decode(encoding)
        except (IOError, OSError) as e:
            raise FilterError('Unable to apply %s (%r): %s' %
                              (self.__class__.__name__, self.command, e))
        else:
            if proc.wait() != 0:
                # command failed, raise FilterError exception
                if not err:
                    err = ('Unable to apply %s (%s)' %
                           (self.__class__.__name__, self.command))
                    if filtered:
                        err += '\n%s' % filtered
                raise FilterError(err)

            if self.verbose:
                self.logger.debug(err)

            outfile_path = options.get('outfile')
            outfile_path_css = options.get('outfile_css')
            if outfile_path:
                with io.open(outfile_path, 'r', encoding=encoding) as file:
                    filtered = file.read()
            if outfile_path_css:
                with io.open(outfile_path_css, 'r', encoding=encoding) as file:
                    css_filtered = file.read()
                    csas = smart_text(css_filtered)
        finally:
            if self.infile is not None:
                self.infile.close()
            if self.outfile is not None:
                self.outfile.close()
        return smart_text(filtered)


class JSDevParserFilter(ParserFilter):
    def input(self, **kwargs):
        _kind = kwargs.get('kind')
        if _kind == 'file':
            self.command = f"{self.command} {kwargs.get('filename')} --no-minify --no-source-maps "
            self.command = f"{self.command} -d /tmp/ --out-file" + " {outfile}"
        else:
            self.command = "yUglify"
        return super().input(**kwargs)


class JSProdParserFilter(ParserFilter):
    def input(self, **kwargs):
        _kind = kwargs.get('kind')
        if _kind == 'file':
            self.command = f"{self.command} {kwargs.get('filename')} --no-source-maps --no-cache"
            self.command = f"{self.command} -d /tmp/ --out-file" + " {outfile}"
        else:
            # fallback to default js compressor command
            self.command = "yUglify"
        return super().input(**kwargs)


class CSSDevParserFilter(ParserFilter):
    def input(self, **kwargs):
        _kind = kwargs.get('kind')
        if _kind == 'file':
            self.command = f"{self.command} {kwargs.get('filename')} --no-minify --no-source-maps"
            self.command = f"{self.command} -d /tmp/ --out-file" + " {outfile}"
        else:
            # fallback to default css compressor command
            self.command = "yUglify"
        return super().input(**kwargs)


class CSSProdParserFilter(ParserFilter):
    def input(self, **kwargs):
        _kind = kwargs.get('kind')
        if _kind == 'file':
            self.command = f"{self.command} {kwargs.get('filename')} --no-source-maps --no-cache"
            self.command = f"{self.command} -d /tmp/ --out-file" + " {outfile}"
        else:
            # fallback to default css compressor command
            self.command = "yUglify"
        return super().input(**kwargs)

