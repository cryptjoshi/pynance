
import React from "react";
import withStyles from "isomorphic-style-loader/withStyles";
import s from './footer.css'
class Footer extends React.Component {
    render(){
    return (
        <h1>Footer</h1>
    )
    }
}

export default withStyles(s)(Footer)