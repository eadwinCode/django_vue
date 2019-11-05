import Vue from "vue";
import { Button, Carousel, notification } from 'ant-design-vue';
import test  from "../components/test.vue";

Vue.use(Carousel);
Vue.use(Button);

Vue.prototype.$notification = notification;
new Vue(test).$mount("#components-demo");

