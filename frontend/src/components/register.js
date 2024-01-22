"use client";
 import React, { useState } from "react";
 import Link from "next/link";
 import axios from "axios";

 export default function Register() {
   const [email, setEmail] = useState("");
   const [password, setPassword] = useState("");
   const [otp, setOtp] = useState("");
   const [error, setError] = useState("");
   const [otpsent,setOtpsent]= useState(false);

   const handleRegister = async (event) => {
     event.preventDefault();
     try {
       setError("");
       if ( !email || !password ) {
         setError("Please fill in all fields.");
         return;
       }
       const response = await axios.post(
         "http://localhost:8000/user/register/",
         {
           email,
           password,
         }
       );
       const status = response.data.status;
       if (status ==200){
         console.log("Otp is Sent to the User to Proceed");
         setOtpsent(true);
        }
       else {
         setError("Email is already in use");
         console.log("Email 's alr in use");
       }
     } catch (error) {
       console.error(error.response.data);
       setError("Registration failed. Please try again.");
     }
   };
   const handleVerify = async (event) => {
     event.preventDefault();
     try {
       setError("");
       if (!email || !password || !otp) {
         setError("Please fill in all fields.");
         return;
       }
       const response1 = await axios.post(
         "http://localhost:8000/user/verify/",
         {
           email,
           password,
           otp,
         }
       );
       const status1 = response1.data.status;
       if (status1 ==200){
        console.log("Successfully Veirfied the otp");
        window.location.href = "/";
       }
       else {
        console.log("Wrong otp");
       }
     }
    catch (error) {
        console.log(error.response.data);
        setError("Not able to verify the OTP")
    }}
   return (
     <>
       <div className="min-h-screen width-[100vw] bg-cover bg-black">
         <div className="h-[100vh] justify-center items-center flex">
           <div
             className="text-white text-[2rem]  w-[27vw] border-gray-500 border p-2 rounded-md"
             style={{ backdropFilter: "blur(2px)" }}
           >
             <div className="text-center">Register here!</div>
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
               <div className={`flex-col flex ${otpsent ? "" : "hidden"}`}>
                 <label className="text-[1.4rem] mt-2 ">Otp:</label>
                 <input
                   type="text"
                   id="otp"
                   name="otp"
                   value={otp}
                   placeholder="Enter the otp  "
                   onChange={(e) => setOtp(e.target.value)}
                   className="text-[1.2rem] h-[4vh] bg-transparent border border-green rounded-sm"
                 />
               </div>
               <div
                 className={`justify-center flex bg-[#907656] mt-3 rounded-md ${
                   otpsent ? "hidden" :""
                 }`}
               >
                 <button
                   type="button"
                   onClick={handleRegister}
                   className="text-[1.3rem]  py-1.5  "
                 >
                   Get Otp
                 </button>
               </div>
               <div
                 className={`justify-center flex bg-[#907656] mt-3 rounded-md ${
                   otpsent ? "" : "hidden"
                 }`}
               >
                 <button
                   type="button"
                   onClick={handleVerify}
                   className="text-[1.3rem]  py-1.5  "
                 >
                   Register 
                 </button>
               </div>
               <div className="text-[1.3rem] mt-3 ">
                 Already Have an Account&nbsp;?
                 <Link href="/signin">
                   <div className="text-[#907656]">Login here!</div>
                 </Link>
               </div>
             </form>
           </div>
         </div>
       </div>
     </>
   );
 }
         