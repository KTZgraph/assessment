<template>
  <div>
    <div v-if="!answerCreated" class="create-answer">
      <div class="img-container">
        <img ref="image" :src="imageSrc">
      </div>
      <img :src="dataURI" class="img-preview">

      <!-- formularz do zapisu danych  -->
      <form v-if="!answerCreated"   @submit.prevent="createNewAnswer">
          <div>
              <p>Maksymalna liczba punktów za zadanie<input v-model.number="max_scores" type="number"></p>
          </div>
          
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">Utwórz zadanie</button>
          </div>
      </form>
      <!-- koniec formularz do zapisu danych  -->

      <router-link :to="{ name: 'document', params: {document_id: document_id } }" class="btn btn-sm btn-danger">Wróć do dokumentu</router-link>
    </div>

    <!-- Po dodaniu odpowiedzi przekirowuje do oceniania odpowiedzi -->
    <div v-if="answerCreated" class="container">
          <AnswerAssessment 
              :answer_id="answer_id"
              :document_id="document_id"
          />
    </div>

  </div>
</template>

<script>
import Cropper from 'cropperjs';
import axios from 'axios';
import { base64StringToBlob } from 'blob-util'; //string base64 -> blob
import { CSRF_TOKEN } from "@/common/csrf_token.js";
import AnswerAssessment from "@/views/AnswerAssessment.vue";
export default {
  name: "ImageCropper",
  props:{
        imageSrc: {
          type: String,
          required: true
        },
        document_id: {
          type: String,
          required: true
        }
      },
  components: {
    AnswerAssessment
  },
  data(){
    return {
      max_scores: null,
      cropper: {},
      dataURI: {},
      image: {},
      showPopup: false,
      answerCreated: false,
      answer: {},
      answer_id: null
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

      let vm = this;
      axios({
          method: 'post',
          url: endpoint,
          withCredentials: true,
          data: formDataNewAnswer
          })
          .then(function (response) {
              vm.answer_id = response.data.id;
              vm.answerCreated = true;
          })
          .catch(function (response) {
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
