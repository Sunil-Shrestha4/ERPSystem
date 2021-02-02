import React from 'react'
import { Route, Redirect } from "react-router-dom";

const roleDash = () =>(
    <Route  render={ (props) => {
        if (localStorage.getItem('is_superuser')=="true"){
            return <Redirect to='/attendance'/>
        }
        
        else{
            
            return <Redirect to='/own' />}
        
            
    }} />
    
)
export default roleDash;

