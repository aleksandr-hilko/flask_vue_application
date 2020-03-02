<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'ProjectList' }" class="navbar-brand"
        >Промтеплогаз</router-link
      >

      <div class="collapse navbar-collapse right-panel">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mx-1">
            <router-link
              :to="{ name: 'ProjectList' }"
              class="btn btn-sm btn-outline-success"
              >Объекты</router-link
            >
          </li>
          <li class="nav-item mx-1">
            <router-link
              :to="{ name: 'CustomerList' }"
              class="btn btn-sm btn-outline-success"
              >Заказчики</router-link
            >
          </li>
          <li class="nav-item mx-1">
            <span class="btn btn-sm btn-outline-danger" v-if="isLoggedIn"><a @click="logout">Выйти</a></span>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import {
  BDropdownItem,
  BNavItemDropdown,
  BDropdownDivider
} from "bootstrap-vue";

export default {
  name: "NavbarComponent",
  components: {
    BDropdownItem,
    BNavItemDropdown,
    BDropdownDivider
  },
  computed: {
      isLoggedIn() { return this.$store.getters.isLoggedIn; }
    },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    }
  }
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}

.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}

.navbar-brand:hover {
  color: #dc3545 !important;
}

#profile-dropdown {
  margin-left: 30px;
}
</style>
