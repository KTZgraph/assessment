<template>
    <div class="single-answer">
        <h1>Pojedyncze zadanie</h1>
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
        <hr>
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
    },
    mounted(){
        console.log(this.answer)
        console.log("MOUNTED ANSWERCOMPONENT")
    }
}
</script>

<style scoped>
.img-answer{
    max-width: 100px;
    height: auto;
}
</style>