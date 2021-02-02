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
    icon: <IoIcons.IoMdHelpCircle />,
    cName: 'nav-text'
  },
  // {
  //   title: 'Logout',
  //   path: '/logout',
  //   icon: <IoIcons.IoMdHelpCircle />,
  //   cName: 'nav-text'
  // }
];