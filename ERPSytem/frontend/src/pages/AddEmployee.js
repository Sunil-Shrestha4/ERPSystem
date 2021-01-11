import React, { Component } from 'react';
import Navbar from '../admin/Dashboard';
import axios from 'axios';
import './AddEmployee.css';
import { Container,Row,Col } from 'react-bootstrap';
 
 
export default class AddEmployee extends Component {
  constructor(){
    super();
    this.state={
        username:"",
        email:"",
        password:"",
        first_name:"",
        last_name:"",
        address:"",
        phone_number:"",
        department:"",
        date_joined:"",
        document:null,
        photo:null
 
    }
    
  
    //this.handleChange=this.handleChange.bind(this);
}
 
changeHandler= (e) => {
  this.setState({
    [e.target.name]: e.target.value
  })
};
 
handleImageChange = event => { 
  // Update the state 
  this.setState({ photo: event.target.files[0] })
 
}; 
handleFileChange = (e) => {
  this.setState({
    document:e.target.files[0]
  })
};
 
handleSubmit = (e) => {
  const token= localStorage.getItem('access')
  e.preventDefault();
  console.log(this.state);
  let form_data = new FormData();
  form_data.append('username', this.state.username);
  form_data.append('email', this.state.email);
  form_data.append('password', this.state.password);
  form_data.append('first_name', this.state.first_name);
  form_data.append('last_name', this.state.last_name);
  form_data.append('address', this.state.address);
  form_data.append('phone_number', this.state.phone_number);
  form_data.append('department', this.state.department);
  form_data.append('date_joined', this.state.date_joined);
  form_data.append('document', this.state.document);
  form_data.append('photo', this.state.photo);
  let url = 'http://127.0.0.1:8000/api/register/';
  axios.post(url, form_data, {
    body:JSON.stringify(this.state),
    headers: {
      'content-type': 'multipart/form-data',

      'Authorization': `Bearer ${token}`,
    },
    // body: JSON.stringify(this.state)
  })
      .then(res => {
        console.log(res.data);
      })
      .catch(err => console.log(err))
};
  render() {
    console.log(this.state);
    const mystyle = {
    // display: "grid",
    // gridTemplateColumns: "50px 300px 50px 300px 50px 300px",
    // gap: "20px",
    // padding: "40px",
    // border: "5px solid gray" 
    
 
      // gridTemplateColumns: "60px 60px"
    };
 
    const buttonstyle={
      backgroundColor: "#008CBA",
      color: "white",
      border: "2px solid #555555",
  
      left:"50%",
      height:"60px",
      width:"100px",
      borderRadius: "8px",
    
      
    }
 
    return (
      <div>
        < Navbar/>
        <Container>
            
          <h1>Add Employee Here</h1>
          <div>
         
            <form style={mystyle} onSubmit={this.handleSubmit}>
            <Row>
                <Col>
            <p>User name</p> 
            <input value={this.state.username} type="text" name="username"
                    onChange={this.changeHandler}
                    />
                <p>Email</p>
                    <input value={this.state.email} type="email" name="email"
                    onChange={this.changeHandler}
                    />
                    <p>Password</p>
                    <input value={this.state.password} type="password" name="password"
                    onChange={this.changeHandler}
                    />
                <p>First name</p>
                <input value={this.state.first_name} type="text" name="first_name"
                    onChange={this.changeHandler}
                    />
                
                
                <p>Last name:</p>
                    <input value={this.state.last_name} type="text" name="last_name"
                    onChange={this.changeHandler}
                    />
                
                <p>Phone Number</p>
                    <input value={this.state.phone_number} type="number" name="phone_number"
                    onChange={this.changeHandler}
                    />
                </Col>
                    <Col>
                <p>Address</p>
                    <input value={this.state.address} type="text" name="address"
                    onChange={this.changeHandler}
                    />
                    
                <p>Position:</p>
                <input value={this.state.position} type="text" name="position"
                    onChange={this.changeHandler}
                    />
    
                    <p>Date joined </p>
                <input value={this.state.date_joined} type="date" name="date_joined"
                    onChange={this.changeHandler}
                    
    
                    />
                    
                    <p>Department </p>
                <input value={this.state.department} type="text" name="department"
                    onChange={this.changeHandler}
                />
                <p>Documents </p>
                <input file={this.state.document} type="file" className="document"
                    onChange={this.handleFileChange}
                />
                <p>Photo </p>
                <input file={this.state.photo} type="file" className="document"
                    onChange={this.handleImageChange} 
                /></Col>
                 </Row>
                    <input style={buttonstyle}  type="submit"/>
                    
                    </form>
                   
              </div >
              <div>
              {/* <button style={buttonstyle} onClick={this.submitForm} class="add">Add</button> */}
              </div>
              
              </Container>      
              
      </div>
    )
  }
}
