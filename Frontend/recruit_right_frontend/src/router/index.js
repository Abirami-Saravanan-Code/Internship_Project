import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "../views/LoginPage.vue";
import AdminPage from "../views/AdminPage.vue"; // Create empty components for now
import HiringManagerPage from "../views/HiringManagerPage.vue";
import SourcingTeamPage from "../views/SourcingTeamPage.vue";
import InterviewerPage from "../views/InterviewerPage.vue";
import CandidatePage from "../views/CandidatePage.vue";
import UserRegister from '@/views/UserRegister.vue';

const routes = [
  { path: "/", name: "Login", component: LoginPage },
  { path: "/admin", name: "Admin", component: AdminPage },
  { path: "/hiring_manager", name: "HiringManager", component: HiringManagerPage },
  { path: "/sourcing_team", name: "SourcingTeam", component: SourcingTeamPage },
  { path: "/interviewer", name: "Interviewer", component: InterviewerPage },
  { path: "/candidate", name: "Candidate", component: CandidatePage },
  {path: '/userregister',name: 'UserRegister',component: UserRegister},
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
