import React,{useState} from 'react';
import Button from "react-bootstrap/Button";
// import { useFormFields } from "../libs/hooksLib";
// import { BooleanField, FunctionField } from "react-admin"
// import { Redirect } from 'react-router-dom';
// import PostAttendanceCO from './PostAttendanceCO';
// import GuardedRoute from "../component/guardroute";
// import {Route} from "react-router-dom";
import Attendance from './Attendance';
// import From from 'react-bootstrap'
// import updateAttendance from "./Attendance"

export default function AttendanceFilterDate({ updateAttendance }) {
    
    
    const [searchTerm , setSearchTerm] = useState("")
    
    const handleChange = (e) => {
      setSearchTerm(e.target.value)
    }

    async function handleSubmit(event) {
        const token= localStorage.getItem('access')
        event.preventDefault();
        try{
          let res = await fetch('http://127.0.0.1:8000/api/attendance/?date='+searchTerm, {
              method: 'GET',
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json',
                'Authorization': `Bearer ${token}`,
              },
              // body: JSON.stringify(attendance)
        
            })
            res = await res.json();
            console.log(res);
            updateAttendance(res)
            
            
        }catch(err){
          console.log(err)
        }
    
    
        // setIsLoading(true);
    
        // setNewUser("test");
    
        // setIsLoading(false);
      }
      
      


    return (
        <div>
            <h1>Filter by Date</h1>
        
            <form onSubmit={handleSubmit}> 
                
            <input
                type="date"name="date"
                value={searchTerm}
                onChange={handleChange} />
            <Button type="submit">
              Submit
            </Button>
                
           
            
              
            </form>
            
            
        </div>
    )
}