<template>
    <div class="answer-creator">
        <ImageCropper :imageSrc="src" />
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";

import ImageCropper from  '@/components/ImageCropper.vue';
export default {
    name: "AnswerCreator",
    data(){
        return{
            document: null,
            src: "http://127.0.0.1:8000/media/documents/kotek4_i8cc1o4.jpg"
        }
    },
    props: {
        document_id: {
            type: Number,
            required: true
        }
    },
    components:{
        ImageCropper
    },
    methods:{
        getDocumentData() {
            let endpoint = `/api/documents/${this.document_id}/`;
            console.log("endpoint: ", endpoint);
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.document = response.data;
                        console.log("this.document: ", this.document.document_file);
                        this.src = this.document.document_file;
                        this.setPageTitle(response.data.slug);
                    }else{
                        this.document = null;
                        this.setPageTitle("404 - Page Not Found");
                }
            })
        },
        setPageTitle(title){
            document.title = title;
        }
    },
    created(){
        this.getDocumentData();
    }
}
</script>

<style>

</style>