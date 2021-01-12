import React from "react";
import Navbar from "../admin/Dashboard";
import { Container ,Row ,Col, ListGroup} from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';

export default function Userdetails(props){
    console.log(props.location.param.user);
   
    return (
        <div>
        <Navbar /> 
        <Container className="container">
          <Row >
            <Col >
              <img src={''} width='200' height='200' />
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
                      <ListGroup.Item>Email: {props.location.param.user.email}</ListGroup.Item>
                      <ListGroup.Item>Username: {props.location.param.user.username}</ListGroup.Item>
                      <ListGroup.Item>first_name: {props.location.param.user.first_name}</ListGroup.Item>
                      <ListGroup.Item>last_name: {props.location.param.user.last_name}</ListGroup.Item>
                      <ListGroup.Item>address: {props.location.param.user.address}</ListGroup.Item>
                      <ListGroup.Item>phone_number: {props.location.param.user.phone_number}</ListGroup.Item>
                      <ListGroup.Item>position: {props.location.param.user.position}</ListGroup.Item>
                      <ListGroup.Item>department: {props.location.param.user.department}</ListGroup.Item>
                      <ListGroup.Item>date_joined: {props.location.param.user.date_joined}</ListGroup.Item>
                      <ListGroup.Item>document: {props.location.param.user.document}</ListGroup.Item>
                      <ListGroup.Item>photo: {props.location.param.user.photo}</ListGroup.Item>
                      <ListGroup.Item>created_at: {props.location.param.user.created_at}</ListGroup.Item>
                      <ListGroup.Item>updated_at: {props.location.param.user.updated_at}</ListGroup.Item>      
                      <ListGroup.Item>Is Active:     {props.location.param.user.is_active+""}</ListGroup.Item>
                      <ListGroup.Item>Is Staff:    {props.location.param.user.is_staff+""}</ListGroup.Item>
                      <ListGroup.Item>Is Superuser:     {props.location.param.user.is_superuser+""}</ListGroup.Item>
                    </ListGroup>
                  </Card.Text>
                  <Button variant="primary">Go somewhere</Button>
                </Card.Body>
                </Card>
            </Col>
          </Row>

        </Container>   
      </div> 
        

    )
}