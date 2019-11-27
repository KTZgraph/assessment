
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Usuń permamentinie swoja ocenę dla dokumentu</h1>
        <p>Plik: {{ answer.answer_file }}</p>
        <div class="img-answer">
            <a v-bind:href="answer.answer_file">
                <b-img class="img-full" v-bind:src="answer.answer_file" fluid-grow alt="Fluid image"></b-img>
            </a>
        </div>
        <p class="text-muted">
            <strong>{{ answer.author }} </strong> &#8901; {{ answer.created_at }}
        </p>
        <p>MAksymalna punktów dla zadania: {{ answer.max_score }}</p>    
            <button
                @click="deleteAnswer"
                type="submit"
                class="btn btn-danger"
            >Usuń zadanie
            </button>

        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "DocumentAssessmentEditor",
    props: {
        answer_id: {
            type: String | Number,
            required: true
        },
        document_id: {
            type: Number | String,
            required: true
        }
    },
    data(){
        return{
            error: null,
            scores: null,
            answer: null
        }
    },
    methods:{
        deleteAnswer(){
            //usuwanie opinie o calycm dokumencie
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/`;

            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };

            let vm = this;
            let document_id_local = this.document_id;
            axios({
                method: 'delete',
                url: endpoint,
                withCredentials: true,
                })
                .then(function (response) {
                    vm.$router.push({name: 'document', params: {document_id: document_id_local}})
                })
                .catch(function (response) {
                    vm.$router.push({name: 'document', params: {document_id: document_id_local}})
                });
        },
        
        getAnswer(){
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/`;

            let vm = this;
            axios({
                method: 'get',
                url: endpoint,
                })
                .then(function (response) {
                    console.log(response)
                    vm.answer= response.data;
                })
                .catch(function (response) {
                });
        }
    },
    created(){
        this.getAnswer();
    }
}
</script>

<style scoped>
.img-answer{
    max-width: 600px;
    height: auto;
}
</style>