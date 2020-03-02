<template>
  <div>
    <form @submit.prevent="login" class="login-form">
      <h2 class="text-center">Войдите в аккаунт</h2>
      <div class="form-group">
        <input
          class="form-control"
          required
          v-model="email"
          type="text"
          placeholder="Почтовый ящик"
        />
      </div>

      <div class="form-group">
        <input
          type="password"
          v-model="password"
          class="form-control"
          placeholder="Password"
          required
        />
      </div>

      <div class="form-group">
        <button type="submit" class="btn btn-primary btn-block">Войти</button>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    login() {
      const email = this.email;
      const password = this.password;
      this.$store
        .dispatch("login", { email, password })
        .then(() => this.$router.push({ name: "ProjectList" }))
        .catch(err => console.log(err));
    }
  }
};
</script>
<style>
.login-form {
  width: 340px;
  margin: 50px auto;
}
.login-form form {
  margin-bottom: 15px;
  background: #f7f7f7;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
  padding: 30px;
}
.login-form h2 {
  margin: 0 0 15px;
}
.form-control,
.btn {
  min-height: 38px;
  border-radius: 2px;
}
.btn {
  font-size: 15px;
  font-weight: bold;
}
</style>
