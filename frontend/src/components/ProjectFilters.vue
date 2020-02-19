<template>
  <div class="filters">
    <b-form class="w-100">
      <b-form-group
        id="customer-label"
        label="Заказчик:"
        label-for="customer-filter"
      >
        <b-form-select
          id="customer-filter"
          v-on:change="setFilterAttr($event, 'customer_name')"
          :options="customers"
        ></b-form-select>
      </b-form-group>

      <b-form-group id="form-checkboxes-input">
        <b-form-checkbox value="1" unchecked-value="" v-on:change="setFilterAttr($event, 'has_plan')"
          >Съёмка готова?</b-form-checkbox
        >
        <b-form-checkbox value="1" unchecked-value="" v-on:change="setFilterAttr($event, 'work_started')"
          >Работы начаты?</b-form-checkbox
        >
        <b-form-checkbox value="1" unchecked-value="" v-on:change="setFilterAttr($event, 'has_contract')"
          >Договор подписан?</b-form-checkbox
        >
        <b-form-group label="Цена:">
          <b-form-input
            v-on:change="setFilterAttr($event, 'min_price')"
            id="min_price"
            placeholder="От"
            type="number"
          ></b-form-input>
          <b-form-input
            v-on:change="setFilterAttr($event, 'max_price')"
            id="max_price"
            placeholder="До"
            type="number"
          ></b-form-input>
        </b-form-group>
      </b-form-group>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "ProjectFilters",
  data() {
    return {
      form: {
        has_plan: "",
        has_contract: "",
        work_started: "",
        customer_name: "",
        min_price: "",
        max_price: ""
      }
    };
  },
  methods: {
    setFilterAttr(event, attr) {
      this.form[attr] = event;
      this.emitFilterProjects();
    },
    emitFilterProjects() {
      const filters = this.form;
      console.log("here");
      Object.keys(filters).forEach((key) => {
        if (filters[key] === undefined || filters[key] === null || filters[key] === "") {
           delete filters[key];
        } 
      });
      this.$emit("filterProjects", filters);
    }
  },
  props: {
    customers: {}
  }
};
</script>

<style>
.filters {
  margin-top: 100px;
  margin-right: 20px;
}
fieldset {
  margin-top: 40px;
}
#min_price {
  margin-bottom: 10px;
}
</style>
