<template>
  <div>
    <h1>{{ message }}</h1>
    <div>
      <a-button type="primary">Primary</a-button>
      <a-button>Default</a-button>
      <a-button type="dashed">Dashed</a-button>
      <a-button type="danger">Danger</a-button>
      <a-button type="primary" @click="openNotification">Open the notification box</a-button>
      <div class="carousel">
        <a-carousel arrows dotsClass="slick-dots slick-thumb">
          <a slot="customPaging" slot-scope="props">
            <img :src="getImgUrl(props.i)" />
          </a>
          <div v-for="item in 4" :key="item">
            <img :src="baseUrl+'abstract0'+item+'.jpg'" />
          </div>
        </a-carousel>
    </div>
    </div>
    
  </div>
</template>

<script>
const baseUrl =
    'https://raw.githubusercontent.com/vueComponent/ant-design-vue/master/components/vc-slick/assets/img/react-slick/';

export default {
  name: "app",
  components: {},
  data: {
    message: "Hello from Vue",
    baseUrl: baseUrl,
  },
  computed: {},
  methods: {
    openNotification() {
      this.$notification.open({
        message: "Notification Title",
        description:
          "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
        onClick: () => {
          console.log("Notification Clicked!");
        }
      });
    },
    getImgUrl(i) {
        return `${baseUrl}abstract0${i + 1}.jpg`;
    },
  }
};
</script>

<style scoped>
body {
  /* background-image: url(///../static/img/ssd/avatar1.png); */
}
.carousel{
  display: block;
  padding: 10px;
  height: 382px;
  /* For demo */
  
}
.ant-carousel >>> .slick-dots {
    height: auto;
  }
  .ant-carousel >>> .slick-slide img {
    border: 5px solid #fff;
    display: block;
    margin: auto;
    max-width: 80%;
  }
  .ant-carousel >>> .slick-thumb {
    bottom: -45px;
  }
  .ant-carousel >>> .slick-thumb li {
    width: 60px;
    height: 45px;
  }
  .ant-carousel >>> .slick-thumb li img {
    width: 100%;
    height: 100%;
    filter: grayscale(100%);
  }
  .ant-carousel >>> .slick-thumb li.slick-active img {
    filter: grayscale(0%);
  }

</style>