import React from "react";
import Navbar from "../admin/Dashboard";
import { Container ,Row ,Col, ListGroup} from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';

export default function Userdetails(props){
    console.log(props.location.param.user);
    const user = props.location.param.user
   
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
                      <ListGroup.Item>Email: {user.email}</ListGroup.Item>
                      <ListGroup.Item>Username: {user.username}</ListGroup.Item>
                      <ListGroup.Item>first_name: {user.first_name}</ListGroup.Item>
                      <ListGroup.Item>last_name: {user.last_name}</ListGroup.Item>
                      <ListGroup.Item>address: {user.address}</ListGroup.Item>
                      <ListGroup.Item>phone_number: {user.phone_number}</ListGroup.Item>
                      <ListGroup.Item>position: {user.position}</ListGroup.Item>
                      <ListGroup.Item>department: {user.department}</ListGroup.Item>
                      <ListGroup.Item>date_joined: {user.date_joined}</ListGroup.Item>
                      <ListGroup.Item>document: {user.document}</ListGroup.Item>
                      <ListGroup.Item>photo: {user.photo}</ListGroup.Item>
                      <ListGroup.Item>created_at: {user.created_at}</ListGroup.Item>
                      <ListGroup.Item>updated_at: {user.updated_at}</ListGroup.Item>      
                      <ListGroup.Item>Is Active:     {user.is_active+""}</ListGroup.Item>
                      <ListGroup.Item>Is Staff:    {user.is_staff+""}</ListGroup.Item>
                      <ListGroup.Item>Is Superuser:     {user.is_superuser+""}</ListGroup.Item>
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