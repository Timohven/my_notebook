<template>
    <div class="v-calendar">
        <h3>My calendar
            <span>
                <i 
                    class="material-icons"
                    @click="add"
                >
                    edit_calendar
                </i>
            </span>        
        </h3>
        <div class="v-calendar__list">
            <v-note 
                v-for="note in NOTES" 
                :key="note.id"
                v-bind:note_data="note"
            />            
        </div>
    </div>
</template>

<script>
import vNote from './v-note.vue';
import {mapActions, mapGetters} from 'vuex';

export default {
    name: "v-calendar",
    components: {
        vNote
    },
    props: {},
    data() {
        return {}
    },
    computed: {
        ...mapGetters([
            'NOTES'
        ]),
    },
    methods: {
        ...mapActions([
            'GET_NOTES_FROM_API',
        ]),
    },
    watch: {},
    mounted() {
        this.GET_NOTES_FROM_API();
    }
}
</script>

<style lang="scss">
    .v-calendar {
        &__list {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }
    }
</style>