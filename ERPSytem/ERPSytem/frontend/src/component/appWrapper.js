import { Redirect } from 'react-router-dom'
import React, { Component } from 'react';
import Cookies from "js-cookie";
import Profile from '../containers/Profile';
import {Route} from 'react-router-dom'
import Login from '../containers/Login';


class AppWrapper extends Component{
  render(){

  if(Cookies.get('auth')!="loginTrue")
    return (<div>
      <Route path='/' component={Login} />
    </div>);
  

   return(
     <div>
       <Redirect to='/profile' />
       {/* <Route path='/' component={Profile} /> */}
     </div>
   );
  }
} export default AppWrapper;