import React from "react"
import s from './home.css'
import {flowRight as compose} from 'lodash';
import useStyles from 'isomorphic-style-loader/useStyles'
import withStyles from 'isomorphic-style-loader/withStyles'
import cx from 'classnames'
const Home = () => {
    
    return (
     <div className={s.title}>
     <h1>Home Components</h1>
     <p>-----------------</p>
     <p>Hello BrowserSync</p>
     <p>-----------------</p>
     <button onClick={()=>alert('clicked')}>Clicked</button>



     </div>   
    )
}
export default  (withStyles(s)(Home));