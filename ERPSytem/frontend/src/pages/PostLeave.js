import React,{useState} from 'react'

export default function PostLeave() {
    const[state, setState]=useState({
        id:'',
        is_approved:'false',
        is_notapproved:'false',
        is_verified:'false',
        is_notverified:'fales',
        start:'',
        end:'',
        number_of_days:'',
        reason:'',
        name:'',
        email:'',


    })
    const handleChange = (e) => {
        const {id , value} = e.target
        // console.log(value)   
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    async function handleSubmit(event){
        const token=localStorage.getItem('access')
        event.preventDefault();
        console.log(state)
        try{
            const res = await fetch('http://127.0.0.1:8000/api/leave/',{
                method:'POST',
                headers:{
                    'Accept':'application/json',
                    'Content-type':'application/json',
                    'Authorization':`Bearer ${token}`,
                },
                body:JSON.stringify(state)

            })
            console.log(await res.json());

        }catch(err){
            console.log(err)
        }
    }




    
    
    
    
    



    return (
        <div>
        <form onSubmit ={handleSubmit} >
        <p>Start Date</p> 
            <input type="date" id="start" name="start"  value={state.start}
                    onChange={handleChange}
                    />
        <p>End Date</p> 
            <input type="date"id="end" name="end"value={state.end}
                    onChange={handleChange}
                    />

        <p>Number of Days</p> 
            <input type="number" id="number_of_days" name="number_of_days" value={state.number_of_days}
                    onChange={handleChange}
                    />
        <p>Reason</p> 
            <input type="textArea" id="reason" name="reason" value={state.reason}
                    onChange={handleChange}
                    />
        
        
            


        </form>
        </div>
    )
}
