import React, { Component } from 'react';
import Navbar from '../admin/Dashboard';
import axios from 'axios';
import './AddEmployee.css';
import { Container,Row,Col } from 'react-bootstrap';
 
 

  const initialState = {
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
    photo:null,
    usernameError: "",
    usernameSpecialCharacterError: "",
    firstnameError:"",
    firstnameSpecialCharacterError:"",
    lastnameError:"",
    lastnameSpecialCharacterError:"",
  
    addressError:"",
    emailError:"",
    photoError:"",
    fileError:"",
    passwordError:"",
    passwordLengthError:"",
    addressError:"",
    positionError:"",
    departmentError:"",
    phonenumberError:"",
    isError:false
    };
    

  export default class AddEmployee extends Component {
    state=initialState;
    
  
    //this.handleChange=this.handleChange.bind(this);
changeHandler= event => {
  const isCheckbox = event.target.type === "checkbox";
  this.setState({
    [event.target.name]:isCheckbox
     ? event.target.checked
     :event.target.value
  });
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

validate = () => {
  
  let usernameError = "";
  let passwordError = "";
  let firstnameError = "";
  let lastnameError = "";
  let emailError = "";
  let photoError = "";

  let fileError = "";
  let addressError = "";
  let positionError = "";
  let departmentError = "";
  let usernameSpecialCharacterError="";
  let passwordLengthError="";
  let firstnameSpecialCharacterError="";
  let lastnameSpecialCharacterError="";
  let phonenumberError="";


  if (!this.state.username) {
    usernameError = "username cannot be blank and should be unique";
  }
  
  
  if(!this.state.username.match(/^[a-zA-Z0-9]+$/)){
    usernameSpecialCharacterError = "username should not contain special characters";
  }


  if (!this.state.first_name) {
    firstnameError = "firstname cannot be blank";
  }
  if (!this.state.first_name) {
    firstnameError = "firstname cannot be blank";
  }
  
  // if(!this.state.first_name.match(/^[a-zA-Z]+$/)){
  //   firstnameError = "First name should only contain Alphabets";
  // }
  if (!this.state.last_name) {
    lastnameError = "lastname cannot be blank";
  }
  if(!this.state.last_name.match(/^[a-zA-Z]+$/)){
    lastnameSpecialCharacterError = "Last name should only contain Alphabets";
  }
  if (!this.state.photo) {
    photoError = "You need to choose your photo";
  }
  if (!this.state.file) {
    fileError = "You need to choose file";
  }
  if (!this.state.password) {
    passwordError = "Password should be of at least 6 character";
  }
  if (this.state.password.length <5) {
    passwordLengthError = "Password should be of at least 6 character";
  }
  if (!this.state.address) {
    addressError = "address cannot be blank";
  }
  if (!this.state.position) {
    positionError = "Position cannot be blank";
  }
  if (!this.state.department) {
    departmentError = "Department cannot be blank";
  }
  if (this.state.phone_number.length !=10) {
    phonenumberError = "Please enter valid phone number";
  }
  
  
  


  if (!this.state.email.includes("@")) {
     emailError = "Invalid email, it should contain @ and .";
  }

  if (!this.state.email.includes(".")) {
    emailError = "Invalid email,it should contain @ and .";
 }

  if (emailError || usernameError || firstnameError || lastnameError || photoError || fileError || passwordError || addressError || positionError || departmentError ||usernameSpecialCharacterError ||passwordLengthError || lastnameSpecialCharacterError,firstnameSpecialCharacterError || phonenumberError) {
    this.setState({ emailError, usernameError,firstnameError,lastnameError,photoError,fileError,passwordError,addressError,positionError,departmentError,usernameSpecialCharacterError,passwordLengthError,firstnameSpecialCharacterError,lastnameSpecialCharacterError,phonenumberError });
    return false;
  }
  return true;
  
};





 
handleSubmit = event => {
  const token= localStorage.getItem('access')
  event.preventDefault();
  
  const isValid = this.validate();
  // this.props.history.push('/team')
  if (isValid) {
    console.log(isValid);
    // clear form
    this.setState(this.initialState);
    // this.props.history.push('/team')
  }
  // this.props.history.push('/team')
  
  // else{
  //   this.props.history.push('/team')

  // }
  

  
  

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
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.usernameError}
          </div>
          <div style={{ fontSize: 12, color: "red" }}>
            {this.state.usernameSpecialCharacterError}
          </div>
                <p>Email</p>
                    <input value={this.state.email} type="email" name="email"
                    onChange={this.changeHandler}

                    />
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.emailError}
          </div>
                    <p>Password</p>
                    <input value={this.state.password} type="password" name="password"
                    onChange={this.changeHandler}
                    />
                     {/* <div style={{ fontSize: 12, color: "red" }}>
            {this.state.passwordError}
          </div> */}
          <div style={{ fontSize: 12, color: "red" }}>
            {this.state.passwordLengthError}
          </div>
                    
                <p>First name</p>
                <input value={this.state.first_name} type="text" name="first_name"
                    onChange={this.changeHandler}
                    />
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.firstnameError}
            
          </div>
          <div style={{ fontSize: 12, color: "red" }}>
            {this.state.firstnameSpecialCharacterError}
            </div>
                
                
                <p>Last name:</p>
                    <input value={this.state.last_name} type="text" name="last_name"
                    onChange={this.changeHandler}
                    />
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.lastnameError}
          </div>
          <div style={{ fontSize: 12, color: "red" }}>
            {this.state.lastnameSpecialCharacternameError}
            </div>
                
                
                <p>Phone Number</p>
                    <input value={this.state.phone_number} type="number" name="phone_number"
                    onChange={this.changeHandler}
                    />
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.phonenumberError}
            </div>
                </Col>
                    <Col>
                <p>Address</p>
                    <input value={this.state.address} type="text" name="address"
                    onChange={this.changeHandler}
                    />
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.addressError}
          </div>
                    
                <p>Position:</p>
                <input value={this.state.position} type="text" name="position"
                    onChange={this.changeHandler}
                    />
                    <div style={{ fontSize: 12, color: "red" }}>
            {this.state.positionError}
          </div>
    
                    <p>Date joined </p>
                <input value={this.state.date_joined} type="date" name="date_joined"
                    onChange={this.changeHandler}
                    
    
                    />
                    
                    <p>Department </p>
                <input value={this.state.department} type="number" name="department"
                    onChange={this.changeHandler}
                />
                <div style={{ fontSize: 12, color: "red" }}>
            {this.state.usernameError}
          </div>
                <p>Documents </p>
                <input file={this.state.document} type="file" className="document"
                    onChange={this.handleFileChange}
                />
                {/* <div style={{ fontSize: 12, color: "red" }}>
            {this.state.fileError}
          </div> */}
                <p>Photo </p>
                <input file={this.state.photo} type="file" className="document"
                    onChange={this.handleImageChange} 
                />
                <div style={{ fontSize: 12, color: "red" }}>
            {this.state.photoError}
          </div>
                
                </Col>
                 </Row>
                    <input style={buttonstyle}  type="submit"/>
                    </form>
                   
              </div >
              <div>
              {/* <button style={buttonstyle} onClick={this.submitForm} class="add">Add</button> */}
              </div>
              
              </Container>      
              
      </div>
    );
  }
}
