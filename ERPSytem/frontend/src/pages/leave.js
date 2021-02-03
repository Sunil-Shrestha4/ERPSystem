import React from 'react';
import {useState,useEffect} from 'react';
import { Container ,Row ,Col , Card, CardGroup} from 'react-bootstrap';
import Navbar from "../admin/Dashboard"
import './Attendance.css';
import { Dropdown, DropdownMenu, DropdownToggle, DropdownItem } from 'reactstrap';
import ManagerLeave from "./ManagerLeave"

export default function Leave(){
    const[leave,setLeave]=useState([
        {
            id:"",
            is_approved:"false",
            is_verified:"false",
            name:"",
            email:"",
            start:"",
            end:"",
            number_of_days:"",
            reason:""
        }
    ]);
    
    useEffect(async() =>{
        const token =localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/leave/MyLeaveHistory/',{

            method:'GET',
            headers:{
                'Accept':'application/json',
                'Content-type':'application/json',
                'Authorization':`Bearer ${token}`,

            },
        })
        res=await res.json();
        console.log(res);
        setLeave(res);
    },[])


    return(
        <div>
            <Navbar/>
            <h1>Leave History</h1>

            <ul>
                {leave.map((item)=>(
                    <CardGroup className="card">
                    <Card style={{ width: '18rem' }} border="success">
                     <Row>
                     <Col>Leave Id:{item.id}</Col>
                     <Col>Leave Approved:{item.is_approved+""}</Col>
                     <Col>Leave Verified:{item.is_verified+""}</Col>
                     <Col>Name:{item.name}</Col>
                     <Col>Start date:{item.start_date}</Col>
                     <Col>End Date:{item.end_date}</Col>
                     <Col>No. of Days:{item.number_of_days}</Col>
                     <Col>Reason:{item.reason}</Col>

                     <ManagerLeave UpdateLeave ={setLeave}/> 
                     

                     <br/>
                     </Row>
                     </Card> 
                     </CardGroup>
                     

                ))}
                



            </ul>
            {/* <ManagerLeave Leave id ={item.id}/> 
            <ManagerLeave Name={item.name} /> */}
        </div>
    )





}