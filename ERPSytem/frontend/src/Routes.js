import React, { useEffect, useState, useContext } from "react";
import {Route, Switch} from "react-router-dom";
import Home from "./containers/Home";
import Login from "./containers/Login";
import NotFound from "./containers/NotFound";
import Signup from "./containers/Signup";
import Profile from "./containers/Profile";
import Dashboard from "./admin/Dashboard";
import GuardedRoute from "./component/guardroute";
import User from "./pages/User"
import AddEmployee from "./pages/AddEmployee"
import Attendance from "./pages/Attendance"
import SalaryReport from "./pages/SalaryReport";

import appWrapper from "./component/appWrapper"
import OwnAttendance from "./pages/OwnAttendance";
import roleDash from "./component/roleDash";

import { IsSuperUserContext } from "./context/IsSuperUserContext";



export default function Routes(){
    const [isSuperUser, setIsSuperUser] = useContext(IsSuperUserContext);

    // useEffect(() => {
    //     setIsSuperUser(localStorage.getItem("is_superuser") == "true")
    // }, [])

    

    
    return(
        <Switch>
            
            
            <Route exact path="/"  component={appWrapper}  />
            <GuardedRoute exact path="/"  component={SalaryReport}  />
            <Route exact path="/signup">
                <Signup/>
            </Route>
            
            <GuardedRoute exact path="/profile"  component={Dashboard}  />
            
            <GuardedRoute exact path="/user"  component={User}  />
            <GuardedRoute exact path="/employee"  component={AddEmployee}  />
            <GuardedRoute exact path="/attendance" auth={isSuperUser} component={()=><Attendance/>} redirectTo={"/own"} />
            <GuardedRoute exact path="/salary"  component={SalaryReport}  />
            <GuardedRoute exact path="/own" auth={!isSuperUser} component = {()=><OwnAttendance/> } redirectTo={"/"} />
             

            <Route>
                <NotFound/>
            </Route>
        </Switch>
    );
}
