<template>
    <div class="answer-creator">
        <div v-if="imageSrc">
            <ImageCropper 
                :imageSrc="imageSrc" 
                :document_id="document_id"
            />
        </div>
        <div v-else>
            <p> Nie można wczytać obraz</p>
        </div>
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
            imageSrc: null,
            requestUser: null
        }
    },
    props: {
        document_id: {
            type: String | Number,
            required: true
        }
    },
    components:{
        ImageCropper
    },
    methods:{
        getDocumentData() {
            let endpoint = `/api/documents/${this.document_id}/`;
            axios.get(endpoint)
                .then(response => {
                    if(response){
                        this.document = response.data;
                        this.imageSrc = this.document.document_file;
                        this.setPageTitle(response.data.slug);
                    }else{
                        this.document = null;
                        this.setPageTitle("404 - Page Not Found");
                }
            })
        },
        setPageTitle(title){
            document.title = title;
        },
        setRequestUser(){
        // data for logged user
        this.requestUser = window.localStorage.getItem("username"); //data form loac storage
        }
    },
    created(){
        this.getDocumentData();
        this.setRequestUser();
    }
}
</script>

<style>

</style>