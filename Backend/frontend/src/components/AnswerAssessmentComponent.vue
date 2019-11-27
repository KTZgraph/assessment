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
    methods:{
        deleteAnswerAssessment(){
            let endpoint = `/api/documents/${this.document_id}/documentassessment/`;
            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };

            let vm = this;
            axios({
                method: 'delete',
                url: endpoint,
                withCredentials: true,
                })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (response) {
                    console.log(response);
                });
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
