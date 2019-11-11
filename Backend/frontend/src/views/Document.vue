<template>
  <div class="document">
        <div v-if="document" class="container">
            <div class="document-data">
                <!-- zamienic potem na document.document_code -->
                <h1>{{ document.slug }}</h1>
                <p class="mb-0">
                    Dodane przez: <span class="author-name">{{ document.author }}</span>
                </p>
                <p class="mb-0">
                    Kod: <span class="author-name">{{ document.document_code }}</span>
                </p>
                <p class="mb-0">
                    Utworzono: <span class="author-name">{{ document.created_at }}</span>
                </p>
                <!-- formularz do zapisu danych  -->
                <div>
                    <p>Liczba punktów <input v-model.number="score" type="number"></p>
                </div>

                <form  @submit.prevent="onSubmit">
                    <div class="card-block">
                        <textarea
                        v-model="newDocumentBody"
                        class="form-control"
                        placeholder="Opisz wybrany dokument"
                        rows="5"
                        ></textarea>
                    </div>
                    <br>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-success">Dodaj opis</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2">{{ error }}</p>
                <!-- koniec formularz do zapisu danych  -->


                <!-- tworzenie zadań -->
                <div  @submit.prevent="onSubmit">
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-danger">Stwórz zadania z pliku</button>
                    </div>
                </div>
            </div>
            <!-- image -->
            <div class="document-image">
                <a v-bind:href="document.document_file">
                    <b-img class="img-full" v-bind:src="document.document_file" fluid-grow alt="Fluid image"></b-img>
                </a>
                <hr />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "Document",
    props: {
        document_id: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            document: {},
            answers: [],
            score: 0,
            newDocumentBody: null,
            error: null,
            userHasAnswered: false,
                showForm: false,
                next: null,
            loadingAnswers: false,
            requestUser: null,
        };
    },
    computed: {
        isDocumentAuthor(){
        // return true if the logged user is also the author of question instance
        return this.document.author === this.requestUser;
        }
    },
    methods:{
        setPageTitle(title) {
                document.title = title;
        },

        setRequestUser(){
            // data for logged user
            this.requestUser = window.localStorage.getItem("username"); //data form loac storage
        },

        getQuestionData() {
            let endpoint = `/api/documents/${this.document_id}/`; // `slug` is a prop, always remember about `/` at the end!
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.document = response.data;
                        console.log(response.data);
                        this.setPageTitle(response.data.slug);
                    }else{
                        this.document = null;
                        this.setPageTitle("404 - Page Not Found");
                }
            })
        },
         onSubmit(){
             console.log(this.newDocumentBody);
         }
    },
    created(){
        this.getQuestionData();
    }
};
</script>

<style scoped>
.container{
    text-align:center;
}
.document-data{
    display: inline-block;
    vertical-align: middle;

}
.document-image{
    display: inline-block;
    vertical-align: middle;

}


</style>
