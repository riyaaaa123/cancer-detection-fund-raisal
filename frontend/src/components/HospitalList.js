// components/HospitalList.js

import React from 'react';

const HospitalList = ({ hospitals }) => {
  return (
    <div>
      {hospitals.map((hospital) => (
        <div key={hospital.id}>
          <h2>{hospital.name}</h2>
          <p>Phone Number: {hospital.phone_number}</p>
          {/* You can add more details here */}
          {hospital.pdf && (
            <a href={hospital.pdf} target="_blank" rel="noopener noreferrer">
              Download PDF
            </a>
          )}
        </div>
      ))}
    </div>
  );
};

export default HospitalList;
