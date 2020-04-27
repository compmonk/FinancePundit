import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import Modal from 'react-modal';

export class UserModal extends Component {
    render() {
        return (
            <div className="container">
            <div className="btn-toolbar">
                <button className="btn btn-primary">New User</button>
                <button className="btn">Import</button>
                <button className="btn">Export</button>
            </div>
            </div>
        )
    }
}

export default UserModal