import { createWebHistory, createRouter } from 'vue-router'
import vNotebook from '../components/v-notebook'
import vCalendar from '../components/v-calendar'
import vEditor from '../components/v-editor'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'notebook',
            component: vNotebook
        },
        {
            path: '/',
            name: 'calendar',
            component: vCalendar
        },
        {
            path: '/editor',
            name: 'editor',
            component: vEditor,
            //props: true
        }
        // {
        //     path: '/editor/:id',
        //     component: vEditor

        // }
    ]
})


export default router;