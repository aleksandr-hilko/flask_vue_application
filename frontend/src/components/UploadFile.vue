<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label
        >File
        <input
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
        />
      </label>
      <button v-on:click="submitFile()">Загрузить</button>
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
      const url = `http://localhost:5000/api/projects/${this.contractId}/upload_contract`;
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
