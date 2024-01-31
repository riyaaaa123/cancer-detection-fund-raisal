// app/hospitals/page.js
"use client";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import HospitalList from '../../components/HospitalList';

const HospitalsPage = () => {
  const [hospitals, setHospitals] = useState([]);

  useEffect(() => {
    const fetchHospitals = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/hospitals/');
        setHospitals(response.data);
      } catch (error) {
        console.error('Error fetching hospitals:', error);
      }
    };

    fetchHospitals();
  }, []);

  return (
    <div className='bg-[#987678] min-h-screen w-[100vw]'>
      <h1>List of Hospitals</h1>
      <HospitalList hospitals={hospitals} />
    </div>
  );
};

export default HospitalsPage;
