<template>
    <div id="new-document">
    <h1>Tworzenie nowego dokumentu - drag and drop</h1>
    
    <form>
        <!-- upload jednego pliku -->
        <div class="dropzone">
            <input 
                type="file"
                class="input-file"
                ref="file"
                @change="sendFile"
            />
            <p v-if="!uploading" class="call-to-action">
                Dodaj plik przez upuszczenie go tutaj
            </p>
            <p v-if="uploading" class="progess-bar">
                <progress
                    class="progress is-primary"
                    :value="progress"
                    max="100"
                >
                    {{progress}} %
                </progress>
            </p>
        </div>

        <!--  -->
        <div class="content">
        <ul>
            <li v-for="file in uploadedFiles" :key="file.id" >
                <a v-bind:href="file.document_file">{{file.document_file}}</a>
                <router-link :to="{ name: 'document', params: {document_id: file.id } }" class="btn btn-sm btn-success">Przejdź do edycji</router-link>
            </li>
        </ul>
        </div>

    </form>
    
    </div>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js";
export default {
    name: "NewDocument",
    data(){
        return{
            file: "",
            message: "",
            error: false,
            uploading: false,
            newDocumentId: null,
            uploadedFiles: [],
            progress: 0
        }
    },
    methods: {
        async sendFile(){
            let endpoint = `/api/documents/`;
            
            const file = this.$refs.file.files[0];
            const formDataNewDocument = new FormData();
            formDataNewDocument.append("document_file", file);

            axios.defaults.headers.common = {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': CSRF_TOKEN
            };

            this.uploading = true;
            let vm = this;
            const rest = await axios({
                method: 'post',
                url: endpoint,
                withCredentials: true,
                data: formDataNewDocument,
                onUploadProgress: e => vm.progress = Math.round(e.loaded * 100 / e.total)
                })
                .then(function (response) {
                    vm.uploadedFiles.push(response.data);
                    vm.newDocumentId = response.data.id;
                    vm.uploading = false;
                })
                .catch(function (response) {
                    console.log("Error: ", response)
                    vm.uploading = false;
                });

        }
    }
}
</script>

<style scoped>
.dropzone{
    min-height: 200px;
    padding: 10 px 10 px;
    position: relative;
    cursor: pointer; /* łpka jak najedzie sie na pole */
    outline: 2px dashed grey;
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
}

.input-file{
    opacity: 0; /*nie widoczne ALE DALEJ aktywne */
    width: 100%;
    height: 200px;
    position: absolute;
    cursor: pointer;

}

.dropzone:hover{
    /* cssowa sztuczka - użytkownik widiz zmaine koloru po najechaniu*/
    background: lightblue;    
}

.dropzone .call-to-action {
    font-size: 1.2rem;
    text-align: center;
    padding: 70px 0;
}

.dropzone .progess-bar{
    text-align: center;
    padding: 70px 10px;
}
</style>