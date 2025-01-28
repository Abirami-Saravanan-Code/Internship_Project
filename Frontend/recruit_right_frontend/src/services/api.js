import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export default {
  getUserRoles() {
    return axios.get(`${API_URL}get-user-roles/`);
  },
  assignUserRole(userId, role) {
    return axios.post(`${API_URL}assign-user-role/`, {
      user_id: userId,
      role: role
    });
  }
};
