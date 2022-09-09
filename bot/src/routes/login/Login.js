import React from "react";
import PropTypes from 'prop-types'
//import {FormattedMessage, injectIntl} from 'react-intl'

import withStyles from "isomorphic-style-loader/withStyles";
import s from './Login.css'
import cx from 'classnames'
import {
    Button,
    Col
} from 'react-bootstrap'

import LoginForm from '../../components/LoginForm'
// import SocialLogin from '../../components/socialLogin'
// import Link from  '../../components/Link'

// import messages from '../../locale/messages'

class Login extends React.Component {
    static propTypes = {
        title: PropTypes.string.isRequired,
        warning: PropTypes.bool,
        refer: PropTypes.string
    }
    static defaultProps = {
        warning: false
    }
    render(){
        const {warning,refer} = this.props
        let initialValues = {}
        let socialLoginRefer
        let registerURL = '/register'
        if(refer){
            initialValues= {
                refer
            }
            socialLoginRefer = refer
            if(socialLoginRefer && socialLoginRefer != null){
                socialLoginRefer = socialLoginRefer.indexOf('?') >= 0 ? socialLoginRefer.replace('?', '---') : socialLoginRefer;
                socialLoginRefer = socialLoginRefer.indexOf('&') >= 0 ? socialLoginRefer.replace('&', '--') : socialLoginRefer;
            }
            registerURL = '/register?refer' + refer
        }
        return(
            <div className={s.root}>
                <div className={s.container}>
                {
                    warning && <div>{ warning }</div>
                }
                <h1>{this.props.title}</h1>
                <LoginForm initialValues={initialValues} />
                </div>
            </div>
        )
    }
}

export default withStyles(s)(Login)