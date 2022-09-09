// import React,{Component} from "react";
// import PropTypes from 'prop-types'
// import {connect} from 'react-redux'

// import {Field,reduxForm} from 'redux-form'
// import validate from './validate';
// import submit from './submit'
import withStyles from "isomorphic-style-loader/withStyles";
import cx from 'classnames'
import s from './Login.css'
import {
    Button,
    FormGroup,
    Col,
    FormControl,
    Checkbox,
    Image
} from 'react-bootstrap'
 

// class LoginForm extends Component {
//     static propTypes ={ 

//     }

//     renderFormControl = ({input,label,type,meta:{touched,error},className}) => {
//         return (
//             <div className={'inputFocusColor'}>
//                 <FormControl {...input} placeholder={label} type={type} className={className} />
//                 {touched && error && <span className={s.errorMessage}>{error}</span>}
//             </div>
//         )
//     }
//     render(){
//         const {error,handleSubmit,submitting,dispatch} = this.props
        
//         return (
//             <form onSubmit={handleSubmit(submit)}>
//                  {error && <span className={s.errorMessage}>{error}</span>}
//                 <FormGroup className={s.formGroup}>
//                  <Field
//                     name="email"
//                     type="text"
//                     component={this.renderFormControl}
//                     label={messages.email}
//                     className={cx(s.formControlInput, s.backgroundOne)}
//                 />
                
//                 </FormGroup>

//                 <FormGroup className={s.formGroup}>
//                 <Field
//                     name="password"
//                     type="password"
//                     component={this.renderFormControl}
//                     label={messages.password}
//                     className={cx(s.formControlInput, s.backgroundTwo)}
//                 />
//                 </FormGroup>
                
//                 <FormGroup className={s.formGroup}>
//                 <Button className={cx(s.button, s.btnPrimary)} bsSize="large" block type="submit" disabled={submitting}>
//                     {messages.login}
//                 </Button>
//                 </FormGroup>
//                 <FormGroup className={cx(s.formGroup, s.formSection)}>
//                 <Col xs={12} sm={12} md={12} lg={12} className={cx(s.noPadding, s.textAlignCenter)}>

//                 </Col>
//                 </FormGroup>
//             </form>
//         )
//     }
// }

// LoginForm = reduxForm({
//     form: 'LoginForm',
//     validate,
//     destroyOnUnmount: false
// })(LoginForm)

// const mapState = state =>({})
// const mapDispatch = {
    
// }

// export default withStyles(s)(connect(mapState,mapDispatch)(LoginForm))
const LoginForm = () => {
    
    return (
     <div className={s.title}>
     <h1>Login Components</h1>
     <p>-----------------</p>
     <p>Hello BrowserSync</p>
     <p>-----------------</p>
     <button onClick={()=>alert('clicked')}>Clicked</button>



     </div>   
    )
}
export default  (withStyles(s)(LoginForm));