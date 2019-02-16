import React from "react";
import camera from "../../assets/camera.svg";
import crescent from "../../assets/whiteCresecent.svg";

import "./ImageSelect.css";

export default () => (
  <div className="ImageSelect-root">
    <div className="ImageSelect-black">
      <div className="ImageSelect-text">
        <h1>Upload a Photo</h1>
        <h3>And create a song</h3>
      </div>
    </div>
    <img src={crescent} className="ImageSelect-crescent" alt="White Crescent" />
    <div className="ImageSelect-white">
      <button className="ImageSelect-button">
        <div className="ImageSelect-camera">
          <img className="ImageSelect-camera" src={camera} alt="Camera Icon" />
        </div>
        <p>Click to Upload </p>
      </button>
    </div>
  </div>
);
