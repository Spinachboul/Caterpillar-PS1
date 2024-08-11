import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <div>
      <h1>Welcome to CAT Inspect</h1>
      <nav>
        <ul>
          <li><Link to="/about">About Us</Link></li>
          <li><Link to="/services">Services</Link></li>
          <li><Link to="/image-upload">Image Augmentation</Link></li>
          <li><Link to="/speech-to-text">Speech to Text</Link></li>
          <li><Link to="/noise-cancellation">Noise Cancellation</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default LandingPage;
