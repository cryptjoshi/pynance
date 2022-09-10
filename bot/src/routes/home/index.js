import React from "react"
import Home from  '../../components/Home'
import Layout from "../../components/Layout/Layout"
export default {
    path: '/',
    async action({store}){
        
        const title = "Home"
        const description = "Home from Routes"
        return {
            title,
            description,
            chunk: 'home',
            component: <Layout><Home /></Layout>
        }
    }
}