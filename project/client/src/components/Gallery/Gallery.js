import React, { Component } from "react";
import axios from "axios";

import "./Gallery.css";

const SERVER_URL =
  process.env.NODE_ENV === "development" ? "http://localhost:4000" : "";

class Gallery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      photos: Array(12).fill({}),
      loading: true
    };
  }

  componentDidMount() {
    axios.get(`${SERVER_URL}/gallery`).then(({ data }) => {
      const photos = data;
      if (photos.length < 12) {
        photos.push(...Array(12 - photos.length).fill({}));
      }
      this.setState({ photos, loading: false });
    });
  }

  render() {
    return (
      <div className="Gallery-root" id="gallery">
        <h1>Gallery</h1>
        <div className="Gallery-photos">
          {this.state.photos.map(({ image, song }) =>
            image && song ? (
              <div>
                <img src={image} alt={image} className="Gallery-image" />
                <audio
                  src={song}
                  controls
                  playsInlLne
                  name="media"
                  className="Gallery-audio"
                />
              </div>
            ) : (
              <div
                className={`Gallery-placeholder ${
                  this.state.loading ? "loading" : ""
                }`}
              />
            )
          )}
        </div>
      </div>
    );
  }
}

export default Gallery;
