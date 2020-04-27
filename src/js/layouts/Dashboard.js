import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';

import Header from "../components/Header";
import UserModal from "../components/UserModal";

class Dashboard extends Component {
    render() {
        return (
            <Fragment>
                <Header/>
                <UserModal/>
            </Fragment>
        )
    }
}

ReactDOM.render(<Dashboard/>, document.getElementById('dashboard'));