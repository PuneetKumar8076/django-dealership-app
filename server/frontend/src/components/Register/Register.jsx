import React, { useState } from "react";

function Register() {
  const [form, setForm] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  return (
    <div>
      <h2>Sign Up</h2>

      <input name="username" placeholder="Username" onChange={handleChange} /><br />
      <input name="first_name" placeholder="First Name" onChange={handleChange} /><br />
      <input name="last_name" placeholder="Last Name" onChange={handleChange} /><br />
      <input name="email" placeholder="Email" onChange={handleChange} /><br />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} /><br />

      <button>Register</button>
    </div>
  );
}

export default Register;
