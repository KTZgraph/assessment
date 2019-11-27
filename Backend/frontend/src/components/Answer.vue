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
            type: Number,
            required: true
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