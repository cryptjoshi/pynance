import { createStore, applyMiddleware, compose } from 'redux';
import thunkMiddleware  from 'redux-thunk';
import createRootReducer from '../reducers'
export default function configuresStore(state,config){
const {apolloClient} = config
const middleware = [
    thunkMiddleware ,
    //apolloClient
  ];
  
  let enhancer;

  if (__DEV__) {
    //middleware.push(createLogger());

    // https://github.com/zalmoxisus/redux-devtools-extension#redux-devtools-extension
    let devToolsExtension = f => f;
    if (process.env.BROWSER && window.devToolsExtension) {
      devToolsExtension = window.devToolsExtension();
    }

    enhancer = compose(
      applyMiddleware(...middleware),
      devToolsExtension,
    );
  } else {
    enhancer = applyMiddleware(...middleware);
  }

  const store =  createStore(createRootReducer(apolloClient),state,enhancer)

  if (__DEV__ && module.hot) {
    module.hot.accept('../reducers', () =>
      // Don't forget to remove `()` if you change reducers back to normal rootReducer.
      // eslint-disable-next-line global-require            // eslint-disable-next-line global-require
      store.replaceReducer(require('../reducers').default({ apolloClient })),
    );
  }
  return store
} 