<template>
  <nav class="nav__main">
    <ul class="nav__main__nav__menu">
      <li class="nav__menu__item">
        <router-link class="nav__menu__item__link" to="/">Home</router-link>
      </li>
      <li class="nav__menu__item">
        <router-link class="nav__menu__item__link" to="/menu">Menu</router-link>
      </li>
      <li class="nav__menu__item">
        <router-link class="nav__menu__item__link" to="reservas"
          >Reservas</router-link
        >
      </li>
      <li class="nav__menu__item">
        <router-link class="nav__menu__item__link" to="/blog">Blog</router-link>
      </li>
    </ul>

    <!-- Right Nav -->
    <ul class="nav__menu__right">
      <li class="nav__menu__item">

        <router-link class="nav__menu__item__link link__login" to="/login">Login</router-link>
        <router-link class="nav__menu__item__link link__register" to="/newUser">Register</router-link>
        
      </li>
    </ul>
  </nav>
</template>

<style  scoped>
@import "../assets/Styles/StyleNav.css";
</style>