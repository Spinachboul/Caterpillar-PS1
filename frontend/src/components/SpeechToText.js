import React, { useState } from 'react';
import axios from 'axios';

function SpeechToText() {
  const [audio, setAudio] = useState(null);
  const [text, setText] = useState('');
  const [error, setError] = useState('');

  const handleAudioChange = (e) => {
    setAudio(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!audio) {
      setError('Please upload an audio file.');
      return;
    }

    const formData = new FormData();
    formData.append('audio', audio);

    try {
      const response = await axios.post('http://localhost:8000/inspections/api/speech-to-text/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setText(response.data.results);  // Adjust if needed
    } catch (error) {
      setError('Error processing audio');
      console.error('Error processing audio:', error);
    }
  };

  return (
    <div>
      <h1>Speech to Text</h1>
      <input type="file" accept="audio/*" onChange={handleAudioChange} />
      <button onClick={handleUpload}>Upload and Convert</button>
      {text && <p>Extracted Text: {text}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default SpeechToText;
