<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark bg-light my-navbar">
    <!-- link do głównej strony aplikacji -->
    <router-link :to="{ name: 'home' }" class="navbar-brand">System Oceniania</router-link>
    
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <router-link :to="{ name: 'new-document' }" class="btn btn-sm btn-success">Utwórz dokument</router-link>
            </li>
        </ul>
    </div>
    <!-- Search form -->
    <form class="form-inline">
        <i class="fas fa-search" aria-hidden="false"></i>
        <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search">
    </form>

    <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
            <a class="btn btn-sm btn-danger" href="/accounts/logout/"><strong>Wyloguj</strong></a>
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

.nav-link:hover {
  color: #dc3545 !important;
}
</style>

