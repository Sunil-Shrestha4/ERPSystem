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
import SalaryReport from "./pages/SalaryReportList";
import Userlist from "./pages/Userlist";
import Userdetails from "./pages/details";
import SalaryAdd from "./pages/SalaryAdd";
import SalaryUpdate from './pages/SalaryUpdate';
import appWrapper from "./component/appWrapper"
import OwnAttendance from "./pages/OwnAttendance";
import OwnAttendanceCO from "./pages/OwnAttendanceCO";
import Leave from "./pages/leave";
import PostLeave from "./pages/PostLeave";
import ManagerLeave from "./pages/ManagerLeave";
import AdminLeave from "./pages/AdminLeave";
import Myleavehistory from "./pages/Myleavehistory";


import { IsSuperUserContext } from "./context/IsSuperUserContext";



export default function Routes(){
    const [isSuperUser, setIsSuperUser] = useContext(IsSuperUserContext);

    // useEffect(() => {
    //     setIsSuperUser(localStorage.getItem("is_superuser") == "true")
    // }, [])

    

    
    return(
        <Switch>
            <Route exact path="/"  component={appWrapper}  />
            <GuardedRoute exact path="/signup" component={Signup}/>
            {/* <Route exact path="/profile">
                <Dashboard/>
            </Route> */}
            {/* <GuardedRoute /> */}
            <GuardedRoute exact path="/dashboard"  component={Dashboard}  />
            <GuardedRoute exact path="/team" component={Userlist}/>
            <GuardedRoute exact path="/user"  component={User}  />
            <GuardedRoute exact path="/details/:id" component={Userdetails}/>
            <GuardedRoute exact path="/employee"  component={AddEmployee}  />
            <GuardedRoute exact path="/salaryreport"  component={SalaryReport}  />
            <GuardedRoute exact path="/salaryAdd"  component={SalaryAdd} />
            <GuardedRoute exact path="/salaryUpdate/:id" component={SalaryUpdate}/>
            <GuardedRoute exact path="/attendance" auth={isSuperUser} component={()=><Attendance/>} redirectTo={"/own"} />
            <GuardedRoute exact path="/own" auth={!isSuperUser} component = {()=><OwnAttendance/> } redirectTo={"/"} />
            <GuardedRoute exact path="/owns" auth={!isSuperUser} component = {()=><OwnAttendanceCO/> } redirectTo={"/"} />
             
            <GuardedRoute>
                {/* <GuardedRoute exact path="/employee"  component={AddEmployee}  /> */}
            {/* <GuardedRoute exact path="/attendance"  component={Val//idationForm}  /> */}
            <GuardedRoute exact path="/salary"  component={SalaryReport}  />
            <GuardedRoute exact path="/team"  component={Userlist}  />
            <GuardedRoute exact path="/leave"  component={Myleavehistory}  />
            
            {/* <GuardedRoute exact path="/team"  component={Userlist}  /> */}

            <Route exact path="/employee">
                <AddEmployee/>
            </Route>
            <Route exact path="/team">
                <Userlist/>
            </Route>
            <Route exact path="/manage">
                <ManagerLeave/>
            </Route>


            {/* <Route exact path="/details/:id" component={Detail}> */}
            {/* <Detail name="samman"/> */}
          {/* </Route> */}
          <Route exact path="/manage" component={ManagerLeave}>
            {/* <Detail name="samman"/> */}
          </Route>
          <Route exact path="/verify" component={AdminLeave}>
            {/* <Detail name="samman"/> */}
          </Route>
          
          <Route exact path="/own">
                <OwnAttendance/>
            </Route>


                <NotFound/>
            </GuardedRoute>
        </Switch>
    );
}
