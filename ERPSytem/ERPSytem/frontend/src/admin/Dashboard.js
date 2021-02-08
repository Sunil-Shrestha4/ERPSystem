import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';
import './Dashboard.css';
import { IconContext } from 'react-icons';
import {Button} from "react-bootstrap";
import Auth from '../component/auth';
import Cookies from 'js-cookie'


// import Login from '../containers/Login'


function Dashboard() {

  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => setSidebar(!sidebar);

  async function handleSubmit(){
    Auth.logout(()=>{
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        Cookies.remove('auth');
        

    })
    window.location.href = '/';
    // history.push('/');

}

  return (
    <>
      <IconContext.Provider value={{ color: '#fff' }}>
        <div className='navbar'>
          

        
          <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar} />
            
          </Link>
          <div className="header">
          <h3 >EMPLOYEE MANAGEMENT SYSTEM</h3>
          </div>
          
        </div>
        
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
          <ul className='nav-menu-items' onClick={showSidebar}>



            <li className='navbar-toggle'>
              <Link to='#' className='menu-bars'>
                <AiIcons.AiOutlineClose />
              </Link>
            </li>
            {SidebarData.map((item, index) => {
              return (
                <li key={index} className={item.cName}>
                  <Link to={item.path}>
                    {item.icon}
                    <span>{item.title}</span>
                  </Link>
                </li>
              );
            })}
          <Button onClick={handleSubmit}>Logout</Button>

          </ul>
          
       
        </nav>
        
      </IconContext.Provider>
    </>
  );
}

export default Dashboard;