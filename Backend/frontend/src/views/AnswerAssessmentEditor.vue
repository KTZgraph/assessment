
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Edytuj swoja ocenę dla pojedynczego zadania</h1>
        <form @submit.prevent="updateAnswerAssessment">
            <div>
             <p>Nowa liczba punktów: <input v-model.number="scores" type="number"></p>
            </div>
            <textarea
                v-model="newAssessmentDescriptionBody"
                class="form-control"
                rows="3"
                placeholder="Nowa zmienionana notatka"
            ></textarea>
            <br>
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
            answerAssessment:null //do aktualizacji nie pobieram obiektu
        }
    },
    methods:{        
        updateAnswerAssessment(){
            //usuwanie opinie o calycm dokumencie
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/answerassessment/${this.answerAssessment_id}/`;
            //http://127.0.0.1:8000/api/documents/57/answer/136/answerassessment/70/
            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };
            let formData = new FormData();

            if (this.newAssessmentDescriptionBody){
                //notatka może być pusta
                formData.set("note",this.newAssessmentDescriptionBody)
            }
            if (this.scores){
                // punkty nie mogą być puste!
                formData.set("scores",this.scores)
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
                        vm.$router.push({name: 'document', params: {document_id: document_id_local}})
                    })
                    .catch(function (response) {
                        vm.$router.push({name: 'document', params: {document_id: document_id_local }})
                    });
            }

        }
    }
}
</script>