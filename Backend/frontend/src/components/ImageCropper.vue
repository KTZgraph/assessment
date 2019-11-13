<template>
  <div>
    <div class="img-container">
      <img ref="image" :src="imageSrc">
    </div>
    <img :src="destination" class="img-preview">
  </div>
</template>

<script>
import Cropper from 'cropperjs';
export default {
  name: "ImageCropper",
  props:{
        imageSrc: {
          type: String,
          required: true
        }
      },
  data(){
    return {
      cropper: {},
      destination: {},
      image: {},

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
  .img-preview{
    width: 200px;
    height: 200px;
    float: left;
    margin-left: 10px;
  }
</style>
