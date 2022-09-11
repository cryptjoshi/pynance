
import React from "react";
import withStyles from "isomorphic-style-loader/withStyles";
import s from './footer.css'
class Footer extends React.Component {
    constructor(props) {
        super(props);}
    render(){
    return (
        <div className={s.footer}>
        <h1>Footer</h1>
        </div>
    )
    }
}

export default withStyles(s)(Footer)