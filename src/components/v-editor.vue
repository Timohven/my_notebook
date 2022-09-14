<template>
    <div class="v-editor">
        <template v-if="ACTIVE_NOTE.note_id==-1">
            <p>Creation of the new note ID:{{NOTES.length+1}}</p>
        </template>
        <template v-else>
            <p>Editing of the note ID:{{ACTIVE_NOTE.note_id}}</p>
        </template>
        <p>Title of note :{{ACTIVE_NOTE.title}}</p>
        <p>Category of note :{{ACTIVE_NOTE.category}}</p>
        <p><textarea class="v-editor__textarea" v-model="ACTIVE_NOTE.content" placeholder="Content"></textarea></p>
        
        <router-link :to="{name: 'notebook'}">
            <button @click="save">Save</button>
        </router-link>
        <router-link :to="{name: 'notebook'}">
            <button @click="cancel">Cancel</button>
        </router-link>
    </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex';


export default {
    name: "v-editor",
    components: {},
    props: {
        ar_index: {
            type: Number,
            default () {
                return 0
            }
        },        
        id: {
            type: Number,
            default () {
                return 0
            }
        }
        // active_note: {
        //     type: Object,
        //     default () {
        //         return {}
        //     }
        // }
    },
    data() {
        return {
            // active_note: {
            //     type: Object,
            //     default () {
            //         return {}
            //     }
            // }
        }
    },
    computed: {
        ...mapGetters([
            'ACTIVE_NOTE',
            'NOTES'
        ])        
    },
    methods: {
        ...mapActions([
            'SAVE_NOTE',
            'CANCEL'
        ]),
        save() {
            console.log("Save note");
            this.SAVE_NOTE();
        },
        cancel() {
            console.log('Cancel');
            this.CANCEL();  
        }
    },
    watch: {},
    mounted() {
        //this.cur_con = this.NOTES[ar_index].content
        }
}
</script>

<style lang="scss">
    .v-editor {
        flex-basis: 25%;
        box-shadow: 0 0 8px 0 #e0e0e0;
        padding: 16px;
        margin-bottom: 16px;
    }
    .v-editor__textarea {
        padding-left: 0px;
        padding-bottom: 100px;
        width: 100%;
        justify-content: center;
        align-items: center;
    }
    
</style>