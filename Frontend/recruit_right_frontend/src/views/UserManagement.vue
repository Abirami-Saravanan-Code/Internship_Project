<template>
    <div>
      <h2>User Management</h2>
  
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Role</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>
              <select v-model="user.selectedRole" @change="assignRole(user)">
                <option v-for="role in roles" :key="role" :value="role">{{ role }}</option>
              </select>
            </td>
            <td>
              <button @click="assignRole(user)">Assign Role</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import api from '@/services/api'; // Import the API service you created
  
  export default {
    data() {
      return {
        users: [],        // Store the list of users
        roles: ['Admin', 'Hiring Manager', 'Sourcing Team', 'Interviewer', 'Candidate'],  // Define the available roles
      };
    },
    mounted() {
      this.fetchUsers();  // Fetch the users when the component is mounted
    },
    methods: {
      fetchUsers() {
        api.getUserRoles().then(response => {
          this.users = response.data;
        }).catch(error => {
          console.error("Error fetching users:", error);
        });
      },
      assignRole(user) {
        api.assignUserRole(user.id, user.selectedRole).then(() => {
          alert(`Role assigned successfully to ${user.name}`);
        }).catch(error => {
          console.error("Error assigning role:", error);
        });
      }
    }
  };
  </script>
  
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 8px;
    border: 1px solid #ddd;
  }
  select {
    padding: 5px;
  }
  button {
    padding: 6px 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
  </style>
  