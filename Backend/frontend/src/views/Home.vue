<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="doc in documents"
           :key="doc.id">
        <p class="mb-0">Dodane przez:
          <span class="document-author">{{ doc.author }}</span>
        </p>
      <!--  -->
      <a v-bind:href="doc.document_file">
        <b-img class="img-mini" v-bind:src="doc.document_file" fluid-grow alt="Fluid image"></b-img>
      </a>
      <!--  -->
        <h2>
          <!-- <router-link
            :to="{ name: 'document', params: { slug: doc.slug }}"
            class="document-link"
          >{{ document.content }}
          </router-link> -->
        </h2>
         <a v-bind:href="doc.document_file"><p>Podgląd</p></a>
        <hr>
      </div>
      <!-- loading more data button section -->
      <div class="my-4">
        <p v-show="loadingDocuments">...loading...</p>
        <button
          v-show="next"
          @click="getDocuments"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
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
      documents: [],
      next: null, //dla paginacji zdjeć
      loadingDocuments: false
    }
  },
  methods:{
    onSubmit(){
      console.log("eeeeeeeeeeeee");
    },
    getDocuments(){
      let endpoint = "http://127.0.0.1:8000/api/documents/";
      if (this.next){
        endpoint = this.next;
      }
      this.loadingDocuments = true;
      axios.get(endpoint)
        .then(response => {
          this.documents.push(...response.data.results);
          console.log(response.data.next);
          this.loadingDocuments = false;
          if (response.data.next) { //url from django REST for next data (pagination)
            this.next = response.data.next;
          }else{ //if no addditional data exists
            this.next = null;
          }
        })
    }
  },
  created(){
    this.getDocuments();
  }
};
</script>

<style scoped>
.img-mini{
    max-width:200px;
    max-height:200px;
}
.document-author{
  font-weight: bold;
  color: #DC3545;
}
.document-link{
  font-weight: bold;
  color: black;
}
.document-link:hover{
  color: #343A40;
  text-decoration: none;
}

</style>