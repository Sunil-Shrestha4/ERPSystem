import React from 'react';
import  { useState, useEffect } from 'react';
import { Container ,Row ,Col} from 'react-bootstrap';
import "./User.css";
import Navbar from "../admin/Dashboard"



// import Card from 'react-bootstrap/Card';
// // import Button from 'react-bootstrap/Button';
// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';

function User() {
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
    // const [data, setData] = useState( [] );
    

    useEffect(async () => {
        const token= localStorage.getItem('access')
        let res = await fetch('http://127.0.0.1:8000/api/profilelist/viewuserdetail/', {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json',
              'Authorization': `Bearer ${token}`,
            },
            // body: JSON.stringify(user)
      
          })
          
        //   console.log(res);
          res = await res.json();
          console.log(res);
     
        setUser(res);
        
      }, []);

    
    
    return (
        <div>
            <Navbar />
            <Container className="container">
                <Row className="row">
                <Col className='column'><img src={'http://127.0.0.1:8000'+user.photo} width='300' height='360' />
                </Col>
                <Col className="column">
                    <ul className="detail">
                        <h2>USER DETAILS</h2>
                        <li>{user.email}</li>
                        <li>{user.username}</li>
                        <li>first name:     {user.first_name}</li>
                        <li>last name:     {user.last_name}</li>
                        <li>Address:     {user.address}</li>
                        <li>phone number:      {user.phone_number}</li>
                        <li>Departmant:   {user.department}</li>
                        <li>Date joined:      {user.date_joined}</li>
                        
                        
                        <a href={'http://127.0.0.1:8000'+user.document} >Documents</a>
                        {/* <li>{user.is_active}</li>
                        <li>{user.is_admin}</li>
                        <li>{user.is_superuser}</li> */}
                    </ul>     
                        
                </Col>
                </Row>
                </Container>
        </div>

            
     
    );
  }
export default User;