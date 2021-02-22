import React from 'react';

export default function Managerpost(props) {
  // console.log(props.abc.reason)
  // console.log(props.reason)

  const handleApprove = () => {
    const token = localStorage.getItem('access')
      // event.preventDefault();
      fetch(`http://127.0.0.1:8000/api/leave/${props.abc.id}/`, {
        method: 'PUT',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({
          is_approved:true,
          is_notapproved:false,
          reason: props.abc.reason,
          types_of_leave:props.abc.types_of_leave,
          remainingday:props.abc.remainingday
        })
      }).then(res => res.json())
        // .then(response => )
        .catch(err => console.log(err.response))
  }

  const handleReject = () => {
    const token = localStorage.getItem('access')
      // event.preventDefault();
      fetch(`http://127.0.0.1:8000/api/leave/${props.abc.id}/`, {
        method: 'PUT',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({
          is_approved:false,
          is_notapproved:true,
          reason: props.abc.reason, 
          types_of_leave:props.abc.types_of_leave,
          remainingday:props.abc.remainingday
        })
      }).then(res => res.json())
        // .then(response => )
        .catch(err => console.log(err.response))
  }



  // const handleChange = (e) => {
  //     const {id , value} = e.target
  //     // console.log(value)   
  //     setState(prevState => ({
  //         ...prevState,
  //         [id] : value
  //     }))
  // }


  // const toggle = React.useCallback(
  //   () => setState(!state),
  //   [state, setState],
  // );

  // const handleChange= event =>{
  // setState([event.target.value]);
  // }

  // async function handleSubmit(event) {
  //   const token = localStorage.getItem('access')
  //   event.preventDefault();
  //   console.log("This is state ", state)

  //   // try{
  //   let res = await fetch(`http://127.0.0.1:8000/api/leave/${props.abc.id}/`,{
  //       method: 'PUT',
  // headers: {
  //   'Accept': 'application/json',
  //   'Content-type': 'application/json',
  //   'Authorization': `Bearer ${token}`,
  //       },
  //       body: JSON.stringify(state)

  //     })
  //     .then(res => res.json())
  //     setState(res)
  //     console.log(res);
  //   console.log(await res.json());
  // }catch(err){
  //   console.log(err)
  // }
  // }




  return (
    <div>





      <button onClick={handleApprove} id="is_approved" name="is_approved"
      // onClick={() => setState((prev) => ({ ...prev.reason, is_approved: !state.is_approved }))} 
      > Approve </button>
      <br />

      <button onClick={handleReject} id="is_notapproved" name="is_notapproved"
      // onClick={() => setState((prev) => ({ ...prev.reason, is_approved: !state.is_approved }))} 
      > Reject </button>

      {/* <button onClick={() => set_is_notapproved(true)} id="is_notapproved" name="is_notapproved"
      > Reject </button> */}
      <br />
      {/* <button type="submit" id="is_notapproved" name="is_notapproved" value="rejected"
                  onClick ={handleChange} > Reject</button>
                  */}
      {/* {approve?<h1>true</h1>:<h1>false</h1>}
                    True
                  <input type="radio" onClick={()=>setApprove(true)}></input>
                  False
                  <input type="radio" onClick={()=>setApprove(false)}></input> */}

    </div>
  )
}
