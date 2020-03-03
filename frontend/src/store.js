import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    status: "",
    token: localStorage.getItem("token") || ""
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, token) {
      state.status = "success";
      state.token = token;
    },
    auth_error(state) {
      state.status = "error";
    },
    cleanToken(state) {
      state.status = "";
      state.token = "";
    }
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: `${process.env.VUE_APP_API_URL}/auth/login`,
          data: user,
          method: "POST"
        })
          .then(resp => {
            const token = `Bearer ${resp.data.auth_token}`;
            localStorage.setItem("user-token", token);
            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", token);
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            localStorage.removeItem("user-token");
            reject(err);
          });
      });
    },
    cleanToken({ commit }) {
      return new Promise((resolve, reject) => {
        commit("cleanToken");
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        // refactor this code a bit
        axios({
          url: `${process.env.VUE_APP_API_URL}/auth/logout`,
          method: "POST"
        })
          .then(resp => {
            commit("cleanToken");
            if (resp.status !== "200") {
              console.log(resp);
            }
            localStorage.removeItem("token");
            delete axios.defaults.headers.common["Authorization"];
            resolve(resp);
          })
          .catch(err => {
            commit("cleanToken");
            localStorage.removeItem("token");
            delete axios.defaults.headers.common["Authorization"];
            reject(err);
          });
      });
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status
  }
});
