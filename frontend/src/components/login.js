"use client";
import React, { useState } from "react";
import Link from "next/link";
import axios from "axios";
import Login from "./login";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [otp, setOtp] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      setError("");
      if (!email || !password) {
        setError("Please fill in all fields.");
        return;
      }
      const response = await axios.post("http://localhost:8000/user/login/", {
        email,
        password,
      });
      const status = response.data.status;
     
      if ( status ==200){
       console.log("Login successful ! ", response.data.data);
       window.location.href = "/";

      }
      else {
        console.log("Invalid Email or Password !");
      }

    } catch (error) {

      console.error("Login failed", error);
    }
  };

  return (
    <>
      <div className="min-h-screen width-[100vw] bg-cover bg-black">
        <div className="h-[100vh] justify-center items-center flex">
          <div
            className="text-white text-[2rem]  w-[27vw] border-gray-500 border p-2 rounded-md"
            style={{ backdropFilter: "blur(2px)" }}
          >
            <div className="text-center">Login here!</div>
            <form className="">
              <div className="flex-col flex">
                <label className="text-[1.4rem] mt-2">Email Id:</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={email}
                  placeholder="Enter your email "
                  onChange={(e) => setEmail(e.target.value)}
                  className="text-[1.2rem] h-[4vh] bg-transparent border border-green rounded-sm"
                />
              </div>
              <div className="flex-col flex">
                <label className="text-[1.4rem] mt-2 ">Password:</label>
                <input
                  type="password"
                  name="password"
                  id="password"
                  value={password}
                  placeholder="Enter password"
                  onChange={(e) => setPassword(e.target.value)}
                  className="text-[1.2rem] h-[4vh] bg-transparent border border-green rounded-sm"
                />
              </div>
              <div className="justify-center flex bg-[#907656] mt-3 rounded-md">
                <button
                  type="button"
                  onClick={handleLogin}
                  className="text-[1.3rem]  py-1.5  "
                >
                  Login
                </button>
              </div>
              <div className="text-[1.3rem] mt-3 ">
                Don't Have an Account&nbsp;?
                <Link href="/signup">
                  <div className="text-[#907656]">Register here!</div>
                </Link>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}
