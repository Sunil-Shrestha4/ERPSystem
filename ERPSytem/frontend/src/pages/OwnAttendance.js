import React from 'react';
import  { useState, useEffect } from 'react';
import { Container ,Row ,Col} from 'react-bootstrap';
import "./User.css";
import Navbar from "../admin/Dashboard"



// import Card from 'react-bootstrap/Card';
// // import Button from 'react-bootstrap/Button';
// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';

function OwnAttendance() {
    const [user, setUser] = useState( {
        id:'',
        choices:'',
        time:'',
        name:''



        
    });
    // const [data, setData] = useState( [] );
    

    useEffect(async () => {
        
        const token= localStorage.getItem('access')
        let res = await fetch(`http://127.0.0.1:8000/api/attendance/?emp_name=${}`, {
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
        console.log(user.name)
      }, []);

    
    
    return (
        <div>
            <Navbar />
            <Container className="container">
                <Row className="row">
                
                
                <Col className="column">
                    <ul className="detail">
                        <h2>USER DETAILS</h2>
                        <li>{user.name}</li>

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
export default OwnAttendance;