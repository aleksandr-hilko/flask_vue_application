import Vue from 'vue';
import Router from 'vue-router';
import ProjectList from '../views/ProjectList';
import CustomerList from '../views/CustomerList';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ProjectList',
      component: ProjectList,
      props: true
    },
    {
      path: '/customers',
      name: 'CustomerList',
      component: CustomerList,
    },
  ],
});
