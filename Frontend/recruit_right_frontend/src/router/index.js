import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "../views/LoginPage.vue";
import AdminPage from "../views/AdminPage.vue";
import HiringManagerPage from "../views/HiringManagerPage.vue";
import SourcingTeamPage from "../views/SourcingTeamPage.vue";
import InterviewerPage from "../views/InterviewerPage.vue";
import CandidatePage from "../views/CandidatePage.vue";
import UserRegister from '@/views/UserRegister.vue';

// Define routes with meta for role-based access control
const routes = [
  { path: "/", name: "Login", component: LoginPage },
  { 
    path: "/admin", 
    name: "Admin", 
    component: AdminPage,
    meta: { requiresRole: 'Admin' } 
  },
  { 
    path: "/hiring_manager", 
    name: "HiringManager", 
    component: HiringManagerPage, 
    meta: { requiresRole: 'Hiring Manager' }
  },
  { 
    path: "/sourcing_team", 
    name: "SourcingTeam", 
    component: SourcingTeamPage, 
    meta: { requiresRole: 'Sourcing Team' }
  },
  { 
    path: "/interviewer", 
    name: "Interviewer", 
    component: InterviewerPage, 
    meta: { requiresRole: 'Interviewer' }
  },
  { 
    path: "/candidate", 
    name: "Candidate", 
    component: CandidatePage, 
    meta: { requiresRole: 'Candidate' }
  },
  { path: '/userregister', name: 'UserRegister', component: UserRegister },
];

// Create the router with navigation guards
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard to check role access
router.beforeEach((to, from, next) => {
  const user = JSON.parse(localStorage.getItem('user')) || null; // Get user from localStorage (or use your preferred method)
  
  if (to.meta.requiresRole) {
    // Check if user is logged in and has the right role
    if (!user) {
      next({ name: 'Login' }); // Redirect to login if not logged in
    } else if (user.role !== to.meta.requiresRole) {
      next({ name: 'Login' }); // Redirect to login if user doesn't have the required role
    } else {
      next(); // Allow access to the page
    }
  } else {
    next(); // If no role required, just continue
  }
});

export default router;
