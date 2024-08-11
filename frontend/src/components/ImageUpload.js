import React, { useState } from 'react';
import axios from 'axios';

const ImageAugmentView = () => {
    const [image, setImage] = useState(null);
    const [enhancedImage, setEnhancedImage] = useState(null);

    const handleImageUpload = (event) => {
        setImage(event.target.files[0]);
    };

    const handleImageSubmit = async () => {
        const formData = new FormData();
        formData.append('image', image);

        try {
            const response = await axios.post('http://127.0.0.1:8000/inspections/api/image-augment/', formData, {
                responseType: 'blob' // Important for binary data
            });

            const url = URL.createObjectURL(response.data);
            setEnhancedImage(url);
        } catch (error) {
            console.error('Error uploading the image', error);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleImageUpload} />
            <button onClick={handleImageSubmit}>Enhance Image</button>
            {enhancedImage && <img src={enhancedImage} alt="Enhanced" />}
        </div>
    );
};

export default ImageAugmentView;
