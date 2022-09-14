<template>  
    <div class="v-notebook">
        <h3>My notebook
        <!-- <router-link :to="{name: 'editor', params: {ar_index: -1}}"> -->
        <router-link :to="{name: 'editor'}">
            <span>
                <i 
                    class="material-icons"
                    @click="add_note()"
                >
                    note_add
                </i>
            </span>        
        </router-link>
        My calendar
            <span>
                <i 
                    class="material-icons"
                    @click="add_note"
                >
                    edit_calendar
                </i>
            </span>        
        </h3>
        <div class="v-notebook__list">
            <v-note 
                v-for="(note, index) in NOTES" 
                :key="note.id"
                v-bind:note_data="note"
                v-bind:ind="index"
                @toEdittingNote="toEdittingNote(note)"
            />            
        </div>
    </div>
</template>

<script>
import vNote from './v-note.vue';
import {mapActions, mapGetters} from 'vuex';

export default {
    name: "v-notebook",
    components: {
        vNote
    },
    props: {},
    data() {
        return {}
    },
    computed: {
        ...mapGetters([
            'NOTES',
            'ACTIVE_NOTE'
        ]),
    },
    methods: {
        ...mapActions([
            'GET_NOTES_FROM_API',
            'EDIT_NOTE'
        ]),
        add_note () {
            console.log('Add new note');
            this.EDIT_NOTE(-1);
        },
        toEdittingNote(note) {
            this.$router.push({
                name: 'editor',
                query: { 'note_id': note.note_id}
            })
        }
    },
    watch: {},
    mounted() {
        this.GET_NOTES_FROM_API();
    }
}
</script>

<style lang="scss">
    .v-notebook {
        &__list {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }
    }
</style>