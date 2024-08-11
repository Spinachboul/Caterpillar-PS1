import React, { useState } from 'react';
import { ReactMic } from 'react-mic';
import axios from 'axios';

const VoiceGuidedInspection = () => {
    const [record, setRecord] = useState(false);
    const [audioData, setAudioData] = useState(null);
    const [pdfUrl, setPdfUrl] = useState('');

    const startRecording = () => setRecord(true);
    const stopRecording = () => setRecord(false);

    const onData = (recordedBlob) => {
        setAudioData(recordedBlob);
    };

    const onStop = (recordedBlob) => {
        setAudioData(recordedBlob);
        uploadAudio(recordedBlob);
    };

    const uploadAudio = (recordedBlob) => {
        const formData = new FormData();
        formData.append('audio', recordedBlob.blob, 'audio.wav');

        axios.post('/speech-to-text-pdf/', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then(response => {
            setPdfUrl(response.data.pdf_url);
        })
        .catch(error => {
            console.error('Error uploading audio:', error);
        });
    };

    return (
        <div>
            <h2>Voice-Guided Inspection</h2>
            <ReactMic
                record={record}
                className="sound-wave"
                onStop={onStop}
                onData={onData}
                strokeColor="#000000"
                backgroundColor="#FF4081"
            />
            <button onClick={startRecording}>Start Recording</button>
            <button onClick={stopRecording}>Stop Recording</button>
            {pdfUrl && (
                <div>
                    <h3>Inspection Report:</h3>
                    <a href={pdfUrl} target="_blank" rel="noopener noreferrer">Download PDF</a>
                </div>
            )}
        </div>
    );
};

export default VoiceGuidedInspection;
