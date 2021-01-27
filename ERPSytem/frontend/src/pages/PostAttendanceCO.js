import React,{useState} from 'react';
import Button from "react-bootstrap/Button";
import { useFormFields } from "../libs/hooksLib";
import { BooleanField, FunctionField } from "react-admin"


export default function PostAttendanceCO() {
    
    const [state , setState] = useState({
        checkout : "",
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
          const res = await fetch('http://127.0.0.1:8000/api/checkout/', {
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
    
    
      }


    return (
        <div>
            <h1>Don't forget to do CheckOut</h1>
            
        
            <form onSubmit={handleSubmit}> 
              <button type="submit" id="checkout"  value="True"
                  onClick ={handleChange} > Checkout</button>
            </form>
        </div>
    )
}