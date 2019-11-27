<template>
  <div class="document">
            <b-container v-if="document" class="container">
                <!-- gorny wiersz -->
                <b-row>
                    <!-- lewa gorna kolumna -->
                    <b-col>
                        <div class="document-data">
                            <p class="mb-0">
                                Utworzono: <span class="author-name">{{ document.created_at }}</span>
                            </p>
                            <p class="mb-0">
                                Dokument dodany przez: <span class="author-name">{{ document.author }}</span>
                            </p>
                            <p class="mb-0">
                                Kod dokumentu: <span class="author-name">{{ document.document_code }}</span>
                            </p>
                            <!-- Opcje dodawania oceny - juz dodal ocene/ nie dodal/ chce zmodyfikowac -->
                            <div v-if="userHasAnswered">
                                <p class="documentAssessment-added"> Już dodałeś ocenę do tego pliku </p>
                            </div>
                            <div v-else-if="!showForm">
                                <button
                                class="btn tbn-sm btn-success"
                                @click="showForm = true"
                                >Oceń dokument
                                </button>
                            </div>
                            <div v-else>
                                <!-- formularz do zapisu danych  -->
                                <form v-if="showForm" @submit.prevent="addDocumentAssessment">
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
                            </div>


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
                    </b-col>
                    <b-col>
                        <div class="document-image">
                            <a v-bind:href="document.document_file">
                                <b-img class="img-full" v-bind:src="document.document_file" fluid-grow alt="Fluid image"></b-img>
                            </a>
                        </div>
                    </b-col>
                </b-row>


        <!-- dolny wiersz -->
        <b-row>
            <!-- lewa dolna kolumna -->
            <b-col>
                <h1>Oceny całego dokumentu</h1>
                <div class="container">
                    <DocumentAssessment 
                        v-for="(documentAssessment, index) in documentAssessments"
                        :documentAssessment="documentAssessment"
                        :v-key="index"
                    />
                </div>
                <div class="my-4">
                    <p v-show="loadingDocumentAssessments">...loading...</p>
                    <button
                    v-show="nextDocumentAssessments"
                    @click="getDocumentAssessments"
                    class="btn btn-sm btn-outline-info"
                    >Więcej ocen dokumentu
                    </button>
                </div>
            </b-col>
            
            <!-- prawa dolna kolumna -->
            <b-col>
                <h1>Pojedyncze zadania </h1>
                <div class="container">
                    <AnswerComponent 
                        v-for="(answer, index) in answers"
                        :answer="answer"
                        :document_id="document_id"
                        :v-key="index"
                    />
                </div>

                <div class="my-4">
                    <p v-show="loadingAnswers">...loading...</p>
                    <button
                    v-show="nextAnswers"
                    @click="getDocumentAnswers"
                    class="btn btn-sm btn-outline-info"
                    >Więcej zadań
                    </button>
                </div>

            </b-col>
        </b-row>
    </b-container>

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
            type: String | Number,
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
            nextAnswers: null,
            loadingAnswers: false,
            scores: 0,
            newDocumentDescriptionBody: null,
            newAnswerBody: null,
            next: null,
            requestUser: null,
            error: null,
            userHasAnswered: false,
            showForm: false,
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
        getDocumentData() {
            let endpoint = `/api/documents/${this.document_id}/`;
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.document = response.data;
                        this.userHasAnswered = response.data.user_has_answered;
                        console.log("this.userHasAnswered: ", this.userHasAnswered)
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
                        if (response.data.next) {
                            this.nextDocumentAssessments = response.data.next;
                        }else{
                            this.nextDocumentAssessments = null;
                        }
                    }
            })
        },
        getDocumentAnswers(){
            let endpoint = `/api/documents/${this.document_id}/answers/`;
            if (this.nextAnswers){
                endpoint = this.nextAnswers;
            }
            this.loadingAnswers = true;

            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.answers.push(...response.data.results);
                        this.loadingAnswers = false;
                        if (response.data.next) {
                            this.nextAnswers = response.data.next;
                        }else{ 
                            this.nextAnswers = null;
                        }
                    }
            })
        },
        addDocumentAssessment(){ //TODO: jedna opinia na jednego użytkownika
            //Dodawanie opisu dokumentu przez użytkownika
            let endpoint = `/api/documents/${this.document_id}/documentassessment/`;
            
            let bodyUpdateDocument = new FormData();
            if (this.newDocumentDescriptionBody){
                bodyUpdateDocument.set("description",this.newDocumentDescriptionBody)
            }
            if (this.scores){
                bodyUpdateDocument.set("scores",this.scores)
            }

            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };

            let vm = this;
            axios({
                method: 'post',
                url: endpoint,
                withCredentials: true,
                data: bodyUpdateDocument
                })
                .then(function (response) {
                    vm.documentAssessments.unshift(response.data);

                })
                .catch(function (response) {
                    console.log(response);
                });
            this.userHasAnswered = true;
         }
    },
    created(){
        this.getDocumentData();
        this.getDocumentAnswers();
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
.error{
    font-weight: bold;
    color: red;
}
.documentAssessment-added{
    font-weight: bold;
    color: green;
}
</style>
