import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as AiOutline from 'react-icons/io';
import * as ImIcons from 'react-icons/im';
export const SidebarData = [
  {
    title: 'Home',
    path: '/own',
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
    title: 'Salary Report',
    path: '/salary',
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
    path: '/own',
    icon: <ImIcons.ImExit />,
    cName: 'nav-text'
  }

];