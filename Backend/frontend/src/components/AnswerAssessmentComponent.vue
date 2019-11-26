<template>
    <div id="answer-assessment-component">
        <p class="text-muted">
            <strong>{{ answerAssessment.author }} </strong> &#8901; {{ answerAssessment.created_at }}
        </p>
        <p>Przynznana liczba punktów: {{ answerAssessment.scores }}</p>
        <p>Notatka: {{ answerAssessment.note }}</p>
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
    }
}
</script>

<style scoped>

</style>
