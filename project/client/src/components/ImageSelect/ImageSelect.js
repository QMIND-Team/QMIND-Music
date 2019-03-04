import React, { Component } from "react";
import axios from "axios";
import camera from "../../assets/camera.svg";
import crescent from "../../assets/whiteCresecent.svg";

import "./ImageSelect.css";

const SERVER_URL =
  process.env.NODE_ENV === "development" ? "http://localhost:4000" : "";

function onInputChange(e) {
  if (!e.target.files[0]) return;

  const imageUrl = URL.createObjectURL(e.target.files[0]);
  const imageFile = e.target.files[0];
  this.setState({ imageUrl, imageFile });
}

function onCreateSong(e) {
  const data = new FormData();
  data.append("image", this.state.imageFile);
  axios({
    method: "POST",
    url: `${SERVER_URL}/song`,
    data
  }).then(res => {
    console.log(res);
  });
}

function displayImage(url, obj) {
  return (
    <div className="ImageSelect-camera">
      <img
        className="ImageSelect-camera"
        src={url || camera}
        alt="Camera Icon"
      />

      {url ? (
        <div className="ImageSelect-btn-container">
          <button
            className="ImageSelect-create-song"
            onClick={onCreateSong.bind(obj)}
          >
            Create A Song
          </button>
        </div>
      ) : (
        <p className="ImageSelect-p">Click to Upload</p>
      )}
    </div>
  );
}

class ImageSelect extends Component {
  constructor(props) {
    super(props);
    this.state = { imageUrl: null, imageFile: null };
  }

  render() {
    return (
      <div className="ImageSelect-root">
        <div className="ImageSelect-black">
          <div className="ImageSelect-text">
            <h1>Upload a Photo</h1>
            <h3>And create a song</h3>
          </div>
        </div>
        <img
          src={crescent}
          className="ImageSelect-crescent"
          alt="White Crescent"
        />
        <div className="ImageSelect-white">
          <button className="ImageSelect-button">
            <label for="image-upload">
              {displayImage(this.state.imageUrl, this)}
            </label>
          </button>
          <input
            id="image-upload"
            className="ImageSelect-input"
            type="file"
            accept="image/*"
            onChange={onInputChange.bind(this)}
          />
        </div>
      </div>
    );
  }
}

export default ImageSelect;
