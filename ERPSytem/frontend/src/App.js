import React, { useEffect } from 'react';
import Navbar from "react-bootstrap/Navbar";
import './App.css';
import Routes from "./Routes";
import Nav from "react-bootstrap/Nav";
import { LinkContainer } from "react-router-bootstrap";
import { useState } from "react";
import Dashboard from './admin/Dashboard';

function App(){
  useEffect(() => {
    console.log("App has rendered")
    // return () => {
    //   cleanup
    // }
  }, [])
  
  return (
    <div className="App container py-3">
      
      
      <Routes/>
    </div>
  );
}
export default App;

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }


