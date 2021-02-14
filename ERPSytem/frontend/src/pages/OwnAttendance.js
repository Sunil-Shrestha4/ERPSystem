import React from 'react';
import  { useState, useEffect } from 'react';
import { Container ,Row ,Col,Card,CardGroup} from 'react-bootstrap';
import "./User.css";
import Navbar from "../admin/Dashboard";
import './Attendance.css';
import { Dropdown, DropdownMenu, DropdownToggle, DropdownItem } from 'reactstrap';
<<<<<<< HEAD
import PostAttendance from './PostAttendanceCI';
import {Route, Switch} from "react-router-dom";
import PostAttendanceCO from './PostAttendanceCO';
import PostAttendanceCI from './PostAttendanceCI';
=======
import PostAttendance from './PostAttendance';
>>>>>>> origin/sunil-dev




// import Card from 'react-bootstrap/Card';
// // import Button from 'react-bootstrap/Button';
// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';

function OwnAttendance() {
    const [attendance, setAttendance] = useState([ {
        id:'',
        choices:'',
        time:'',
<<<<<<< HEAD
        date:'',
=======
>>>>>>> origin/sunil-dev
        name:''



        
    }]);
<<<<<<< HEAD
    
=======
    // const [data, setData] = useState( [] );
>>>>>>> origin/sunil-dev
    

    useEffect(async () => {
        const token= localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/attendance/view/', {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json',
              'Authorization': `Bearer ${token}`,
            },
            // body: JSON.stringify(user)
      
          })
        //   console.log(res);
          res = await res.json();
          console.log(res);
     
        setAttendance(res);
        
        
      }, []);

    
    
    return (
        <div>
            <Navbar />
            <br/>
            <br/>
<<<<<<< HEAD
            <PostAttendanceCI />
=======
            <PostAttendance/>
>>>>>>> origin/sunil-dev
            <br/>
            <br/>
            <h1>Your Attendance History</h1>
            <ul>{attendance.map((item)=>(
               <CardGroup className="card">
               <Card style={{ width: '18rem' }} border="success">
                <Row>
<<<<<<< HEAD
                <Col key={item.id}>Attendance-ID:{item.id}</Col>
                <Col>USER NAME:{item.name}</Col>
                <Col>STATUS:{item.choices}</Col>
                <Col>TIME:{item.time}</Col>
                <Col>DATE:{item.date}</Col>
=======
                <Col>Attendance-ID:{item.id}</Col>
                <Col>USER NAME:{item.name}</Col>
                <Col>STATUS:{item.choices}</Col>
                <Col>TIME:{item.time}</Col>
>>>>>>> origin/sunil-dev
                <br/>
                </Row>
                </Card> 
                </CardGroup>
            )
            )}
            </ul> 



            {/* {attendance.map((item) =>(<li>{item.name}</li>)) } */}
            
           </div>

            
     
    );
  }
export default OwnAttendance;