<template>
  <tr>
    <td>{{data.name}}</td>
    <td>{{data.customer}}</td>
    <td>{{data.has_contract}}</td>
    <td>{{data.price}}</td>
    <td>{{data.has_plan}}</td>
    <td>{{data.start_date}}</td>
    <td>{{data.expiration_date}}</td>
    <td>
      <button type="button" class="btn btn-warning btn-sm">Изменить</button>
      <button
        type="button"
        class="btn btn-danger btn-sm"
        v-on:click="deleteProject">
        Удалить
        </button>
    </td>
  </tr>
</template>

<script>
import axios from "axios";

export default {
  name: "Project",
  props: {
    data: {}
  },
  methods: {
    deleteProject() {
      const endpoint = `http://localhost:5000/api/projects/${this.data.id}`;
      axios
        .delete(endpoint)
        .then((res) => {
          // eslint-disable-next-line
          console.log(res);
          this.$emit("deleteProject");
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>
