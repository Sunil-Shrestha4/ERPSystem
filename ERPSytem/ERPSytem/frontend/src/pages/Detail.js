import React, { Component } from 'react';
// import Navbar from '../components/Navbar';
import {Image} from "react-bootstrap";
import { Link } from 'react-router-dom';
import Navbar from '../admin/Dashboard';

export default class detail extends Component {
    constructor(props){
        super(props);
        console.log(props)
        this.state={
            data:""
        }
    }

    componentDidMount() {
        console.log(this.props)
        let url = `http://127.0.0.1:8000/api/profilelist/${this.props.match.params.id}`;
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

    render() {
        console.log(this.state.data)
        return (
            <div>
                < Navbar/>
                console.log(this.state.data.photo)
               <p>User name: {this.state.data.username}</p>
               <p><Image src={this.state.data.photo} width='400' height='500'/></p>
                <p>First name:{this.state.data.first_name}</p>
                <p>Last name:{this.state.data.last_name}</p>
                <p>Address:{this.state.data.address}</p>
                <p>Phone Number:{this.state.data.phone_number}</p>
                <p>Position:{this.state.data.position}</p>
                <p>Department:{this.state.data.department}</p>
                <p>Email:{this.state.data.email}</p>
                <p>Join Date:{this.state.data.date_joined}</p>
                <a  href = {this.state.data.document} target = "_blank">User Documents</a>

            </div>
        )
    }
}
