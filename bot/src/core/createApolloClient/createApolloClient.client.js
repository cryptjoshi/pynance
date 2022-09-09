import { ApolloClient,HttpLink,InMemoryCache } from "@apollo/client";
import fetch from "cross-fetch";


const client = new ApolloClient({
    link: new HttpLink({ uri: '/graphql', fetch }),
    cache: new InMemoryCache(),
  // queryDeduplication:true,
  // reduxRoots: state=>state.apollo
  
  });


export default function createApolloClient(){
    return client
}