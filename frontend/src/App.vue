<template>
  <div id='app'>
    <NavbarComponent/>
    <router-view/>
  </div>
</template>

<script>
import NavbarComponent from '@/components/Navbar';

export default {
  name: 'App',
  components: {
    NavbarComponent,
  },
};
</script>

<style>
#app {
  font-size: 14px;
}
</style>
