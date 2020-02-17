<template>
  <tr>
    <td>{{ data.name }}</td>
    <td>{{ data.customer }}</td>
    <td v-if="data.price">{{ data.price }}</td>
    <td v-else>-</td>

    <td v-if="data.has_contract"><i class="fas fa-check"></i></td>
    <td v-else><i class="fas fa-times"></i></td>

    <td v-if="data.has_plan"><i class="fas fa-check"></i></td>
    <td v-else><i class="fas fa-times"></i></td>

    <td v-if="data.work_started"><i class="fas fa-check"></i></td>
    <td v-else><i class="fas fa-times"></i></td>

    <td v-if="data.expiration_date">{{ data.expiration_date }}</td>
    <td v-else>-</td>

    <td v-if="data.contract">
      <a :href="this.contractUrl" target="_blank"
        ><i class="far fa-file-excel"></i>
        </a>
    </td>
    <td v-else><i class="fas fa-times"></i></td>
    <td>
      <button type="button" class="btn btn-warning btn-sm">Изменить</button>
      <button
        type="button"
        class="btn btn-danger btn-sm"
        v-on:click="deleteProject"
      >
        Удалить
      </button>
      <button
        type="button"
        class="btn btn-success btn-sm"
        v-on:click="$emit('uploadFile', data.id)"
        v-b-modal.upload-contract-modal
      >
        Загрузить договор
      </button>
    </td>
  </tr>
</template>

<script>
import axios from "axios";

export default {
  name: "Project",
  components: {},
  props: {
    data: {}
  },
  methods: {
    deleteProject() {
      const endpoint = `http://localhost:5000/api/projects/${this.data.id}`;
      axios
        .delete(endpoint)
        .then(res => {
          // eslint-disable-next-line
          console.log(res);
          this.$emit("deleteProject");
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  },
  computed: {
    contractUrl() {
      return (
         this.data.contract
      );
    }
  }
};
</script>

<style></style>
