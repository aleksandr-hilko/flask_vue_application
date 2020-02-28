<template>
  <div class="container-fluid">
    <project-filters
      :customers="customerNames"
      @filterProjects="handleFilter($event)"
    ></project-filters>
    <div class="row">
      <div class="col-sm-10">
        <br />
        <br />
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.project-modal
        >
          Добавить Объект
        </button>
        <br />
        <br />
        <table class="table table-hover table-bordered">
          <thead>
            <tr>
              <th scope="col" v-on:click="switchOrder('id')">
                #
                <font-awesome-icon
                  v-if="orderBy === 'id'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('name')">
                Название
                <font-awesome-icon
                  v-if="orderBy === 'name'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('customer_name')">
                Заказчик
                <font-awesome-icon
                  v-if="orderBy === 'customer_name'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('price')">
                Цена
                <font-awesome-icon
                  v-if="orderBy === 'price'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('has_contract')">
                Договор подписан
                <font-awesome-icon
                  v-if="orderBy === 'has_contract'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('has_plan')">
                Съёмка сделана
                <font-awesome-icon
                  v-if="orderBy === 'has_plan'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('work_started')">
                Работы начаты
                <font-awesome-icon
                  v-if="orderBy === 'work_started'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('expiration_date')">
                Окончание работ
                <font-awesome-icon
                  v-if="orderBy === 'expiration_date'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th scope="col" v-on:click="switchOrder('contract')">
                Договор
                <font-awesome-icon
                  v-if="orderBy === 'contract'"
                  :icon="getOrderDirClass()"
                />
              </th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <project
              v-for="(project, item) in projects"
              :key="item"
              :pkey="item + 1"
              :data="project"
              @deleteProject="handleDeleteProject($event)"
              @uploadFile="uploadContractId = $event"
            >
            </project>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      ref="addProjectModal"
      id="project-modal"
      title="Добавьте новый объект"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-name-group"
          label="Название:"
          label-for="form-name-input"
        >
          <b-form-input
            id="form-name-input"
            type="text"
            required
            v-model="addProjectForm.name"
            placeholder="Название"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="form-customer-group"
          label="Заказчик:"
          label-for="form-customer-select"
        >
          <b-form-select
            id="form-customer-select"
            v-model="addProjectForm.customerName"
            :options="customerNames"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group
          id="form-price-group"
          label="Цена:"
          label-for="form-price-input"
        >
          <b-form-input
            id="form-price-input"
            type="text"
            v-model="addProjectForm.price"
            placeholder="Цена"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-checkboxes-input">
          <b-form-checkbox-group
            v-model="addProjectForm.checked"
            id="checkboxes-4"
          >
            <b-form-checkbox value="has_plan">Съёмка готова?</b-form-checkbox>
            <b-form-checkbox value="work_started"
              >Работы начаты?</b-form-checkbox
            >
            <b-form-checkbox value="has_contract"
              >Договор составлен?</b-form-checkbox
            >
          </b-form-checkbox-group>
        </b-form-group>

        <b-form-group
          id="form-end-group"
          label="Окончание работ:"
          required
          label-for="form-end-input"
        >
          <b-form-input
            id="form-end-input"
            type="date"
            v-model="addProjectForm.expirationDate"
            placeholder="Окончание работ"
          >
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Подтвердить</b-button>
        <b-button type="reset" variant="danger">Отменить</b-button>
      </b-form>
    </b-modal>
    <b-modal
      ref="uploadContractModal"
      id="upload-contract-modal"
      title="Загрузите договор"
      hide-footer
    >
      <upload-file
        :contractId="uploadContractId"
        @closeUploadModal="closeUploadContractModal"
      />
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import Project from "@/components/Project";
import ProjectFilters from "@/components/ProjectFilters";
import UploadFile from "@/components/UploadFile";

export default {
  name: "ProjectList",
  components: {
    Project,
    UploadFile,
    ProjectFilters
  },
  data() {
    return {
      projects: [],
      customers: [],
      uploadContractId: "",
      orderBy: "",
      ascOrder: true,
      addProjectForm: {
        name: "",
        customerName: "",
        price: "",
        checked: [],
        expirationDate: ""
      }
    };
  },
  methods: {
    handleFilter(filters) {
      console.log(filters);
      this.$router
        .push({
          query: filters
        })
        .catch(() => {});
    },
    getOrderQS(orderBy) {
      if (orderBy === this.orderBy) {
        this.ascOrder = !this.ascOrder;
      } else {
        this.orderBy = orderBy;
        this.ascOrder = true;
      }
      const order = this.ascOrder ? "asc" : "desc";
      return `order=${orderBy}:${order}`;
    },
    switchOrder(orderBy) {
      const qs = this.getOrderQS(orderBy);
      this.getProjects(qs);
    },
    getOrderDirClass() {
      return this.ascOrder ? "sort-up" : "sort-down";
    },
    getProjects(orderBy) {
      const path = orderBy
        ? `${process.env.VUE_APP_API_URL}/projects?${orderBy}`
        : `${process.env.VUE_APP_API_URL}/projects`;
      axios
        .get(path)
        .then(res => {
          this.projects = res.data;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getCustomers() {
      const path = `${process.env.VUE_APP_API_URL}/customers`;
      axios
        .get(path)
        .then(res => {
          this.customers = res.data;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    handleDeleteProject() {
      this.getProjects();
    },
    initForm() {
      this.addProjectForm.name = "";
      this.addProjectForm.customerName = "";
      this.addProjectForm.price = "";
      this.addProjectForm.checked = [];
      this.addProjectForm.expirationDate = "";
    },
    getPayload() {
      const payload = {
        customer_id: this.selectedCustomerId,
        expiration_date: this.addProjectForm.expirationDate
          ? this.addProjectForm.expirationDate
          : null,
        has_contract: this.addProjectForm.checked.includes("has_contract"),
        has_plan: this.addProjectForm.checked.includes("has_plan"),
        name: this.addProjectForm.name,
        price: this.addProjectForm.price ? this.addProjectForm.price : null,
        work_started: this.addProjectForm.checked.includes("work_started")
      };
      // eslint-disable-next-line
      console.log(payload);
      return payload;
    },
    addProject(payload) {
      const path = `${process.env.VUE_APP_API_URL}/projects`;
      axios
        .post(path, payload)
        .then(() => {
          this.getProjects();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.getProjects();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      const payload = this.getPayload();
      this.addProject(payload);
      this.initForm();
    },
    closeUploadContractModal() {
      this.getProjects();
      this.$refs.uploadContractModal.hide();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      this.initForm();
    }
  },
  computed: {
    customerNames() {
      return this.customers.map(customer => customer.customer_name);
    },
    selectedCustomerId() {
      return this.customers.filter(
        customer => customer.customer_name === this.addProjectForm.customerName
      )[0].id;
    }
  },
  created() {
    this.getProjects();
    this.getCustomers();
  },
  async beforeRouteUpdate(to, from, next) {
    const qs = to.fullPath.replace(to.path, "");
    console.log(to);
    console.log(from);
    const endpoint = `${process.env.VUE_APP_API_URL}/projects${qs}`;
    console.log(endpoint);
    const res = await axios.get(endpoint);
    if (res.status === 200) {
      this.projects = res.data;
      return next();
    }
    return next();
  }
};
</script>

<style>
.container-fluid {
  margin-left: 10%;
  display: flex;
  width: 100%;
}
.modal-backdrop {
  opacity: 0.5;
}
</style>
