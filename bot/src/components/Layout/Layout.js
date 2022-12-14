import React from "react";
import PropTypes from 'prop-types'
import withStyles from "isomorphic-style-loader/withStyles";
import s from './Layout.css'

import cx from 'classnames'

class Layout extends React.Component {
    static propTypes = {
        children: PropTypes.node.isRequired,
    }
    render() {
        return (
            <div>
                {this.props.children}
                <div className={cx('hidden-xs hidden-sm')}>
                    <h1>Footer</h1>
                </div>
            </div>
        )
    }
}

export default withStyles(s)(Layout)