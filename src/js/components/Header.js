import React, {Component} from 'react';

export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <button className="navbar-toggler" type="button" data-toggle="collapse"
                        data-target="#nav-bar" aria-controls="nav-bar" aria-expanded="false"
                        aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <a className="navbar-brand" href="#">Finance Pundit</a>
                <div className="collapse navbar-collapse" id="nav-bar">
                    <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                        <li className="nav-item active">
                            <a className="nav-link" href="/user/">Profile <span className="sr-only">(current)</span></a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="/auth/logout">Logout</a>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }
}

export default Header