
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Usuń swoja ocenę dla pojedynczego zadania</h1>
        <p class="text-muted">
            <strong>{{ answerAssessment.author }} </strong> &#8901; {{ answerAssessment.created_at }}
        </p>
        <p>Liczba punktów dla dokumentu: {{ answerAssessment.scores }}</p>
        <p>Opis dokumentu: {{ answerAssessment.note }}</p>
    
            <button
                @click="deleteAnswerAssessment"
                type="submit"
                class="btn btn-danger"
            >Usuń swoja odpowiedz
            </button>

        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "AnswerAssessmentEditor",
    props: {
        answer_id: {
            type: String | Number,
            required: true
        },
        document_id: {
            type: Number | String,
            required: true
        },
        answerAssessment_id: {
            type: Number | String,
            required: true
        }
    },
    data(){
        return{
            error: null,
            scores: null,
            newAssessmentDescriptionBody: null,
            answerAssessment: null
        }
    },
    methods:{        
        deleteAnswerAssessment(){
            //usuwanie opinie o pojedynczym zadaniu
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/answerassessment/${this.answerAssessment_id}/`;
            //http://127.0.0.1:8000/api/documents/57/answer/136/answerassessment/70/
            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };

            let vm = this;
            let document_id_local = this.document_id
                axios({
                    method: 'delete',
                    url: endpoint,
                    withCredentials: true,
                    })
                    .then(function (response) {
                        vm.$router.push({name: 'document', params: {document_id: document_id_local}})
                    })
                    .catch(function (response) {
                        vm.$router.push({name: 'document', params: {document_id: document_id_local }})
                    });

        },
        getAnswerAssessment(){
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/answerassessment/${this.answerAssessment_id}/`;
            //http://127.0.0.1:8000/api/documents/57/answer/136/answerassessment/70/
            console.log(endpoint)

            let vm = this;
            axios({
                method: 'get',
                url: endpoint,
                })
                .then(function (response) {
                    console.log(response)
                    vm.answerAssessment= response.data;
                })
                .catch(function (response) {
                    console.log(response)
                });
        }
    },
    created(){
        this.getAnswerAssessment();
    }
}
</script>