import React, { useState } from 'react';
// import * as FaIcons from 'react-icons/fa';
// import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';
// import './Dashboard.css';
// import { IconContext } from 'react-icons';
// import {Button} from "react-bootstrap";
import Auth from '../component/auth';
import Cookies from 'js-cookie'


// // import Login from '../containers/Login'


// function Dashboard() {

//   const [sidebar, setSidebar] = useState(false);

//   const showSidebar = () => setSidebar(!sidebar);

//   async function handleSubmit(){
//     Auth.logout(()=>{
//         localStorage.removeItem('access');
//         localStorage.removeItem('refresh');
//         Cookies.remove('auth');
        

//     })
//     window.location.href = '/';
//     // history.push('/');

// }

//   return (
//     <>
//       <IconContext.Provider value={{ color: '#fff' }}>
//         <div className='navbar'>
          

        
//           <Link to='#' className='menu-bars'>
//             <FaIcons.FaBars onClick={showSidebar} />
            
//           </Link>
          
//         </div>
        
//         <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
//           <ul className='nav-menu-items' onClick={showSidebar}>



//             <li className='navbar-toggle'>
//               <Link to='#' className='menu-bars'>
//                 <AiIcons.AiOutlineClose />
//               </Link>
//             </li>
//             {SidebarData.map((item, index) => {
//               return (
//                 <li key={index} className={item.cName}>
//                   <Link to={item.path}>
//                     {item.icon}
//                     <span>{item.title}</span>
//                   </Link>
//                 </li>
//               );
//             })}
//           

//           </ul>
          
       
//         </nav>
        
//       </IconContext.Provider>
//     </>
//   );
// }

// export default Dashboard;





import './Dashboard.css';
import { Button, Radio } from 'antd';

import { Layout, Menu } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  LogoutOutlined
} from '@ant-design/icons';
import 'antd/dist/antd.css';

const { Header, Sider, Content } = Layout;

class Dashboard extends React.Component {
  state = {
    collapsed: false,
  };

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  };
  // async function handleSubmit(){
  //       Auth.logout(()=>{
  //           localStorage.removeItem('access');
  //           localStorage.removeItem('refresh');
  //           Cookies.remove('auth');
            
    
  //       })

  render() {
    return (
        <Sider 
        style={{
        overflow: 'auto',
        height: '100vh',
        position: 'fixed',
        left: 0,
      }}
         trigger={null} collapsible collapsed={this.state.collapsed}>
          <div className="logo" />
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
          {SidebarData.map((item, index) => {
              return (
                <Menu.Item key={index} icon={item.icon} >
                  <Link to={item.link}>
                    <span className='nav-text'>{item.title}</span>
                  </Link>
                  </Menu.Item>
              );
            })}
          </Menu>
          <br/>
          <Button type="primary" icon={<LogoutOutlined />} onClick={()=>{
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            Cookies.remove('auth');window.location.href = '/'}}>Logout</Button>
        </Sider>
       
    );
  }
}

export default Dashboard;

