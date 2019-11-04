import Vue from "vue";
import { Button } from 'ant-design-vue';
import test  from "../components/test.vue";

Vue.use(Button);


new Vue(test).$mount("#components-demo");
