import React,{useState} from 'react';
import Button from "react-bootstrap/Button";
import { useFormFields } from "../libs/hooksLib";
import { BooleanField, FunctionField } from "react-admin"
import { Redirect } from 'react-router-dom';
import PostAttendanceCO from './PostAttendanceCO';
import GuardedRoute from "../component/guardroute";
import {Route} from "react-router-dom";


export default function PostAttendanceCI() {
    
    
    const [state , setState] = useState({
        checkin : "",
        
    })
    
    const handleChange = (e) => {
        const {id , value} = e.target
        // console.log(value)   
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    async function handleSubmit(event) {
        const token= localStorage.getItem('access')
        event.preventDefault();
        console.log(state)
        try{
          const res = await fetch('http://127.0.0.1:8000/api/checkin/', {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json',
                'Authorization': `Bearer ${token}`,
              },
              body: JSON.stringify(state)
        
            })
            window.location.href = '/owns';
          console.log(await res.json());
        }catch(err){
          console.log(err)
        }
    
    
        // setIsLoading(true);
    
        // setNewUser("test");
    
        // setIsLoading(false);
      }
      
      


    return (
        <div>
            <h1>Don't forget to do Attendance</h1>
        
            <form onSubmit={handleSubmit}> 
              <button type="submit" id="checkin"  value="True"
                  onClick ={handleChange} > Checkin</button> 
            </form>
            
            
        </div>
    )
}