import React from 'react'
import  { useState, useEffect } from 'react';
import {Container,Row,Col,Card,CardGroup} from "react-bootstrap";
import Navbar from "../admin/Dashboard"


export default function SalaryReport() {
    const [salary,setSalary]=useState([
        {
        username:'',
        department:'',
        amount:'',
        }


    ]);
    useEffect(async() => {
        
            const token= localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/salary/', {
            method: 'GET',
            headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': `Bearer ${token}`,
            }, })
            res = await res.json();
            console.log(res);
            setSalary(res);
        
    }, [])
    return (
        <div>
             <Navbar/>
            
                <ul>{salary.map((sal)=>(
                    <CardGroup className="card">
                    <Card style={{ width: '18rem' }} border="success">
                    <Row>
                    <Col>EMP-ID:{sal.username}</Col>
                    <Col>NAME:{sal.amount}</Col>
                    <Col>STATUS:{sal.department}</Col>
                    
                    <br/>
                    </Row>
                    </Card> 
                    </CardGroup>
                )
                )}
                </ul> 
        </div>
    )
}
