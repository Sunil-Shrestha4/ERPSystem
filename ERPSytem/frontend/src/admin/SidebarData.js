import React from 'react';
import Dashboard from './Dashboard';
import User from '../pages/User';
import Attendance from '../pages/Attendance';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  LogoutOutlined,
  HomeOutlined,
  PlusOutlined,
  TeamOutlined,
  DollarCircleOutlined,
  FileTextOutlined,
  UserAddOutlined,
} from '@ant-design/icons';
import Userlist from '../pages/Userlist';
import AddSalary from '../pages/SalaryAdd';
import SalaryReport from '../pages/SalaryReportList';
import AddEmployee from '../pages/AddEmployee';
export const SidebarData = [
  {
    title: 'Home',
    path: '/dashboard',
    link:'/home',
    icon: <HomeOutlined />,
    cName: 'nav-text',
    component:<Dashboard />
  },
  {
    title: 'User Profile',
    path: '/User',
    link: '/User',
    icon: <UserOutlined />,
    cName: 'nav-text',
    component:<User />
  },
  {
    title: 'Attendance',
    path: '/attendance',
    link: '/attendance',
    icon: <PlusOutlined />,
    cName: 'nav-text',
    component:<Attendance />
  },
  {
    title: 'Team',
    path: '/team',
    link: '/team',
    icon: <TeamOutlined />,
    cName: 'nav-text',
    component:<Userlist />

  },
  {
    title: 'Salary',
    path: '/salaryAdd',
    link: '/salaryAdd',
    icon: <DollarCircleOutlined />,
    cName: 'nav-text',
    component:<AddSalary />
  },
  {
    title: 'Salary Report',
    path: '/salaryreport',
    link: '/salaryreport',
    icon: <FileTextOutlined />,
    cName: 'nav-text',
    component:<SalaryReport />
  },
  {
    title: 'Add Employee',
    path: '/employee',
    link: '/employee',
    icon: <UserAddOutlined />,
    cName: 'nav-text',
    component:<AddEmployee />
  },
  // {
  //   title: 'Logout',
  //   path: '/logout',
  //   icon: <LogoutOutlined />,
  //   cName: 'nav-text'
  // }
];