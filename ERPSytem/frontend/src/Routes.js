import React from "react";
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
import SalaryReport from "./pages/SalaryReport";
import Userlist from "./pages/Userlist";
import Userdetails from "./pages/details";
import Salary from "./pages/Salary";

export default function Routes(){
    
    return(
        <Switch>
            {/* <Route exact path="/">
              <Home/>  
            </Route> */}
            
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
            <Route exact path="/salary"  component={Salary} />
             
            <Route>
                <NotFound/>
            </Route>
        </Switch>
    );
}
