<template>
    <div class="admin-page">
      <h1>Admin Dashboard</h1>
      <div class="admin-actions">
        <button @click="createUser">Create User</button>
        <button @click="deactivateUser">Deactivate User</button>
        <button @click="deleteUser">Delete User</button>
        <button @click="managePermissions">Manage Permissions</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AdminPage",
    methods: {
      createUser() {
        alert("Create User functionality coming soon!");
      },
      deactivateUser() {
        alert("Deactivate User functionality coming soon!");
      },
      deleteUser() {
        alert("Delete User functionality coming soon!");
      },
      managePermissions() {
        alert("Manage Permissions functionality coming soon!");
      }
    }
  };
  </script>
  
  <style scoped>
  .admin-page {
    padding: 20px;
  }
  .admin-actions {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  button {
    padding: 10px 15px;
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #2563eb;
  }
  </style>
  