import React, { useState } from 'react';
import Button from "react-bootstrap/Button";
// import { useFormFields } from "../libs/hooksLib";
// import { BooleanField, FunctionField } from "react-admin"
// import { Redirect } from 'react-router-dom';
// import PostAttendanceCO from './PostAttendanceCO';
// import GuardedRoute from "../component/guardroute";
// import {Route} from "react-router-dom";
import Attendance from './Attendance';
import User from './User'
// import From from 'react-bootstrap'
// import empName from "./Attendance"

export default function AttendanceFilterID({ onSearch }) {


  const [searchTerm, setSearchTerm] = useState('')
  // const [options,setOptions]=useState([{
  //   emp_name:"",
  // }])


  const handleChange = (e) => {
    setSearchTerm(e.target.value)
  }



  async function handleSubmit(e) {
    e.preventDefault();
    // onSearch(searchTerm);
    const token= localStorage.getItem('access')
    
    try{
      let res = await fetch('http://127.0.0.1:8000/api/attendance/?search='+searchTerm, {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': `Bearer ${token}`,
          },
          // body: JSON.stringify(attendance)

        })
        // if(`${res.status}`.startsWith("2")){
        res = await res.json();
        onSearch(res)
       



        console.log(res,"res")


    }catch(err){
      console.log(err,'error aayo')
    }


    // setIsLoading(true);

    // setNewUser("test");

    // setIsLoading(false);
  }







  return (
    <div>
      <h1>Filter by Emp-FirstName</h1>


      <form onSubmit={handleSubmit} >
            {/* <select >
            
            <option value={Attendance.emp_name} onChange={handleChange}>
              {Attendance.emp_name}
            </option>
            )
            </select> */}

        <input
          type="text" name="first_name"
          value={searchTerm} onChange={handleChange}
        />
        <Button type="submit">
          Submit
            </Button>




      </form>


    </div>
  )
}