import React from 'react';
import  { useState, useEffect } from 'react';
import { Container ,Row ,Col, ListGroup} from 'react-bootstrap';
import "./User.css";
import Navbar from "../admin/Dashboard";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';

export default function User() {
    const [user, setUser] = useState( {
        email:'',
        username:'',
        first_name:'',
        last_name:'',
        address:'',
        phone_number:'',
        department:'',
        date_joined:'',
        document:'',
        photo:'' ,
        is_active:'',
        is_superuser:'',
        is_staff:'',       
    });    

    useEffect(async () => {
        const token= localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/profilelist/viewuserdetail/', {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json',
              'Authorization': `Bearer ${token}`,
            },      
          })
          res = await res.json();
          console.log(res);
     
        setUser(res);
        
      }, []);

    
    
    return (              
        <div>
        <Navbar /> 
        <Container className="container">
          <Row >
            <Col >
              <img src={'file://home/bimarsha/Pictures/72BCT612 (1).jpg' + '{user.photo}'} width='200' height='200' />
            </Col>
            <Col xs={8}>
                
            </Col>
          </Row>

          <Row>
            <Col>
            </Col>
            <Col xs={8}>
            <Card>
                <Card.Header>
                  <Nav variant="tabs" defaultActiveKey="#first">
                    <Nav.Item>
                      <Nav.Link href="#first">About</Nav.Link>
                    </Nav.Item>
                  </Nav>
                </Card.Header>
                <Card.Body>
                  {/* <Card.Title>Special title treatment</Card.Title> */}
                  <Card.Text>
                    <ListGroup>
                      <ListGroup.Item>Email: {user.email}</ListGroup.Item>
                      <ListGroup.Item>Username: {user.username}</ListGroup.Item>
                      <ListGroup.Item>first name:     {user.first_name}</ListGroup.Item>
                      <ListGroup.Item>last name:     {user.last_name}</ListGroup.Item>
                      <ListGroup.Item>Address:     {user.address}</ListGroup.Item>
                      <ListGroup.Item>phone number:      {user.phone_number}</ListGroup.Item>
                      <ListGroup.Item>Departmant:   {user.department}</ListGroup.Item>
                      <ListGroup.Item>Date joined:      {user.date_joined}</ListGroup.Item>
                    </ListGroup>
                  </Card.Text>
                  <Button variant="danger">Logout</Button>
                </Card.Body>
                </Card>
            </Col>

          </Row>

        </Container>   
      </div> 
    );
  }
