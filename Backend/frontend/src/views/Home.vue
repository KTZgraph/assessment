<template>
  <div class="home">
    <ul>
    <li v-for="doc in documents"> 
      {{doc.author}} 
      {{doc.document_file}}
      <img v-bind:src="doc.document_file" />



    </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "home",
  components: {
  },
  data(){
    return{
      msg: "Wszystkie dokuemnty tutaj",
      documents: []
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/api/documents/')
      .then(response => (this.documents = response.data))
  }
};
</script>
