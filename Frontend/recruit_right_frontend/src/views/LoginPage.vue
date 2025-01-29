<template>
  <div class="page-container">
    <div class="illustration-container">
      <img src="/assets/WelcomePageimage.jpg" alt="Illustration" class="illustration" />
    </div>
    <div class="login-container">
      <h1>Welcome to Recruit Right!</h1>
      <p class="welcome-text">Please sign in to your account and start the adventure.</p>

      <form @submit.prevent="login" class="login-form">
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

        <div class="form-group remember-me">
          <input type="checkbox" id="remember-me" />
          <label for="remember-me">Remember Me</label>
        </div>

        <button type="submit" class="login-button">Sign In</button>
      </form>

      <div class="options">
        <router-link to="/forgot-password">Forgot Password?</router-link>
        <div class="register-text">
          New to Recruit Right? <router-link to="/register">Create an account</router-link>
        </div>
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
      selectedRole: '',
      loginError: null,
    };
  },
  methods: {
    async login() {
  if (this.email && this.password) {
    try {
      const response = await axios.post('http://localhost:8000/api/login/', {
        email: this.email,
        password: this.password,
      });

      // If login is successful, check the user's role
      const userRole = response.data.role;

      // Role-based redirection logic
      if (userRole === 'admin') {
        this.$router.push({ name: 'Admin' });
      } else if (userRole === 'hiring-manager') {
        this.$router.push({ name: 'HiringManager' });
      } else if (userRole === 'sourcing-team') {
        this.$router.push({ name: 'SourcingTeam' });
      } else if (userRole === 'interviewer') {
        this.$router.push({ name: 'Interviewer' });
      } else if (userRole === 'candidate') {
        this.$router.push({ name: 'Candidate' });
      } else {
        alert('Invalid role selected');
      }
    } catch (error) {
      this.loginError = "Invalid login credentials!";
      alert(this.loginError);
    }
  } else {
    alert('Please fill in all fields.');
  }
}
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
    flex: 1.5; /* Increased illustration area */
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
  
  .login-container {
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
  
  .welcome-text {
    font-size: 14px;
    margin-bottom: 20px;
    color: #666;
  }
  
  .login-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    width: 100%; /* Full width for the form */
  }
  
  .form-group {
    text-align: left;
    width: 100%; /* 100% width to make it responsive */
    max-width: 400px; /* Limits the width */
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
    box-sizing: border-box; /* Ensures padding is included in the width */
  }
  
  .remember-me {
    display: flex;
    align-items: center;
    gap: 5px;
  }
  
  .login-button {
    width: 100%;
    max-width: 200px; /* Ensure the button doesn't overflow */
    background-color: #6c63ff;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 18px;
    transition: background-color 0.3s;
  }
  
  .login-button:hover {
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
  
  .register-text {
    margin-top: 10px;
    font-size: 14px;
    color: #666;
  }
  
  .register-text a {
    color: #6c63ff;
    font-weight: bold;
  }
  
  /* Media Queries for responsive design */
  @media (max-width: 600px) {
    .form-group {
      width: 90%; /* Make the form fields take up more width on smaller screens */
    }
  
    .input-field {
      font-size: 14px; /* Adjust font size for better readability */
    }
  
    .login-button {
      width: 90%; /* Ensure the button doesn't overflow on small screens */
    }
  }
  </style>
  