import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from "./containers/Home";
import Login from "./containers/Login";
import NotFound from "./containers/NotFound";
import Signup from "./containers/Signup";
import Profile from "./containers/Profile";
import Dashboard from "./admin/Dashboard";
import GuardedRoute from "./component/guardroute";
import User from "./pages/User";
import AddEmployee from "./pages/AddEmployee";
import Attendance from "./pages/Attendance";
import SalaryReport from "./pages/SalaryReport";
import Userlist from "./containers/Userlist";
import Detail from './pages/Detail';
import OwnAttendance from './pages/OwnAttendance';
import Leave from "./pages/leave";
import PostLeave from "./pages/PostLeave";



export default function Routes(){
    
    return(
        <Switch>
            {/* <Route exact path="/">
              <Home/>  
            </Route> */}
            
            <Route exact path="/">
                <Login/>
            </Route>
            <Route exact path="/signup">
                <Signup/>
            </Route>
            {/* <Route exact path="/profile">
                <Dashboard/>
            </Route> */}
            {/* <GuardedRoute /> */}
            <GuardedRoute exact path="/profile"  component={Dashboard}  />
            <Route exact path="/User">
                <User />
            </Route>
            <GuardedRoute exact path="/employee"  component={AddEmployee}  />
            <GuardedRoute exact path="/attendance"  component={Attendance}  />
            <GuardedRoute exact path="/salary"  component={SalaryReport}  />
            <GuardedRoute exact path="/team"  component={Userlist}  />
            <GuardedRoute exact path="/leave"  component={PostLeave}  />
            
            {/* <GuardedRoute exact path="/team"  component={Userlist}  /> */}

            <Route exact path="/team">
                <Userlist/>
            </Route>

            <Route exact path="/details/:id" component={Detail}>
            {/* <Detail name="samman"/> */}
          </Route>
          
          <Route exact path="/own">
                <OwnAttendance/>
            </Route>


            <Route>
                <NotFound/>
            </Route>
        </Switch>
    );
}
