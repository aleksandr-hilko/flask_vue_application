<template>
  <tr>
    <td>{{ data.customer_name }}</td>
    <td>{{ data.phone }}</td>
    <td>{{ data.email }}</td>
    <td>{{ data.address }}</td>
    <td>{{ data.payment_account }}</td>
    <td>{{ this.projectsStr }}</td>
    <td>
      <button type="button" class="btn btn-warning btn-sm">Изменить</button>
      <button
        type="button"
        class="btn btn-danger btn-sm"
        v-on:click="deleteCustomer"
      >
        Удалить
      </button>
    </td>
  </tr>
</template>

<script>
import axios from "axios";

export default {
  name: "Customer",
  props: {
    data: {}
  },
  methods: {
    deleteCustomer() {
      const endpoint = `${API_URL}/customers/${this.data.id}`;
      axios
        .delete(endpoint)
        .then(res => {
          // eslint-disable-next-line
          console.log(res);
          this.$emit("deleteCustomer");
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  },
  computed: {
    projectsStr() {
      if (this.data.projects.length > 0) {
        return this.data.projects.map(project => project.name).join(" ");
      }
      return "-";
    }
  }
};
</script>

<style></style>
