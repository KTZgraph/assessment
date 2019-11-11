<template>
    <div class="answer-component">
        <h1>Odpowiedzi</h1>
        <p class="text-muted">
            <strong>{{ answer.author }} </strong> &#8901; {{ answer.created_at }}
        </p>
        <p>Maksymalna liczba punktów: {{ answer.max_score }}</p>
        <p>Przyznane punkty: {{ answer.score }}</p>
        <p>Nota: {{ answer.note }}</p>
        <p>Plik: {{ answer.answer_file }}</p>
    </div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        }
    }
}
</script>