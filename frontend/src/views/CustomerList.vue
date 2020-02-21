<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-10">
        <br />
        <br />
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.customer-modal
        >
          Добавить Заказчика
        </button>
        <br />
        <br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Ф.И.О.</th>
              <th scope="col">Телефон</th>
              <th scope="col">Эл. почта</th>
              <th scope="col">Адрес</th>
              <th scope="col">Расчетный счет</th>
              <th scope="col">Проекты</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <customer
              v-for="(customer, item) in customers"
              :key="item"
              :data="customer"
              @deleteCustomer="handleDeleteCustomer()"
            >
              >
            </customer>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      ref="addCustomerModal"
      id="customer-modal"
      title="Добавьте нового заказчика"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-name-group"
          label="Ф.И.О.:"
          label-for="form-name-input"
        >
          <b-form-input
            id="form-name-input"
            type="text"
            required
            v-model="addCustomerForm.customer_name"
            placeholder="Ф.И.О."
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-phone-group"
          label="Телефон:"
          label-for="form-phone-input"
        >
          <b-form-input
            id="form-phone-input"
            type="text"
            v-model="addCustomerForm.phone"
            placeholder="Номер телефона"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="form-email-group"
          label="Электронная почта:"
          label-for="form-email-input"
        >
          <b-form-input
            id="form-email-input"
            type="text"
            v-model="addCustomerForm.email"
            placeholder="Электронная почта"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-address-group"
          label="Адрес:"
          label-for="form-address-input"
        >
          <b-form-input
            id="form-address-input"
            type="text"
            v-model="addCustomerForm.address"
            placeholder="Адрес"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-bank-account-group"
          label="Расчетный счет:"
          required
          label-for="form-bank-account-input"
        >
          <b-form-input
            id="form-bank-account-input"
            type="text"
            v-model="addCustomerForm.payment_account"
            placeholder="Расчетный счет"
          >
          </b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Подтвердить</b-button>
        <b-button type="reset" variant="danger">Отменить</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import Customer from "@/components/Customer";

export default {
  name: "CustomerList",
  components: {
    Customer
  },
  data() {
    return {
      customers: [],
      addCustomerForm: {
        customer_name: "",
        email: "",
        address: "",
        payment_account: "",
        phone: ""
      }
    };
  },
  methods: {
    getCustomers() {
      const path = `${process.env.VUE_APP_API_URL}/customers`;
      console.log(path);
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
    addCustomer(payload) {
      const path = `${process.env.VUE_APP_API_URL}/customers`;
      axios
        .post(path, payload)
        .then(() => {
          this.getCustomers();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.getCustomers();
        });
    },
    handleDeleteCustomer() {
      this.getCustomers();
    },
    initForm() {
      this.addCustomerForm.customer_name = "";
      this.addCustomerForm.email = "";
      this.addCustomerForm.address = "";
      this.addCustomerForm.payment_account = "";
      this.addCustomerForm.phone = "";
    },
    getPayload(form) {
      const payload = {};
      Object.keys(form).forEach(function (field) {
        if (form[field]) {
          payload[field] = form[field];
        }
      });
      return payload;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      const payload = this.getPayload(this.addCustomerForm);
      this.addCustomer(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      this.initForm();
    }
  },
  created() {
    this.getCustomers();
  }
};
</script>

<style>
.container-fluid {
  margin-left: 2%;
  width: 1200px;
}
.modal-backdrop {
  opacity: 0.5;
}
</style>
