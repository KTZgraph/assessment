
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Usuń permamentinie swoja ocenę dla dokumentu</h1>
        
        <p class="text-muted">
            <strong>{{ documentAssessment.author }} </strong> &#8901; {{ documentAssessment.created_at }}
        </p>
        <p>Liczba punktów dla dokumentu: {{ documentAssessment.scores }}</p>
        <p>Opis dokumentu: {{ documentAssessment.note }}</p>
    
            <button
                @click="deleteDocumentAssessment"
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
    name: "DocumentAssessmentEditor",
    props: {
        documentAssessment_id: {
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
            newDocumentDescriptionBody: null,
            documentAssessment: null
        }
    },
    methods:{
        deleteDocumentAssessment(){
            //usuwanie opinie o calycm dokumencie
            let endpoint = `/api/documents/${this.document_id}/documentassessment/${this.documentAssessment_id}/`;
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
        
        getDocumentAssessmnet(){
            let endpoint = `/api/documents/${this.document_id}/documentassessment/${this.documentAssessment_id}/`;

            let vm = this;
            axios({
                method: 'get',
                url: endpoint,
                })
                .then(function (response) {
                    vm.documentAssessment= response.data;
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