import React from "react"
import s from './home.css'
import {flowRight as compose} from 'lodash';
import useStyles from 'isomorphic-style-loader/useStyles'
import withStyles from 'isomorphic-style-loader/withStyles'
import Link from "../Link/Link";
import cx from 'classnames'
const Home = () => {
    
    return (
     <div className={s.title}>
     <h1>Home Components</h1>
     <p>-----------------</p>
     <p>Hello BrowserSync</p>
     <p>-----------------</p>
     <Link to={"/login"}>Login</Link>



     </div>   
    )
}
export default  (withStyles(s)(Home));