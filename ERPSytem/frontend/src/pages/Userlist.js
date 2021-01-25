import React, { useState, useEffect } from 'react';
import User from "./User";
import { Link } from 'react-router-dom';
import Navbar from "../admin/Dashboard";
import { Container ,Row ,Col, ListGroup} from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';

export default function Userlist(){
    const [list, setList] = useState( [{ 
        id:'',
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
        is_staff:''        
    }]);

    useEffect(async () => {
        const token= localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/profilelist/', {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json',
              'Authorization': `Bearer ${token}`,
            },
          })
          res = await res.json();
          console.log(res);
        
        setList(res);
        
      },[]);
    return(
          <div>
            <Navbar/>
            <Container className="container">
            <Row >
              <Col >
                
              </Col>
              <Col xs={9}>
              <Card>
                <Card.Body>
                <ListGroup>
                  {list.map((item) =>(
                  <ListGroup.Item key={item.id}><Link to={{pathname:`/details/${item.id}`, param:{user:item}}}> {item.email}</Link> </ListGroup.Item> 
                  ))}                
                </ListGroup>
              </Card.Body>
              </Card>
              </Col>
          </Row>
          </Container>        
          </div>               
      
        )
}

