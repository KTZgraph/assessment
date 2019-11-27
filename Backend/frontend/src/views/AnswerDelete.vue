
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Usuń permamentinie swoja ocenę dla dokumentu</h1>
        
        <p class="text-muted">
            <strong>{{ answer.author }} </strong> &#8901; {{ answer.created_at }}
        </p>
        <p>Liczba punktów dla dokumentu: {{ answer.scores }}</p>
        <p>Opis dokumentu: {{ answer.note }}</p>
    
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
            //http://127.0.0.1:8000/api/documents/57/answer/139/

            let vm = this;
            axios({
                method: 'get',
                url: endpoint,
                })
                .then(function (response) {
                    vm.answer= response.data;
                })
                .catch(function (response) {
                });
        }
    },
    created(){
        this.getDocumentAssessmnet();
    }
}
</script>