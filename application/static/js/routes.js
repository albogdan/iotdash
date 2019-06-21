import React from 'react';
import { HashRouter, Route, hashHistory } from 'react-router-dom';
import Home from './components/Home';
import Dash from './components/Dash';
// import more components
export default (
    <HashRouter history={hashHistory}>
     <div>
      <Route path='/' component={Home} />
      <Route path='/dash' component={Dash} />
     </div>
    </HashRouter>
);
