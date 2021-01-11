import React from 'react';
import Navbar from "react-bootstrap/Navbar";
import './App.css';
import Routes from "./Routes";
import Nav from "react-bootstrap/Nav";
import { LinkContainer } from "react-router-bootstrap";
import { useState } from "react";

function App(){
  
  
  return (
    <div className="App container py-3">
      {/* <Navbar collapseOnSelect bg="light" expand="lg" className="mb-3">
        <LinkContainer to="/">
        <Navbar.Brand href="/" className="font-weight-bold text-muted">
          ERP System
        </Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle/>
      <Navbar.Collapse className="justify-content-end">
        <Nav activeKey={window.location.pathname}>
          
        <LinkContainer to="/logout">
            <Nav.Link>Logout</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/signup">
            <Nav.Link>Signup</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/login">
            <Nav.Link>Login</Nav.Link>
          </LinkContainer>
        </Nav>
      </Navbar.Collapse>
      </Navbar> */}
      
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


