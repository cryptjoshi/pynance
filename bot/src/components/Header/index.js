
import React from "react";
import withStyles from "isomorphic-style-loader/withStyles";
import s from './header.css'
class Header extends React.Component {
    constructor(props) {
        super(props);}
    render(){
    return (
        <div className={s.header}>
        <h1>Header</h1>
        </div>
    )
    }
}

export default withStyles(s)(Header)