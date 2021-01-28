import React from 'react'
import  { useState, useEffect } from 'react';
import {Container,Row,Col,ListGroup} from "react-bootstrap";
import Navbar from "../admin/Dashboard";
import Form from "react-bootstrap/Form";
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
const axios = require('axios');

export default function SalaryReport() {
    const [searchTerm, setSearchTerm] = useState("");
    const [searchResults, setSearchResults] = useState([{
        id:"" ,
        emp:"",
        amount:"" ,
        allowance:"" ,
        year:"",
        month:"" ,
        received_date:"" ,
        email:"",
        first_name:"",
        last_name:"",
    }]);

    const handleChange = event => {
        setSearchTerm(event.target.value);
      };
    useEffect(async() => {
        
        const access_token= localStorage.getItem('access')
        console.log("Access token in Salary Report",access_token)
        let res = await fetch(`http://127.0.0.1:8000/api/salary/?search=${searchTerm}`, {
        method: 'GET',
        headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Authorization': `Bearer ${access_token}`,
        }, })
        res = await res.json();
        setSearchResults(res);
    },[])

    const removeData = async (id) =>{
        if( window.confirm("Are you sure?")){
            const access_token= localStorage.getItem('access')
            let res = fetch(`http://127.0.0.1:8000/api/salary/${id}`,{
                method: 'DELETE',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json',
                    'Authorization': `Bearer ${access_token}`,
                    },
            }).then(res => {
                console.log(res)
                const del = searchResults.filter(sal => id !== sal.id)
                setSearchResults(del)
            })
        }   
    }
        
    return (
        <div>
            <Navbar/>
            <Form>
                <Row  md={10} className="justify-content-md-center">
                    <Col sm={5}>
                        <Form.Control size="lg" type="text" placeholder="Search by Email, Name or Month..." 
                        value={searchTerm}
                        onChange={handleChange}
                        />
                        <Form.Text className="text-muted">
                        Your Results...
                        </Form.Text>                      
                    </Col>
                </Row>  
            </Form>
                     
            <Container fluid="sm"> 
                <Table size='md' responsive='xl' borderless hover>
                    <thead>
                        <tr>
                        <th>S.No.</th>
                        <th>Emp_Id</th>
                        <th>Full Name</th>
                        <th>Email</th>
                        <th>Salary</th>
                        <th>Allowance</th>
                        <th>Year</th>
                        <th>Month</th>
                        <th>Payment Date</th>
                        <th>Options</th>
                        </tr>
                    </thead>          
                    
                {searchResults && searchResults.filter((val) =>{
                    if (searchTerm==""){
                        return val
                    }else if ((val.email.toString().toLowerCase().includes(searchTerm.toLowerCase())) ||
                    (val.month.toString().toLowerCase().includes(searchTerm.toLowerCase())) ||
                    (val.first_name.toString().toLowerCase().includes(searchTerm.toLowerCase())) ||
                    (val.last_name.toString().toLowerCase().includes(searchTerm.toLowerCase())) ||
                    (val.id.toString().toLowerCase().includes(searchTerm.toLowerCase())) ||
                    (val.year.toString().toLowerCase().includes(searchTerm.toLowerCase()))
                    ) {
                        return val
                    }
                }).map((sal,key) =>{
                    return (             
                        <tbody key={key}>
                            <tr>
                            <td>{sal.id}</td>
                            <td>{sal.emp}</td>
                            <td>{sal.first_name}&nbsp;&nbsp;{sal.last_name}</td>
                            <td>{sal.email}</td>
                            <td>{sal.amount}</td>
                            <td>{sal.allowance}</td>
                            <td>{sal.year}</td>
                            <td>{sal.month}</td>
                            <td>{sal.received_date}</td> 
                            <td className='options'>
                                <Button block size="sm" type="submit" variant="danger"
                                onClick={() => removeData(sal.id)}>Delete</Button>
                            </td>                          
                            </tr>                     
                        </tbody>                
                )})}
                </Table>
            </Container>  
        </div>
    )
}

                 
                                      
                          
                       
                  
                                     
                          
                    
          
                   
