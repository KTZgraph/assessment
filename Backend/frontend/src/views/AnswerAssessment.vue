<template>
    <div id="new-answer-assessment">
        <h1>ANSWER ASSESSMNET</h1>
        {{ answer }}
        
    </div>
</template>

<script>
import axios from 'axios';

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
            answer: {}
        }
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
        }
    },
    created(){
        console.log("ANSWER ID : ", this.answer_id);
        this.getAnswer();
    }
}
</script>

<style scoped>

</style>