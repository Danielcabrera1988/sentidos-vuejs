import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/menu",
    name: "menu",
    component: () => import("../views/MenuView.vue"),
  },
  {
    path: "/reservas",
    name: "reservas",
    component: () => import("../views/ReservasView.vue"),
  },
  {
    path: "/blog",
    name: "blog",
    component: () => import("../views/BlogView.vue"),
  },
  {
    path: "/newUser",
    name: "newUser",
    component: () => import("../views/NewUser.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
