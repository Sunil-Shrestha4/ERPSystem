import React,{useState} from 'react';
import Button from "react-bootstrap/Button";
import { useFormFields } from "../libs/hooksLib";


export default function PostAttendance() {
    
    const [state , setState] = useState({
        choices : "",
        // checkin:"",
        // checkout:"",
        // CI: "",
        // CO:""
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
          const res = await fetch('http://127.0.0.1:8000/api/attendance/', {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json',
                'Authorization': `Bearer ${token}`,
              },
              body: JSON.stringify(state)
        
            })
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
                


                
                <button type="submit" id="choices" name="choices" value="CI"
                    onClick ={handleChange} > Checkin</button>
                    <br/>
                    <br/>
                <button type="submit" id="choices" name="choices" value="CO"
                    onClick ={handleChange} > Checkout</button>
                

            </form>
        </div>
    )
}