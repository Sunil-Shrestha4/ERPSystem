import React, { useEffect, useState, useContext } from "react";
import {Route, Switch,BrowserRouter} from "react-router-dom";
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
import Home from "./containers/Home";
import { Layout, Menu } from 'antd';

import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
  } from '@ant-design/icons';



import { IsSuperUserContext } from "./context/IsSuperUserContext";
import { Footer } from "antd/lib/layout/layout";
const { Header, Sider, Content } = Layout;




export default function Routes(){
    const [isSuperUser, setIsSuperUser] = useContext(IsSuperUserContext);
    const [collapsed, setCollapsed] = useState(false)
    const [isLoggedin,setIsLoggedin] = useState(true)

    // useEffect(() => {
    //     setIsSuperUser(localStorage.getItem("is_superuser") == "true")
    // }, [])

    const toggle=()=>{
        setCollapsed(!collapsed)
    }

    

    
    return(
        
        <BrowserRouter>
        <Switch>
        <Route exact path="/"  component={appWrapper}  />

        
        <Layout>
            <Dashboard/>
        <Layout className="site-layout" style={{ marginLeft: 200 }}>
          <Header className="site-layout-background" style={{ padding: 0 }}>
            {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
                 className: 'trigger',
                 onClick:toggle,
               }
            )}
            
          </Header>
          <Content
            className="site-layout-background"
            style={{
              margin: '24px 16px',
              padding: 24,
              minHeight: 280,
            }}
          >
  
        
        
        <GuardedRoute exact path="/signup" component={Signup}/>
        <GuardedRoute exact path="/home" component={Home}/>
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
         
        




   
          </Content>
          <Footer>© 2021 Techrida All Rights Reserved.</Footer>
          
        </Layout>
        
        </Layout>
        <GuardedRoute>
            <NotFound/>
        </GuardedRoute>
        </Switch>
        </BrowserRouter>

    );
}
