<template>
  <div class="login-container">
    <div class="login-form">
      <form @submit.prevent="submitForm">
        <h1 class="title">Register</h1>
        <div class="content">
          <div class="input-field">
            <input
              type="email"
              placeholder="Email"
              name="username"
              autocomplete="nope"
              v-model="username"
            />
          </div>
          <div class="input-field">
            <input type="password" placeholder="Password" v-model="password1" />
          </div>
          <div class="input-field">
            <input
              type="password"
              placeholder="Re-enter password"
              v-model="password2"
            />
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </div>
        <div class="action">
          <button>Sign in</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { toast } from "bulma-toast";
export default {
  name: "Signup",
  data() {
    return {
      username: "",
      password1: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      const signupForm = {
        username: this.username,
        password: this.password1,
      };
      await axios
        .post("api/v1/users/", signupForm)
        .then((response) => {
          console.log(response.data);
          toast({
            message: "Account created, please log in",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
          this.$router.push("/log-in");
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              console.log(error.response.data);
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again");
          }
        });
    },
  },
};
</script>

<style>
.login-container {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}
.login-form {
  background: #fff;
  width: 500px;
  margin: 65px auto;
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  flex-direction: column;
  border-radius: 4px;
  box-shadow: 0 2px 25px rgba(0, 0, 0, 0.2);
}
.login-form h1 {
  padding: 35px 35px 0 35px;
  font-weight: 300;
}
.login-form .content {
  padding: 35px;
  text-align: center;
}
.login-form .input-field {
  padding: 12px 5px;
}
.login-form .input-field input {
  font-size: 16px;
  display: block;
  font-family: "Rubik", sans-serif;
  width: 100%;
  padding: 10px 1px;
  border: 0;
  border-bottom: 1px solid #747474;
  outline: none;
  -webkit-transition: all 0.2s;
  transition: all 0.2s;
}
.login-form .input-field input::-webkit-input-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input::-moz-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input:-ms-input-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input::-ms-input-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input::placeholder {
  text-transform: uppercase;
}
.login-form .input-field input:focus {
  border-color: #222;
}
.login-form a.link {
  text-decoration: none;
  color: #747474;
  letter-spacing: 0.2px;
  text-transform: uppercase;
  display: inline-block;
  margin-top: 20px;
}
.login-form .action {
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  flex-direction: row;
}
.login-form .action button {
  width: 100%;
  border: none;
  padding: 18px;
  font-family: "Rubik", sans-serif;
  cursor: pointer;
  text-transform: uppercase;
  background: #e8e9ec;
  color: #777;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 0;
  letter-spacing: 0.2px;
  outline: 0;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.login-form .action button:hover {
  background: #d8d8d8;
}
.login-form .action button:nth-child(2) {
  background: #2d3b55;
  color: #fff;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 4px;
}
.login-form .action button:nth-child(2):hover {
  background: #3c4d6d;
}
</style>
