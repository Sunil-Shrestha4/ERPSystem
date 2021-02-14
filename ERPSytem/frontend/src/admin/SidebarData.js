import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as AiOutline from 'react-icons/io';
export const SidebarData = [
  {
    title: 'Home',
    path: '/dashboard',
    icon: <AiIcons.AiFillHome />,
    cName: 'nav-text'
  },
  {
    title: 'User Profile',
    path: '/User',
    icon: <AiIcons.AiOutlineUser />,
    cName: 'nav-text'
  },
  {
    title: 'Attendance',
    path: '/attendance',
    icon: <AiIcons.AiOutlineFileAdd />,
    cName: 'nav-text'
  },
  {
    title: 'Team',
    path: '/team',
    icon: <IoIcons.IoMdPeople />,
    cName: 'nav-text'
  },
  {
    title: 'Salary',
    path: '/salaryAdd',
    icon: <FaIcons.FaEnvelopeOpenText />,
    cName: 'nav-text'
  },
  {
    title: 'Salary Report',
    path: '/salaryreport',
    icon: <FaIcons.FaEnvelopeOpenText />,
    cName: 'nav-text'
  },
  {
    title: 'Add Employee',
    path: '/employee',
    icon: <AiIcons.AiOutlineUserAdd />,
    cName: 'nav-text'
  },

  {
    title: 'Attendance',
    path: '/own',
    icon: <FaIcons.FaFistRaised />,
    cName: 'nav-text'
  },

  {
    title: 'Leave',
    path: '/leave',
    icon: <ImIcons.ImExit />,
    cName: 'nav-text'
  },
  
  {
    title: 'Leave',
    path: '/manage',
    icon: <ImIcons.ImExit />,
    cName: 'nav-text'
  },
  {
    title: 'Leave',
    path: '/verify',
    icon: <ImIcons.ImExit />,
    cName: 'nav-text'
  }

];