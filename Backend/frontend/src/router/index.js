import Vue from "vue";
import VueRouter from "vue-router";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import Home from "@/views/Home.vue";
import ImageCropper from "@/components/ImageCropper.vue";
import Document from "@/views/Document.vue";
import AnswerCreator from "@/views/AnswerCreator.vue"
import NewDocument from "@/views/NewDocument.vue"
import AnswerAssessment from "@/views/AnswerAssessment.vue"
import DocumentAssessmentEditor from "@/views/DocumentAssessmentEditor.vue"
import DocumentAssessmentDelete from "@/views/DocumentAssessmentDelete.vue"
import AnswerAssessmentEditor from "@/views/AnswerAssessmentEditor.vue"
import AnswerAssessmentDelete from "@/views/AnswerAssessmentDelete.vue"
import AnswerEditor from "@/views/AnswerEditor.vue" //aktualizuje TYLKO PUNKTy, nie obraz, bo bedzie syf w danych
import AnswerDelete from "@/views/AnswerDelete.vue"
import DocumentDelete from "../views/DocumentDelete.vue"; // BEZ AKTUALIZACJI DOKUMENTU bo syf w danych
Vue.use(VueRouter);
Vue.use(BootstrapVue);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/document/:document_id",
    name: "document",
    component: Document,
    props: true
  },
  {
    path: "/document/document-delete/:document_id",
    name: "document-delete",
    component: DocumentDelete,
    props: true
  },
  {
    path: "/document/:document_id/answer-editor/:answer_id",
    name: "answer-editor",
    component: AnswerEditor,
    props: true
  },
  {
    path: "/document/:document_id/answer-delete/:answer_id",
    name: "answer-delete",
    component: AnswerDelete,
    props: true
  },

  {
    path: "/document/:document_id/document-assessment-editor/:documentAssessment_id",
    name: "document-assessment-editor",
    component: DocumentAssessmentEditor,
    props: true
  },
  {
    path: "/document/:document_id/document-assessment-delete/:documentAssessment_id",
    name: "document-assessment-delete",
    component: DocumentAssessmentDelete,
    props: true
  },
  {
    path: "/document/:document_id/answer/:answer_id/answer-assessment-editor/:answerAssessment_id",
    name: "answer-assessment-editor",
    component: AnswerAssessmentEditor,
    props: true
  },
  {
    path: "/document/:document_id/answer/:answer_id/answer-assessment-delete/:answerAssessment_id",
    name: "answer-assessment-delete",
    component: AnswerAssessmentDelete,
    props: true
  },
  {
    path: "/new-document",
    name: "new-document",
    component: NewDocument,
    props: false
  },
  {
    path: "/crop",
    name: "image-cropper",
    component: ImageCropper,
    props: true
  },
  {
    path: "/document",
    name: "document-editor",
    component: ImageCropper
  },
  {
    path: "/document/:document_id/answer-assessment/:answer_id",
    name: "answer-assessment",
    component: AnswerAssessment,
    props: true
  },
  {
    path: "/answer-creator/:document_id",
    name: "answer-creator",
    component: AnswerCreator,
    props: true
  }

];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
