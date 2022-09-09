import { combineReducers } from 'redux';

import user from './User'

export default function createRootReducer({ apolloClient }) {
    return combineReducers({
        //apollo: apolloClient.reducer(),
        //loadingBar: loadingBarReducer,
        user,
    })
}