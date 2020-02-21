<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <input
        type="file"
        id="file"
        ref="file"
        v-on:change="handleFileUpload()"
        style="display:none"
      />
      <label for="upload">Выберите файл</label>

      <i
        class="fas fa-folder-open fa-lg"
        id="upload"
        onclick="document.getElementById('file').click()"
      ></i>
      <p v-if="file">Файл выбран: {{file.name}}</p>

      <button class="btn btn-success btn-sm submit" v-on:click="submitFile()">
        Загрузить
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UploadFile",
  props: {
    contractId: ""
  },
  data() {
    return {
      file: ""
    };
  },

  methods: {
    submitFile() {
      const formData = new FormData();
      formData.append("file", this.file);
      const url = `${process.env.VUE_APP_API_URL}/projects/${this.contractId}/upload_contract`;
      const vm = this;
      axios
        .post(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function () {
          vm.$emit("closeUploadModal");
        })
        .catch(function () {
          // eslint-disable-next-line
          console.log("FAILURE!!");
        });
    },

    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    }
  }
};
</script>

<style>
.submit {
  display: block;
  margin-top: 20px;
}
label {
  margin-right: 10px;
}
</style>
