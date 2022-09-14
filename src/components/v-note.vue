<template>
    <div class="v-note">
        <v-popup
            v-if="IsInfoPopupVisible"
            rightBtnTitle="Edit"
            :popupTitle="note_data.title"
            @closePopup="closeInfoPopup"
            @rightBtnAction="editNote"
        >
            <div>
                <p>ID of note:{{note_data.note_id}}</p>
                <p>Title of note:{{note_data.title}}</p>
                <p>Content of note:{{note_data.content}}</p>
                <p>Date of creation:{{note_data.creation_date}}</p>
            </div>
        </v-popup>
        
        <p>interior number :{{ind}}</p>
        <p>Note ID :{{note_data.note_id}}</p>
        <p>{{note_data.title}}</p>
        <p>{{note_data.content}}</p>
        <button @click="showPopupInfo">Read</button>
        <!-- <router-link :to="{name: 'editor'}"> -->
            <button @click="editNote">Edit</button>
        <!-- </router-link> -->
    </div>
</template>

<script>
import vPopup from './popup/v-popup.vue';
import {mapActions} from 'vuex';
export default {
    name: "v-note",
    components: { vPopup },
    props: {
        note_data: {
            type: Object,
            default() {
                return {}
            }
        },
        ind: {
            type: Number,
            default() {
                return 0
            }
        }
    },
    data() {
        return {
            IsInfoPopupVisible: false
        }
    },
    computed: {},
    methods: {
        ...mapActions([
            'EDIT_NOTE'
        ]),
        showPopupInfo () {
            this.IsInfoPopupVisible = true;
        },
        closeInfoPopup() {
            this.IsInfoPopupVisible = false;
        },
        editNote() {
            console.log('editting note:', this.note_data.note_id);
            this.$emit('toEdittingNote');
            this.EDIT_NOTE(this.ind);
        }
    },
    watch: {},
    mounted() {}
}
</script>

<style lang="scss">
    .v-note {
        flex-basis: 25%;
        box-shadow: 0 0 8px 0 #e0e0e0;
        padding: 16px;
        margin-bottom: 16px;
    }
   
</style>