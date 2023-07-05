import { createRouter, createWebHistory } from 'vue-router'
import theLayout from "@/layout/theLayout";


const routes = [

    {
        path: '/',
        name: 'theLayout',
        component: theLayout,
        redirect:"/theLayout",
        children:[
            {
                path:'1',
                name:'1',
                component:()=>import("@/views/1")
            },
            {
                path:'2',
                name:'2',
                component:()=>import("@/views/2")
            },
            {
                path:'3',
                name:'3',
                component:()=>import("@/views/3")
            },
        ]
    },


]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
