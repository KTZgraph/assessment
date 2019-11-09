<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark bg-light my-navbar">
    <!-- link do głównej strony aplikacji -->
    <router-link :to="{ name: 'home' }" class="navbar-brand">System Oceniania</router-link>
    
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <router-link :to="{ name: 'home' }" class="nav-link">Dodaj Dokument</router-link>
            </li>
        </ul>
    </div>
    <form class="form-inline my-2 my-lg-0">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    </form>
    <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
            <a class="nav-link" href="/accounts/logout/">Wyloguj</a>
        </li>
    </ul>

</nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style scoped>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}
.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>

