import React from "react";
import  { useState, useEffect } from 'react';
import {Container,Col, Row} from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import Navbar from '../admin/Dashboard';
import Alert from 'react-bootstrap/Alert';
import { useFormFields } from "../libs/hooksLib";

// import DatePicker from 'react-datepicker';
import "./Salary.css";
import { FaWindows } from "react-icons/fa";

export default function AddSalary() {
    const [validated, setValidated] = useState(false);
    const[fields, handleChange] = useFormFields({
        emp: '',
        amount: '',
        allowance: '',
        month: '',
        received_date: '',
    });

    async function handleSubmit(event){
        event.preventDefault();
        const form = event.currentTarget;
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        setValidated(true);
         
        try{
            const token = localStorage.getItem('access')
            console.log("In salaray",token);
            let res = await fetch('http://127.0.0.1:8000/api/salary/',{
                method:'POST',
                body: JSON.stringify(fields),
                headers:{
                    'Accept': 'application/json',
                    'Content-type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                }
            })
            res = await res.json();
            console.log(res)
        }catch(e){
            console.log(e);
        }  
    };
    const [show, setShow] = useState(false);

    function handleClick(){
        setShow(false)  
        window.location.href = "/salary"
    }
    function handleSubmitClick(){
        return(validated ? setShow(true): null)  
    }
    return (
        <div>
        <Navbar/>
        
        <Container className="justify-content-md-center" fluid="sm"> 
        <h2>Store salary data</h2>
        <Form noValidate validated={validated} onSubmit={handleSubmit}>
            <Form.Group as={Row} controlId="emp">
                <Form.Label column sm={4}>Employee ID</Form.Label>
                <Col sm={3}>
                <Form.Control
                required
                type="text"
                placeholder="Employee ID"
                value={fields.emp}
                onChange={handleChange}
                />
                <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                <Form.Control.Feedback type="invalid">
                    Employee Id required.
                </Form.Control.Feedback>
                </Col>                
            </Form.Group>

            <Form.Group as={Row} controlId="amount">
                <Form.Label column sm={4}>Salary</Form.Label>
                <Col sm={3}>
                <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                        <InputGroup.Text id="inputGroupPrepend">Rs.</InputGroup.Text>
                    </InputGroup.Prepend>
                <Form.Control
                required
                type="text"
                placeholder="Salary"
                value={fields.amount}
                onChange={handleChange}
                />
                <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                <Form.Control.Feedback type="invalid">
                    Amount field required.
                </Form.Control.Feedback>
                </InputGroup>
                </Col>
            </Form.Group>
            <Form.Group as={Row} controlId="allowance">
                <Form.Label column sm={4}>Allowance</Form.Label>
                <Col sm={3}>
               
                <InputGroup className="mb-2">
                <InputGroup.Prepend>
                    <InputGroup.Text id="inputGroupPrepend">Rs.</InputGroup.Text>
                </InputGroup.Prepend>
                <Form.Control
                    type="text"
                    required
                    placeholder="Allowance"
                    aria-describedby="inputGroupPrepend"
                    value={fields.allowance}
                    onChange={handleChange}
                />
                <Form.Control.Feedback type="invalid">
                    Allowance field required.
                </Form.Control.Feedback>
                </InputGroup>
                </Col>
            </Form.Group>
            <Form.Group as={Row} controlId="month">
                <Form.Label column sm={4}>Month</Form.Label>
                <Col sm={3}>
                    <Form.Control type="text" placeholder="Month"
                    required
                    value={fields.month} 
                    onChange={handleChange}
                     />
                    <Form.Control.Feedback type="invalid">
                    Month field required.
                    </Form.Control.Feedback>
                </Col>        
            </Form.Group> 

            <Form.Group as={Row} controlId="received_date">
                <Form.Label column sm={4}>Payment Date</Form.Label>
                <Col sm={3}>
                    <Form.Control type="date" 
                    placeholder="Payment Date" 
                    required
                    value={fields.received_date}
                    onChange={handleChange} />
                    <Form.Control.Feedback type="invalid">
                    payment Date required.
                    </Form.Control.Feedback>
                </Col>       
            </Form.Group>
            {show ? <Alert show={show} variant="success">
            <Alert.Heading>Record Stored..</Alert.Heading>
                {/* <p>
                Salary information of employee added
                </p> */}
                {/* <hr /> */}
                <div className="d-flex justify-content-center">
                <Button onClick={handleClick} variant="success">
                    Add another record!
                </Button>
                </div>
            </Alert>
            : null}
             <div className="d-flex justify-content-center">
             {!show && <Button onClick={handleSubmitClick} type="submit">Submit </Button>    }  
             </div>
                  
        </Form>
        </Container>
        </div>   
    );
}
