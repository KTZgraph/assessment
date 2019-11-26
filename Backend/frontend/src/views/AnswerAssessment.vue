<template>
    <div id="new-answer-assessment">
        <h1>ANSWER ASSESSMNET</h1>
            {{answer}}    
        <div class="answer-data">
            <p class="text-muted">
                <strong>{{ answer.author }} </strong> &#8901; {{ answer.created_at }}
            </p>
            <p>Maksymalna liczba punktów: {{ answer.max_score }}</p>
        </div>
        <p>Plik: {{ answer.answer_file }}</p>
        <div class="img-answer">
            <a v-bind:href="answer.answer_file">
                <b-img class="img-full" v-bind:src="answer.answer_file" fluid-grow alt="Fluid image"></b-img>
            </a>
        </div>
        
        <!-- Wyświetlanie ocen odpowiedzi -->
        <div class="container">
            <AnswerAssessmentComponent 
                v-for="(answerAssessment, index) in answerAssessments"
                :answerAssessment="answerAssessment"
                :v-key="index"
            />
        </div>

    </div>
</template>

<script>
import axios from 'axios';

import AnswerAssessmentComponent from '@/components/AnswerAssessmentComponent.vue'

export default {
    name: "AnswerAssessment",
    props: {
        answer_id: {
            type: Number,
            required: true
        },
        document_id: {
          type: String,
          required: true
        }
    },
    data(){
        return{
            answer: {},
            answerAssessments: []
        }
    },
    components: {
        AnswerAssessmentComponent
    },
    methods:{
        getAnswer(){
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/`;
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.answer = response.data;
                        console.log(response);
                        console.log(typeof this.answer);
                    }else{
                        this.answer = null;
                        // this.setPageTitle("404 - Page Not Found");
                }
            })
        },
        
        getAnswerAssessments(){
            let endpoint = `/api/documents/${this.document_id}/answer/${this.answer_id}/answerassessments/`;
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.answerAssessments.push(...response.data);
                        console.log(response);
                    }else{
                         this.answerAssessments = []
                    }
            })
        }
    },
    created(){
        console.log("ANSWER ID : ", this.answer_id);
        this.getAnswer();
        this.getAnswerAssessments();
    }
}
</script>

<style scoped>
.img-answer{
    max-width: 400px;
    height: auto;
}
</style>