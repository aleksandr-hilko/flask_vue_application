<template>
  <tr>
    <th scope="row">{{ pkey }}</th>
    <td>{{ data.name }}</td>
    <td>{{ data.customer }}</td>
    <td v-if="data.price">{{ data.price }}</td>
    <td v-else>-</td>

    <td v-if="data.has_contract"><font-awesome-icon icon="check" /></td>
    <td v-else><font-awesome-icon icon="times" /></td>

    <td v-if="data.has_plan"><font-awesome-icon icon="check" /></td>
    <td v-else><font-awesome-icon icon="times" /></td>

    <td v-if="data.work_started"><font-awesome-icon icon="check" /></td>
    <td v-else><font-awesome-icon icon="times" /></td>

    <td v-if="data.expiration_date">
      {{ data.expiration_date }}
    </td>
    <td v-else>-</td>

    <td v-if="data.contract">
      <a :href="data.contract" target="_blank"
        ><font-awesome-icon icon="file-excel" />
      </a>
    </td>
    <td v-else><font-awesome-icon icon="times" /></td>
    <td>
      <button
        type="button"
        class="btn btn-warning btn-sm"
        v-on:click="$emit('clickEditProject', data)"
      >
        Изменить
      </button>
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
    data: Object,
    pkey: ""
  },
  methods: {
    deleteProject() {
      const endpoint = `${process.env.VUE_APP_API_URL}/projects/${this.data.id}`;
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
  }
};
</script>

<style></style>
