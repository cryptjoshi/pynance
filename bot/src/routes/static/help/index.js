import React from "react";
import Layout from "../../../components/Layout/Layout";
import Page from "../../../components/Page";
import fetch from "../../../core/fetch"

export default {
    path: '/help',
    async action({locale}){
        return {
            title: "Help",
            description: "Help you to get started",
            chunk: 'help',
            component: <Layout><Page html={"<h1>Help</h1>"} title={"Help"}></Page></Layout>
        }
    }
}