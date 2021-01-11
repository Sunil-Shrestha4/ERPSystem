import React from 'react';
import { Route, Redirect } from "react-router-dom";
import Auth from "../component/auth"



const GuardedRoute = ({ component: Component, auth, ...rest }) => (
    <Route {...rest} render={ (props) => {
        if (Auth.isAuthenticated()) {
            return <Component {...props} />;
        }
        else{
            
            return <Redirect to='/' />}
            
    }} />
)
export default GuardedRoute;



