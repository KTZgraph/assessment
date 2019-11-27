
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Usuń permamentinie cały dokument i wszystkie powiazane dane</h1>

            <div class="document-image">
                <a v-bind:href="document.document_file">
                    <b-img class="img-full" v-bind:src="document.document_file" fluid-grow alt="Fluid image"></b-img>
                </a>
            </div>

            <p class="mb-0">
                Utworzono: <span class="author-name">{{ document.created_at }}</span>
            </p>
            <p class="mb-0">
                Dokument dodany przez: <span class="author-name">{{ document.author }}</span>
            </p>
            <p class="mb-0">
                Kod dokumentu: <span class="author-name">{{ document.document_code }}</span>
            </p>   
            <button
                @click="deleteDocument"
                type="submit"
                class="btn btn-danger"
            >Usuń cały dokument i wszystkie powiązane dane
            </button>

        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "DocumentDelete",
    props: {
        document_id: {
            type: Number | String,
            required: true
        }
    },
    data(){
        return{
            error: null,
            document: null
        }
    },
    methods:{
        deleteDocument(){
            //usuwanie opinie o calycm dokumencie
            let endpoint = `/api/document/${this.document_id}/`;

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
                    vm.$router.push({name: 'home'}) //po usunieciu lecimy na glowna
                })
                .catch(function (response) {
                    console.log(response)
                });
        },
        
        getDocument(){
            let endpoint = `/api/documents/${this.document_id}/`;
            let vm = this;
            axios({
                method: 'get',
                url: endpoint,
                })
                .then(function (response) {
                    vm.document= response.data;
                })
                .catch(function (response) {
                });
        }
    },
    created(){
        this.getDocument();
    }
}
</script>

<style scoped>
.img-answer{
    max-width: 600px;
    height: auto;
}
</style>