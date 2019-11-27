<template>
    <div class="single-answer">
        <p class="text-muted">
            <strong>{{ documentAssessment.author }} </strong> &#8901; {{ documentAssessment.created_at }}
        </p>
        <p>Liczba punktów dla dokumentu: {{ documentAssessment.scores }}</p>
        <p>Opis dokumentu: {{ documentAssessment.note }}</p>
        
        <div v-if="isAnswerAuthor" >
            <router-link 
                :to="{ name: 'document-assessment-editor', params: {documentAssessment_id: documentAssessment.id, document_id: document_id }}" 
                class="btn btn-sm btn-warning"
                >Edytuj
            </router-link>
            <button  type="submit" class="btn btn-sm btn-danger">Usuń</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "DocumentAssessment",
    props: {
        documentAssessment: {
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
            return this.documentAssessment.author === window.localStorage.getItem("username");
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