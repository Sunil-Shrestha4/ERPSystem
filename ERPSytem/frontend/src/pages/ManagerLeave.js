import React from 'react';
import {useState,useEffect} from 'react';
import { Container ,Row ,Col , Card, CardGroup} from 'react-bootstrap';
import Navbar from "../admin/Dashboard"
import './Attendance.css';
import { Dropdown, DropdownMenu, DropdownToggle, DropdownItem } from 'reactstrap';
import Button from "react-bootstrap/Button";
import Managerpost from "./Managerpost"

export default function ManagerLeave() {
    const[state, setState]=useState([]);

useEffect(async() => {
    const token= localStorage.getItem('access')
    let res = await fetch('http://127.0.0.1:8000/api/leave/', {
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
                    <Col>No. of Days:{item.number_of_days}</Col>
                    <Col>Types of leave ID:{item.types_of_leave}</Col>
                    <Col>Types of leave:{item.types_of_leaves}</Col>
                    <Col>Reason:{item.reason}</Col>
                    <Col>Remainingday:{item.remainingday}</Col>

                    <Managerpost abc={item}/>
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
                
        </div>
    )
}
