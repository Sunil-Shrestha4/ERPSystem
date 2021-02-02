import React from 'react';
import { Route, Redirect } from "react-router-dom";
import Auth from "../component/auth";
import Cookies from "js-cookie";



const GuardedRoute = ({ component: Component ,auth=true, redirectTo=null, ...rest }) => (
    <Route {...rest} render={ (props) => {
        
        // const additional = additionalCondition === null ? true : additionalCondition
       
        if ((Auth.isAuthenticated() || Cookies.get('auth')=="loginTrue") && auth) {
            // console.log("here")
            
            return <Component {...props} />;
        }
        else{
            if(redirectTo){
                console.log('ma yeta xu');
                return <Redirect to={redirectTo} />
                
            }else{
                return <Redirect to='/' />}
            }
            
    }} />
)
export default GuardedRoute;



