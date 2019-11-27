
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Edytuj swoje zadanie</h1>

        <form @submit.prevent="updateAnswer">
            <div>
             <p>Maksymalna liczba punktów: <input v-model.number="scores" type="number"></p>
            </div>
            <button
                type="submit"
                class="btn btn-success"
            >Zauktualizuj</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "AnswerEditor",
    props: {
        document_id: {
            type: Number | String,
            required: true
        },
        answer_id: {
            type: Number | String,
            required: true
        }
    },
    data(){
        return{
            error: null,
            scores: null,
        }
    },
    methods:{        
        updateAnswer(){
            //usuwanie opinie o calycm dokumencie
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/`;
            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };
            let formData = new FormData();

            if (this.scores){
                // punkty nie mogą być puste!
                formData.set("max_score",this.scores)
            }

            let vm = this;
            let document_id_local = this.document_id
            if (formData){
                axios({
                    method: 'put',
                    url: endpoint,
                    withCredentials: true,
                    data: formData,
                    })
                    .then(function (response) {
                        console.log(response)
                        vm.$router.push({name: 'document', params: {document_id: document_id_local}})
                    })
                    .catch(function (response) {
                        console.log(response)
                    });
            }

        }
    }
}
</script>