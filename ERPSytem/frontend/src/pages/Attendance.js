import React from 'react'
import { useState, useEffect } from 'react';
import { Container, Row, Col, Card, CardGroup } from 'react-bootstrap';
import Dashboard from "../admin/Dashboard"
import './Attendance.css'
import AttendanceFilterID from './AttendanceFilterID'
import AttendanceFilterDate from './AttendanceFilterDate'
import { set } from 'js-cookie';


export default function Attendance() {
    const [searchTerm, setSearchTerm] = useState("");

    const [attendance, setAttendance] = useState([
        {
            emp_name: '',
            choices: '',
            time: '',
            name: '',
            date: '',

        }
    ]);
    useEffect(async () => {
        const token = localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/attendance/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json',
                'Authorization': `Bearer ${token}`,
            },
        })
        res = await res.json();
        console.log(res);
        setAttendance(res);

    }, [])

    // useEffect(async() => {
    //     if (searchTerm) {
    //         const token = localStorage.getItem('access')
    //         try {
    //             let res = await fetch(`http://127.0.0.1:8000/api/attendance/?search=${searchTerm}`, {
    //                 method: 'GET',
    //                 headers: {
    //                     'Accept': 'application/json',
    //                     'Content-type': 'application/json',
    //                     'Authorization': `Bearer ${token}`,
    //                 },

    //             })
    //             if(`${res.status}`.startsWith("2")){
    //                 res = await res.json();
    //                 setAttendance(res);
    //             }
                
    //         }catch(err){
    //             console.log(err);
    //         }
    //     }
        
    // }, [searchTerm])

    

    return (
        <div>
            <Row>
                <Col><AttendanceFilterID onSearch={setAttendance} /></Col>
                <Col><AttendanceFilterDate updateAttendance={setAttendance} /></Col></Row>


            <ul>{attendance.map((item) => (
                <CardGroup className="card">
                    <Card style={{ width: '18rem' }} border="success">
                        <Row>
                            <Col>EMP-ID:{item.emp_name}</Col>
                            <Col>NAME:{item.name}</Col>
                            <Col>STATUS:{item.choices}</Col>
                            <Col>TIME:{item.time}</Col>
                            <Col>TIME:{item.date}</Col>
                            <br />
                        </Row>
                    </Card>
                </CardGroup>
            )
            )}
            </ul>






        </div>
    )
}
