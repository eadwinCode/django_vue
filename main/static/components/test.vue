<template>
  <div>
    <h1>{{ message }}</h1>
    <div>
      <a-button type="primary">Primary</a-button>
      <a-button>Default</a-button>
      <a-button type="dashed">Dashed</a-button>
      <a-button type="danger">Danger</a-button>
      <a-config-provider :autoInsertSpaceInButton="false">
        <a-button type="primary">按钮</a-button>
      </a-config-provider>
      <a-button type="primary">按钮</a-button>
      <a-button type="link">Link</a-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
  data: {
    message: "Hello"
  },
  computed: {}
};
</script>

<style lang="scss">
  body{
      background-color: lightblue;
      background-image: url(///../static/img/ssd/avatar1.png);
      
      button{
          font: outline;
      }
  }
</style>