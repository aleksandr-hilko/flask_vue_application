import Vue from 'vue';
import Router from 'vue-router';
import store from '../store';
import Login from '../components/Login';
import Secure from '../components/Secure';
import ProjectList from '../views/ProjectList';
import CustomerList from '../views/CustomerList';

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'ProjectList',
      component: ProjectList,
      props: true
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/secure',
      name: 'secure',
      component: Secure,
      meta: { 
        requiresAuth: true
      }
    },
    {
      path: '/customers',
      name: 'CustomerList',
      component: CustomerList,
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    console.log("here");
    if (store.getters.isLoggedIn) {
      next();
      return;
    }
    next('/login');
  } else {
    console.log("here 2");
    next();
  }
});

export default router;

