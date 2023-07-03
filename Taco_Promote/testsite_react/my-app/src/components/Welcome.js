import React from 'react';
import { useNavigate } from 'react-router-dom';

const Welcome = () => {
  const navigate = useNavigate();

  const handleOnClick = () => {
    navigate('/home');
  };

  return (
    <div className="welcome" onClick={handleOnClick}>
      <h1>All Seeing EYE</h1>
    </div>
  );
};

export default Welcome;
