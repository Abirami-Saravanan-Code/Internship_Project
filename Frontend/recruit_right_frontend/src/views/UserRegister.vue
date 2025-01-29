<template>
    <div class="page-container">
      <div class="illustration-container">
        <img src="/WelcomePageimage.jpg" alt="Illustration" class="illustration" />
      </div>
      <div class="register-container">
        <h1>Create an Account</h1>
        <p class="register-text">Join Recruit Right to start your journey.</p>
  
        <form @submit.prevent="register" class="register-form">
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="text" v-model="email" id="email" class="input-field" required />
          </div>
  
          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" v-model="password" id="password" class="input-field" required />
          </div>
  
          <div class="form-group">
            <label for="role">Select Your Role:</label>
            <select v-model="selectedRole" id="role" class="input-field" required>
              <option value="" disabled>Select role</option>
              <option value="admin">Admin</option>
              <option value="hiring-manager">Hiring Manager</option>
              <option value="sourcing-team">Sourcing Team</option>
              <option value="interviewer">Interviewer</option>
              <option value="candidate">Candidate</option>
            </select>
          </div>
  
          <div class="form-group">
            <label for="confirm-password">Confirm Password:</label>
            <input type="password" v-model="confirmPassword" id="confirm-password" class="input-field" required />
          </div>
  
          <button type="submit" class="register-button">Sign Up</button>
        </form>
  
        <div class="options">
          <router-link to="/login">Already have an account? Sign in</router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        email: '',
        password: '',
        confirmPassword: '',
        selectedRole: '',
        registerError: null,
      };
    },
    methods: {
      async register() {
        if (this.email && this.password && this.confirmPassword && this.selectedRole) {
          if (this.password === this.confirmPassword) {
            try {
              const response = await axios.post('http://localhost:8000/api/register/', {
                email: this.email,
                password: this.password,
                role: this.selectedRole,
              });
  
              if (response.data.success) {
                alert('Registration successful! Please log in.');
                this.$router.push('/login');
              } else {
                this.registerError = 'Registration failed. Please try again.';
                alert(this.registerError);
              }
            } catch (error) {
              console.error(error);
              this.registerError = 'An error occurred during registration. Please try again.';
              alert(this.registerError);
            }
          } else {
            alert('Passwords do not match.');
          }
        } else {
          alert('Please fill in all fields.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .page-container {
    display: flex;
    min-height: 100vh;
    background-color: #f5f6fa;
  }
  
  .illustration-container {
    flex: 1.5;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f0f4ff;
    padding: 20px;
  }
  
  .illustration {
    max-width: 80%;
    height: auto;
  }
  
  .register-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
    text-align: center;
  }
  
  h1 {
    font-size: 24px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .register-text {
    font-size: 14px;
    margin-bottom: 20px;
    color: #666;
  }
  
  .register-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    width: 100%;
  }
  
  .form-group {
    text-align: left;
    width: 100%;
    max-width: 400px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-size: 14px;
    color: #555;
  }
  
  .input-field {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 16px;
    box-sizing: border-box;
  }
  
  .register-button {
    width: 100%;
    max-width: 200px;
    background-color: #6c63ff;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 18px;
    transition: background-color 0.3s;
  }
  
  .register-button:hover {
    background-color: #574dcf;
  }
  
  .options {
    margin-top: 20px;
  }
  
  .options a {
    color: #6c63ff;
    text-decoration: none;
    font-size: 14px;
  }
  
  .options a:hover {
    text-decoration: underline;
  }
  
  /* Media Queries for responsive design */
  @media (max-width: 600px) {
    .form-group {
      width: 90%;
    }
  
    .input-field {
      font-size: 14px;
    }
  
    .register-button {
      width: 90%;
    }
  }
  </style>
  