<template>
    <div class="single-answer">

        <p class="text-muted">
            <strong>{{ answer.author }} </strong> &#8901; {{ answer.created_at }}
        </p>
        <p>Maksymalna liczba punktów: {{ answer.max_score }}</p>
        <p>Plik: {{ answer.answer_file }}</p>
        <div class="img-answer">
            <a v-bind:href="answer.answer_file">
                <b-img class="img-full" v-bind:src="answer.answer_file" fluid-grow alt="Fluid image"></b-img>
            </a>
        </div>

        <!-- EDYCJA CAŁEGO ZADNAIA A NIE JEGO OPINII !!!!!!!!!!!!!  -->
        <!-- <div v-if="isAnswerAuthor" >
            <router-link 
                :to="{ name: 'answer-assessment-editor', params: {answer_id:answer.id, answerAssessment_id: answerAssessment_id, document_id: document_id }}" 
                class="btn btn-sm btn-warning"
                >Edytuj
            </router-link>
            <router-link 
                :to="{ name: 'answer-assessment-delete', params: {answer_id:answer.id, answerAssessment_id: answerAssessment_id, document_id: document_id }}" 
                class="btn btn-sm btn-danger"
                >Usuń
            </router-link>
        </div> -->

        <div class="card-footer px-3">
            <router-link 
                :to="{ name: 'answer-assessment', params: {document_id: document_id, answer_id: answer.id }}" 
                class="btn btn-sm btn-success"
                >Oceń zadanie
            </router-link>
        </div>

    </div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        document_id: {
            type: Number | String,
            required: true
        }
    },
    computed:{
        isAnswerAuthor(){
            return this.answer.author === window.localStorage.getItem("username");
        }
    }
}
</script>

<style scoped>
.img-answer{
    max-width: 100px;
    height: auto;
}
</style>