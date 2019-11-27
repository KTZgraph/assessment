<template>
    <div id="answer-assessment-component">
        <p class="text-muted">
            <strong>{{ answerAssessment.author }} </strong> &#8901; {{ answerAssessment.created_at }}
        </p>
        <p>Przynznana liczba punktów: {{ answerAssessment.scores }}</p>
        <p>Notatka: {{ answerAssessment.note }}</p>

        <div v-if="isAnswerAuthor">
            <button type="submit" class="btn btn-sm btn-danger">Usuń</button>
            <button type="submit" class="btn btn-sm btn-warning">Edytuj</button>
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
        }
    },
    computed:{
        isAnswerAuthor(){
            return this.answerAssessment.author === window.localStorage.getItem("username");
        }
    }
}
</script>

<style scoped>

</style>
