<template>
  <div class="home">
      <!-- galeria wszystkich dokumentow -->
      <div class="gallery">
        <div class="gallery-panel" 
            v-for="doc in documents"
            :key="doc.id">
          <p class="mb-0">Autor:
            <span class="document-author">{{ doc.author }}</span>
          </p>
          <span class="document-data">{{ doc.created_at }}</span>
        <!--  -->
        <!--  -->
          <h2>
            <router-link
              :to="{ name: 'document', params: { document_id: doc.id }}"
              class="document-link"
            >
              <b-img class="img-mini" v-bind:src="doc.document_file" fluid-grow alt="Fluid image"></b-img>
            </router-link>
          </h2>
          <div class="preview-img-button">
            <a v-bind:href="doc.document_file">
              <button type="submit" class="btn btn-sm btn-success">Podgląd pliku</button>
            </a>
          </div>
          <hr>
        </div>
      </div>


      <!-- loading more data button section -->
      <div class="my-4 load-more-data">
        <p v-show="loadingDocuments">...loading...</p>
        <button
          v-show="next"
          @click="getDocuments"
          class="btn btn-sm btn-outline-info"
          >Więcej dokumentów
        </button>
      </div>
      <!-- end loading more data button section -->

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
      loadingDocuments: false,
      requestUser: null
    }
  },
  methods:{
    onSubmit(){
    },
    getDocuments(){
      let endpoint = "api/documents/";
      if (this.next){
        endpoint = this.next;
      }
      this.loadingDocuments = true;
      axios.get(endpoint)
        .then(response => {
          this.documents.push(...response.data.results);
          this.loadingDocuments = false;
          if (response.data.next) { //url from django REST for next data (pagination)
            this.next = response.data.next;
          }else{ //if no addditional data exists
            this.next = null;
          }
        })
    },
    setRequestUser(){
      // data for logged user
      this.requestUser = window.localStorage.getItem("username"); //data form loac storage
    }
  },
  created(){
    this.getDocuments();
    this.setRequestUser();
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


.home {
  width: 100%;
  height: auto;
}
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
    grid-gap: 1rem;
    max-width: 80rem;
    margin: 5rem auto;
    padding: 0 5rem;
    text-align:center;
}
.gallery-panel img {
    width: 100%;
    height: 22vw;
    object-fit: cover;
    border-radius: 0.75rem;

}
.load-more-data{
  text-align:center;
}

</style>