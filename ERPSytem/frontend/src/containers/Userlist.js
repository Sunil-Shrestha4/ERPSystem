import React, { Component } from 'react';
// import Card from 'react-bootstrap/Card';
// // import Button from 'react-bootstrap/Button';
// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';
import {Image} from "react-bootstrap";
import Navbar from '../admin/Dashboard';

class Userlist extends Component {
    constructor(props){
        super(props);
        this.state={
            data: []
        }
    }

    clickMe(data){
        
        console.log(data);
    }
    

    componentDidMount() {
        let url = "http://127.0.0.1:8000/api/profilelist/";
        fetch(url,{
            method:'GET',
            headers:{
                'Accept':'application/json',
                'content-Type':'application/json',
            }


        })
        .then((result)=>{
            result.json()
            .then((resp)=>{
            
            this.setState({data:resp})

            })

        })  
    
    }

    render(){
        const {data} =this.state;

         console.log(data);
        return(
            <div>
               <Navbar />
                <h1>Our Team</h1>
                {
                    data ?
                    <div style={{columnCount:"3"}}>
                        <ul>
                            {this.state.data.map((data, index) => (
                                <li><a href={`/details/${data.id}`}><Image src={data.photo} width='120' height='120'style={{borderRadius: '50%'}}/><br/>
                                    </a>
                                    <p>{data.username}</p>
                                    <p>{data.department}</p>
                                    <br/>
                                    <br/>
                                    <br/>
                                    <br/>
                                 </li>
                                 ))}
                        </ul>


                    </div>
                    :<p> Please wait ...</p>




                }



                
            </div>
            

                

                 


            
        )
    }
}
export default Userlist;