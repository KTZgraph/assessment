<template>
  <div>
    <div class="img-container">
      <img ref="image" :src="src">
    </div>
    <img :src="destination">
  </div>
</template>

<script>
import Cropper from 'cropperjs';
export default {
  name: "ImageCropper",
  props:{
    src: String
  },
  data(){
    return {
      cropper: {},
      destination: {},
      image: {}    
    }

  },
  mounted(){
    this.image = this.$refs.image;
    this.cropper = new Cropper(this.image,{
      zoomable: false,
      scalable: false,
      // aspectRatio: 1, //idealny kwadrat
      crop:() => {
        const canvas = this.cropper.getCroppedCanvas();
        this.destination = canvas.toDataURL("image/png");
      }


    });
  }

};
</script>

<style scoped>
.img-container{
  width: 640px;
  height: 480px;
}

</style>
