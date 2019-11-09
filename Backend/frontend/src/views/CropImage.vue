<template>
  <div class="cropp-class">
    {{msg}}
  </div>
</template>

<script>
export default {
  name: "CropImage",
  data() {
    return{
      msg: "Wycinanie obrazka tutaj"
    }
  }
};
</script>

<style scoped>
.cropp-class{
  width: 100%;
}

</style>
