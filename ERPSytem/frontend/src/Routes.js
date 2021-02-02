import React, { useEffect, useState, useContext } from "react";
import {Route, Switch} from "react-router-dom";
// import Home from "./containers/Home";
import Login from "./containers/Login";
import NotFound from "./containers/NotFound";
import Signup from "./containers/Signup";
// import Profile from "./containers/Profile";
import Dashboard from "./admin/Dashboard";
import GuardedRoute from "./component/guardroute";
import User from "./pages/User"
import AddEmployee from "./pages/AddEmployee"
import Attendance from "./pages/Attendance"
<<<<<<< HEAD
import SalaryReport from "./pages/SalaryReportList";
import Userlist from "./pages/Userlist";
import Userdetails from "./pages/details";
import SalaryAdd from "./pages/SalaryAdd";
import SalaryUpdate from './pages/SalaryUpdate';
=======
import SalaryReport from "./pages/SalaryReport";

import appWrapper from "./component/appWrapper"
import OwnAttendance from "./pages/OwnAttendance";
import OwnAttendanceCO from "./pages/OwnAttendanceCO";


import { IsSuperUserContext } from "./context/IsSuperUserContext";


>>>>>>> ujjwal_dev

export default function Routes(){
    const [isSuperUser, setIsSuperUser] = useContext(IsSuperUserContext);

    // useEffect(() => {
    //     setIsSuperUser(localStorage.getItem("is_superuser") == "true")
    // }, [])

    

    
    return(
        <Switch>
            
<<<<<<< HEAD
            <Route exact path="/" component={Login} />
            <Route exact path="/signup">
                <Signup/>
            </Route>
            {/* <Route exact path="/profile">
                <Dashboard/>
            </Route> */}
            {/* <GuardedRoute /> */}
            <GuardedRoute exact path="/dashboard"  component={Dashboard}  />
            <Route exact path="/User">
                <User />
            </Route>
            <Route exact path="/team"><Userlist/></Route>
            <Route exact path="/details/:id" component={Userdetails}/>
            <GuardedRoute exact path="/employee"  component={AddEmployee}  />
            <GuardedRoute exact path="/attendance"  component={Attendance}  />
            <Route exact path="/salaryreport"  component={SalaryReport}  />
            <Route exact path="/salaryAdd"  component={SalaryAdd} />
            <Route exact path="/salaryUpdate/:id" component={SalaryUpdate}/>
=======
            
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
            <GuardedRoute exact path="/owns" auth={!isSuperUser} component = {()=><OwnAttendanceCO/> } redirectTo={"/"} />
>>>>>>> ujjwal_dev
             
            <Route>
                <NotFound/>
            </Route>
        </Switch>
    );
}
