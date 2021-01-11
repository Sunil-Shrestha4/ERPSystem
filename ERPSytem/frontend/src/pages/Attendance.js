import React from 'react'
import  { useState, useEffect } from 'react';
import { Container ,Row ,Col , Card, CardGroup} from 'react-bootstrap';
import Navbar from "../admin/Dashboard"
import './Attendance.css';
import { Dropdown, DropdownMenu, DropdownToggle, DropdownItem } from 'reactstrap';

export default function Attendance() {
    const [attendance, setAttendance] = useState([
        {
            emp_name:'',
            choices:'',
            time:'',
            name:'',
        }
    ]);
    
    useEffect(async() => {
        const token= localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/attendance/', {
            method: 'GET',
            headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': `Bearer ${token}`,
            }, })
            res = await res.json();
            console.log(res);
            setAttendance(res);
            

        
    }, [])

    return (
        <div>
           <Navbar/>
            
           <ul>{attendance.map((item)=>(
               <CardGroup className="card">
               <Card style={{ width: '18rem' }} border="success">
                <Row>
                <Col>EMP-ID:{item.emp_name}</Col>
                <Col>NAME:{item.name}</Col>
                <Col>STATUS:{item.choices}</Col>
                <Col>TIME:{item.time}</Col>
                <br/>
                </Row>
                </Card> 
                </CardGroup>
            )
            )}
            </ul> 
            <h1>Don't forget to make </h1>
            <form>
                
<button type="button" >Check In</button>

            </form>
           
        
            
            
            
            
        </div>
    )
}
