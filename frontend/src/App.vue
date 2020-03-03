<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "@/components/Navbar";

export default {
  name: "App",
  components: {
    NavbarComponent
  },
  created() {
    const copy = this;
    this.$http.interceptors.response.use(
      function (response) {
        return response;
      },
      function (error) {
        console.log(error);
        if (error.response.status === 401) {
          copy.$store.dispatch("cleanToken").then(() => {
            copy.$router.push("/login");
          });
        }
        return Promise.reject(error);
      }
    );
  }
};
</script>

<style>
#app {
  font-size: 14px;
}
</style>
