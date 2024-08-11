import React, { useState } from 'react';
import axios from 'axios';
import './NoiseCancellation.css'; // Import the CSS file

function NoiseCancellation() {
  const [audio, setAudio] = useState(null);
  const [buzzwords, setBuzzwords] = useState([]);

  const handleAudioChange = (e) => {
    setAudio(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('audio', audio);

    try {
      const response = await axios.post('http://localhost:8000/inspections/api/noise-cancellation/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setBuzzwords(response.data.buzzwords);
    } catch (error) {
      console.error('Error processing audio:', error);
    }
  };

  return (
    <div className="container">
      <h1>Noise Cancellation</h1>
      <input type="file" accept="audio/*" onChange={handleAudioChange} />
      <button onClick={handleUpload}>Upload and Process</button>
      <ul>
        {buzzwords.map((word, index) => (
          <li key={index}>{word}</li>
        ))}
      </ul>
    </div>
  );
}

export default NoiseCancellation;
