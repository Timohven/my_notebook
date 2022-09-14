<template>
    <div class="v-main-wrapper">
        <!-- <router-link to="/editor/1"></router-link> -->
        <!-- <keep-alive> -->
            <router-view></router-view>
        <!-- </keep-alive> -->
        
        <!-- <p>{{title}}</p>
        <vMenu v-if="STATUS===0" />
        <vEditor v-if="STATUS===1" /> -->
    </div>
</template>

<script>
// import vMenu from './v-menu.vue';
// import vEditor from './v-editor.vue';
import {mapGetters} from 'vuex';
    
export default {
    name: "v-main-wrapper",
    components: {
        // vMenu,
        // vEditor
    },
    props: {},
    data() {
        return {}
    },
    computed: {
        ...mapGetters([
            'STATUS'
        ])
    },
    methods: {},
    watch: {},
    mounted() {}
}
</script>

<style>
    .v-main-wrapper {
        /* max-width: 900px; */
        margin: 0 auto;
    }
</style>