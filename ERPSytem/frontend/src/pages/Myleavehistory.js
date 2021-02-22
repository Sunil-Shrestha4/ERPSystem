import React from 'react';
import {useState,useEffect} from 'react';
import { Container ,Row ,Col , Card, CardGroup} from 'react-bootstrap';
import Navbar from "../admin/Dashboard"
import './Attendance.css';
import { Dropdown, DropdownMenu, DropdownToggle, DropdownItem } from 'reactstrap';
import Button from "react-bootstrap/Button";
import PostLeave from './PostLeave'


export default function Myleavehistory() {
    const[state, setState]=useState([]);

useEffect(async() => {
    const token= localStorage.getItem('access')
    let res = await fetch('http://127.0.0.1:8000/api/leave/MyLeaveHistory/', {
        method: 'GET',
        headers: {
            
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Authorization': `Bearer ${token}`,
        }, })
        res = await res.json();
        console.log(res);
        setState(res);
        

    
}, [])


// const handleChange = (e) => {
//     const {id , value} = e.target
//     // console.log(value)   
//     setState(prevState => ({
//         ...prevState,
//         [id] : value
//     }))
// }

// async function handleSubmit(event) {
//     const token= localStorage.getItem('access')
//     event.preventDefault();
//     console.log(state)
//     console.log(state.id)
//     try{
//       const res = await fetch(`http://127.0.0.1:8000/api/leave/${state.id}`, {
//           method: 'PUT',
//           headers: {
//             'Accept': 'application/json',
//             'Content-type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//           },
//           body: JSON.stringify(state)
    
//         })
//       console.log(await res.json());
//     }catch(err){
//       console.log(err)
//     }


    // setIsLoading(true);

    // setNewUser("test");

    // setIsLoading(false);
//   }






    return (
        <div>
           <Navbar/>
           <h1>Leave History</h1>
          
     
           
           {/* <button onClick={()=>set('true')}>Change</button> */}

            <ul>
                {state.map((item)=>(
                    <CardGroup className="card">
                    <Card style={{ width: '18rem' }} border="success">
                    <Row>
                    <Col>Leave Id:{item.id}</Col>
                    <Col>Leave Approved:{item.is_approved+""}</Col>
                    <Col>Leave Verified:{item.is_verified+""}</Col>
                    <Col>Name:{item.name}</Col>
                    <Col>Start date:{item.start}</Col>
                    <Col>End Date:{item.end}</Col>
                    <Col>Types of leave:{item.types_of_leave}</Col>
                    <Col>No. of Days:{item.number_of_days}</Col>
                    <Col>Reason:{item.reason}</Col>
                    <Col>Remaining day:{item.remainingday}</Col>
                   
                   
                   
                    {/* <Managerpost reason={item.reason} />
                    <Managerpost name={item.name} />
                    <Managerpost start={item.start} />
                    <Managerpost end={item.end} />
                    <Managerpost number_of_days={item.number_of_days}/>
             */}
              


                

                    
                    

                    <br/>
                    </Row>
                    </Card> 
                    </CardGroup>
                    

                ))}
                



                </ul>
                <br/>
                <h1>Please fill the form with valid reason to request for leave</h1>
                <PostLeave/>

                
        </div>
    )
}
