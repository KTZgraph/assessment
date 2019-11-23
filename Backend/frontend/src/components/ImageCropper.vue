<template>
  <div>
    <div class="img-container">
      <img ref="image" :src="imageSrc">
    </div>
    <img :src="destination" class="img-preview">

    <!-- zapisywanie miniaturki obrazka -->
    <button @>
      Utwórz zadanie
    </button>
  </div>
</template>

<script>
import Cropper from 'cropperjs';
import axios from 'axios';

import { CSRF_TOKEN } from "@/common/csrf_token.js";
import AnswerComponent from "@/components/Answer.vue";
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
    methods:{
    onSumbit(){
      // Upload cropped image to server if the browser supports `HTMLCanvasElement.toBlob`.
      // The default value for the second parameter of `toBlob` is 'image/png', change it if necessary.
      cropper.getCroppedCanvas().toBlob((blob) => {
        const formData = new FormData();
        // Pass the image file name as the third parameter if necessary.
        formData.append('croppedImage', blob);/*, 'example.png' */
        formData.append('imageSrc', imageSrc); /*źródło główengo dokumentu */
        let endpoint = `/api/documents/${this.document_id}/`;
        axios({
          method: 'put',
          url: endpoint,
          withCredentials: true,
          data: bodyUpdateDocument
          })
          .then(function (response) {
              console.log(response);
          })
          .catch(function (response) {
              console.log(response);
          });
      })
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
        this.destination = canvas.toDataURL("image/png"); //img.src = imgurl;
      }
    })
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
