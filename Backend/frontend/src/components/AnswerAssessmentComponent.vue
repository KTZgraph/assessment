<template>
    <div id="answer-assessment-component">
        <p class="text-muted">
            <strong>{{ answerAssessment.author }} </strong> &#8901; {{ answerAssessment.created_at }}
        </p>
        <p>Przynznana liczba punktów: {{ answerAssessment.scores }}</p>
        <p>Notatka: {{ answerAssessment.note }}</p>

        <div v-if="isAnswerAuthor" >
            <router-link 
                :to="{ name: 'answer-assessment-editor', params: {answer_id:answer_id, answerAssessment_id: answerAssessment.id, document_id: document_id }}" 
                class="btn btn-sm btn-warning"
                >Edytuj
            </router-link>
            <router-link 
                :to="{ name: 'answer-assessment-delete', params: {answer_id:answer_id, answerAssessment_id: answerAssessment.id, document_id: document_id }}" 
                class="btn btn-sm btn-danger"
                >Usuń
            </router-link>
        </div>

    </div>
</template>

<script>
export default {
    name: "AnswerAssessmentComponent",
    props:{
        answerAssessment: {
            type: Object,
            required: true
        },
        document_id: {
            type: Number | String,
            required: true
        },
        answer_id: {
            type: Number | String,
            required: true
        }
    },
    computed:{
        isAnswerAuthor(){
            return this.answerAssessment.author === window.localStorage.getItem("username");
        }
    },
    created(){
        console.log("answerAssessment: ", this.answerAssessment)
    }
}
</script>

<style scoped>

</style>
