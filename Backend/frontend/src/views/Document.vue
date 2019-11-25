<template>
  <div class="document">
        <div v-if="document" class="container">
            <div class="document-data">
                <!-- zamienic potem na document.document_code -->
                <h1>{{ document.slug }}</h1>
                <p class="mb-0">
                    Utworzono: <span class="author-name">{{ document.created_at }}</span>
                </p>
                <p class="mb-0">
                    Dokument dodany przez: <span class="author-name">{{ document.author }}</span>
                </p>
                <p class="mb-0">
                    Kod dokumentu: <span class="author-name">{{ document.document_code }}</span>
                </p>
                <!-- formularz do zapisu danych  -->
                <form  @submit.prevent="onSubmit">
                    <div>
                        <p>Liczba punktów <input v-model.number="scores" type="number"></p>
                    </div>
                    <div class="card-block">
                        <textarea
                        v-model="newDocumentDescriptionBody"
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
                <!-- <div  @submit.prevent="onSubmit">
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-danger">Stwórz zadania z pliku</button>
                    </div>
                </div> -->

                <!-- Opcja dodawania odpowiedzi do dokumentu -->
                <div class="card-footer px-3">
                    <router-link
                        :to="{ name: 'answer-creator', params: { document_id: document_id}}"
                        class="document-link"
                    >
                    <button type="submit" class="btn btn-sm btn-danger">Stwórz zadania z pliku</button>
                    </router-link>
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
        <hr>
        <!--  Koniec dodawania odpowiedzi do dokumentu -->

        <!-- wysiwetlanie dodanych opinii o doukemncie -->
        <h1>Oceny całego dokumentu</h1>
        <div class="container">
            <DocumentAssessment 
                v-for="(documentAssessment, index) in documentAssessments"
                :documentAssessment="documentAssessment"
                :v-key="index"
            />
        </div>
        <!-- loading more data button section -->
        <div class="my-4">
            <p v-show="loadingDocumentAssessments">...loading...</p>
            <button
            v-show="nextDocumentAssessments"
            @click="getDocumentAssessments"
            class="btn btn-sm btn-outline-success"
            >Load More
            </button>
        </div>
        <!-- end loading more data button section -->
        <!-- koniec opinii o dokumencie -->

        <!-- Wyświetlanie odpowiedzi do dokumentu -->
        <div class="container">
            <AnswerComponent 
                v-for="(answer, index) in answers"
                :answer="answer"
                :v-key="index"
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";
import AnswerComponent from "@/components/Answer.vue";
import DocumentAssessment from "@/components/DocumentAssessment.vue";
export default {
    name: "Document",
    props: {
        document_id: {
            type: String,
            required: true
        }
    },
    components: {
        AnswerComponent,
        DocumentAssessment,
    },
    data() {
        return {
            document: {},
            documentAssessments: [],
            nextDocumentAssessments: null,
            loadingDocumentAssessments: false,
            answers: [],
            scores: 0,
            newDocumentDescriptionBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false,
            newAnswerBody: null,
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

        getDocumentData() {
            let endpoint = `/api/documents/${this.document_id}/`;
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.document = response.data;
                        this.setPageTitle(response.data.slug);
                    }else{
                        this.document = null;
                        this.setPageTitle("404 - Page Not Found");
                }
            })
        },
        getDocumentAssessments() {
            let endpoint = `/api/documents/${this.document_id}/documentassessments/`;
            if (this.nextDocumentAssessments){
                endpoint = this.nextDocumentAssessments;
            }
            this.loadingDocuments = true;
            
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.documentAssessments.push(...response.data.results);
                        this.loadingDocumentAssessments = false;
                        if (response.data.next) { //url from django REST for next data (pagination)
                            this.nextDocumentAssessments = response.data.next;
                        }else{ //if no addditional data exists
                            this.nextDocumentAssessments = null;
                        }
                    }else{
                }
            })
        },
        getDocumentsAnswers(){
            let endpoint = `/api/documents/${this.document_id}/answers/`;
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.answers.push(...response.data.results);
                    }else{
                        this.answers = null;
                        this.setPageTitle("404 - Page Not Found");
                }
            })

        },
        onSubmit(){
            //Dodawanie opisu dokumentu przez użytkownika
            let endpoint = `/api/documents/${this.document_id}/documentassessment/`;
            
            let bodyUpdateDocument = new FormData();
            // opis dokumentu
            if (this.newDocumentDescriptionBody){
                bodyUpdateDocument.set("description",this.newDocumentDescriptionBody)
            }
            //punkty
            if (this.scores){
                // czy można aktualizaowac punkty
                bodyUpdateDocument.set("scores",this.scores)
            }

            //brak aktualizacji obrazka - na jego podstawie są tworzone przeciez zadania
            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };

            axios({
                method: 'post',
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
         }
    },
    created(){
        this.getDocumentData();
        this.getDocumentsAnswers();
        this.getDocumentAssessments();
    }
};
</script>

<style>
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
.answer-added{
    font-weight: bold;
    color: green;
}
.error{
    font-weight: bold;
    color: red;
}
</style>
