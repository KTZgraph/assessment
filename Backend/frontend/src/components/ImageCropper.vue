<template>
  <div>
    <div class="img-container">
      <img ref="image" :src="imageSrc">
    </div>
    <img :src="dataURI" class="img-preview">

    <!-- zapisywanie miniaturki obrazka -->
        <button
          @click="createNewAnswer"
          class="btn btn-sm btn-outline-success"
          >Utwórz zadanie
        </button>
  </div>
</template>

<script>
import Cropper from 'cropperjs';
import axios from 'axios';
import { base64StringToBlob } from 'blob-util'; //string base64 -> blob
import { CSRF_TOKEN } from "@/common/csrf_token.js";
import AnswerComponent from "@/components/Answer.vue";
export default {
  name: "ImageCropper",
  props:{
        imageSrc: {
          type: String,
          required: true
        },
        document_id: {
          type: Number,
          required: true
        }
      },
  data(){
    return {
      cropper: {},
      dataURI: {},
      image: {},
    }

  },
    methods:{
    createNewAnswer(){
      // bardziej zoptymailozwana wersja 
      // http://eugeneware.com/software-development/converting-base64-datauri-strings-into-blobs-or-typed-array
      // convert to typed array
      var BASE64_MARKER = ';base64,';
      var base64Index = this.dataURI.indexOf(BASE64_MARKER) + BASE64_MARKER.length;
      var base64 = this.dataURI.substring(base64Index);
      var arr = Buffer.from(base64, 'base64');
      
      // convert to blob and show as image
      let blob = new Blob([arr], { type: 'image/png' });
      // const blob = base64StringToBlob(this.dataURI) //, contentType);

      let endpoint = `/api/documents/${this.document_id}/answer/`;
      const formDataNewAnswer = new FormData();
      // Pass the image file name as the third parameter if necessary.
      formDataNewAnswer.append('answer_file', blob);/*, 'example.png' */
      formDataNewAnswer.append('max_score', 14);/*, 'example.png' */

      axios.defaults.headers.common = {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFTOKEN': CSRF_TOKEN
      };

      axios({
          method: 'post',
          url: endpoint,
          withCredentials: true,
          data: formDataNewAnswer
          })
          .then(function (response) {
              console.log(response);
          })
          .catch(function (response) {
              console.log(response);
          });
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
        this.dataURI = canvas.toDataURL("image/png"); //img.src = imgurl;
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
