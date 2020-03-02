<template>
 <div>
   <form class="login" @submit.prevent="login">
     <h1>Войдите</h1>
     <label>Почтовый ящик</label>
     <input required v-model="email" type="text" placeholder="Name"/>
     <label>Пароль</label>
     <input required v-model="password" type="password" placeholder="Password"/>
     <hr/>
     <button type="submit">Войти</button>
   </form>
 </div>
</template>
<script>
	export default {
		data(){
			return {
				email : "",
            	password : ""
            }
		},
		methods: {
		 	login: function () {
		   		let email = this.email 
		   		let password = this.password
		   		this.$store.dispatch('login', { email, password })
		   		.then(() => this.$router.push('/'))
		   		.catch(err => console.log(err))
		   	}
		}
	}
</script>