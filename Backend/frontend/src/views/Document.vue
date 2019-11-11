<template>
  <div class="document">
      <h1>DOCUMENT</h1>
        <div v-if="document" class="container">

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
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
                showForm: false,
                next: null,
            loadingAnswers: false,
            requestUser: null
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
        }
    },
    created(){
        this.getQuestionData();
    }
};
</script>

<style scoped>


</style>
