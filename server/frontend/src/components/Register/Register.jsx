import React, { useState } from "react";

function Register() {
  const [form, setForm] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Registered Successfully!");
  };

  return (
    <div>
      <h2>Sign Up</h2>

      <form onSubmit={handleSubmit}>
        <input name="username" placeholder="Username" onChange={handleChange} /><br /><br />
        <input name="first_name" placeholder="First Name" onChange={handleChange} /><br /><br />
        <input name="last_name" placeholder="Last Name" onChange={handleChange} /><br /><br />
        <input name="email" type="email" placeholder="Email" onChange={handleChange} /><br /><br />
        <input name="password" type="password" placeholder="Password" onChange={handleChange} /><br /><br />

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;