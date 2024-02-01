"use client";
import { useEffect, useState } from "react";
import axios from "axios";

const QueryList = () => {
  const [queries, setQueries] = useState([]);

  useEffect(() => {
    const fetchQueries = async () => {
      try {
        const response = await axios.get("http://localhost:8000/query/userq/");
        setQueries(response.data);
      } catch (error) {
        // Handle error
      }
    };

    fetchQueries();
  }, []);

  return (
    <div className="bg-[#987656]">
      <h2>Queries</h2>
      <ul>
        {queries.map((query) => (
          <li key={query.id}>
            <strong>{query.title}</strong>
            <p>{query.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default QueryList;
