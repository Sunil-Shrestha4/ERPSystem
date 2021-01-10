import React, {useEffect, useState} from "react";
import Form from "react-bootstrap/Form";
import { useHistory } from "react-router-dom";
// import LoaderButton from "../components/LoaderButton";
// import { useAppContext } from "../libs/contextLib";
import { useFormFields } from "../libs/hooksLib";
// import { onError } from "../libs/errorLib";
import "./Signup.css";
import Button from "react-bootstrap/Button";
// import useSignUpForm from "../libs/customhooks";

export default function Signup() {
  const [fields, handleFieldChange] = useFormFields({
    email: "",
    username:"",
    password: ""
  });
  const history = useHistory();
  const [newUser, setNewUser] = useState(null);

  function validateForm() {
    return (
      fields.email.length > 0 &&
      fields.password.length > 0 
      // fields.password === fields.confirmPassword
    
    );
  }
  async function handleSubmit(event) {
    event.preventDefault();
    try{
      const res = await fetch('http://127.0.0.1:8000/api/register/', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
          body: JSON.stringify(fields)
    
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
    <div className="Signup">
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="email" size="lg">
          <Form.Label>Email</Form.Label>
          <Form.Control
            autoFocus
            type="email"
            value={fields.email}
            onChange={handleFieldChange}
          />
        </Form.Group>
        <Form.Group controlId="username" size="lg">
          <Form.Label>Username</Form.Label>
          <Form.Control
            autoFocus
            type="text"
            value={fields.username}
            onChange={handleFieldChange}
          />
        </Form.Group>
        <Form.Group controlId="password" size="lg">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            value={fields.password}
            onChange={handleFieldChange}
          />
        </Form.Group>
        <Button block size="lg" type="submit" disabled={!validateForm()}>
                Signup
        </Button>
      </Form>
    </div>
  );
}

