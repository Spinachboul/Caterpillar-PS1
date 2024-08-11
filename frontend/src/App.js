import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import AboutUs from './components/AboutUs';
import Services from './components/Services';
import ImageUpload from './components/ImageUpload';
import SpeechToText from './components/SpeechToText';
import NoiseCancellation from './components/NoiseCancellation';
import VoiceGuidedInspection from './components/VoiceGuidedInspection';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/services" element={<Services />} />
        <Route path="/image-upload" element={<ImageUpload />} />
        <Route path="/speech-to-text" element={<SpeechToText />} />
        <Route path="/noise-cancellation" element={<NoiseCancellation />} />
        <Route path="/voice-guided-inspection" element={<VoiceGuidedInspection />} />
      </Routes>
    </Router>
  );
}

export default App;
