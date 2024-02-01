"use client";
import React,{useState} from "react";
import axios from "axios";

export default function Queries(){
const [title, setTitle] = useState("");
const [content, setContent] = useState("");
 const handlePostQuery = async () => {
   try {
     await axios.post("http://localhost:8000/query/userq/", { title, content });
     // Handle success or redirect to query list
   } catch (error) {
     // Handle error
   }
 };
    return (
      <>
        <div className="min-h-screen w-[100vw] bg-[#987654]">
          <div className="flex flex-col">
            <input
              type="text"
              placeholder="Title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
            <textarea
              placeholder="Content"
              value={content}
              onChange={(e) => setContent(e.target.value)}
            ></textarea>
            <button onClick={handlePostQuery}>Post Query</button>
          </div>
        </div>
      </>
    );
}