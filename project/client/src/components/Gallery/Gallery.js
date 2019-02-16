import React, { Component } from "react";
import "./Gallery.css";

class Gallery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      photos: Array(12).fill({})
    };
  }

  render() {
    return (
      <div className="Gallery-root">
        <h1>Gallery</h1>
        <div className="Gallery-photos">
          {this.state.photos.map(photo => (
            <div className="Gallery-placeholder" />
          ))}
        </div>
      </div>
    );
  }
}

export default Gallery;
