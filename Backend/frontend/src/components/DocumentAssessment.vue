<template>
    <div class="single-answer">
        <p class="text-muted">
            <strong>{{ documentAssessment.author }} </strong> &#8901; {{ documentAssessment.created_at }}
        </p>
        <p>Liczba punktów dla dokumentu: {{ documentAssessment.scores }}</p>
        <p>Opis dokumentu: {{ documentAssessment.note }}</p>
    </div>
</template>

<script>
export default {
    name: "DocumentAssessment",
    props: {
        documentAssessment: {
            type: Object,
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