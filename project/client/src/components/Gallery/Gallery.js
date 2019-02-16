import React, { Component } from "react";
import "./Gallery.css";

class Gallery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      photos: []
    };
  }

  render() {
    return (
      <div className="Gallery-root">
        <h1>Gallery</h1>
      </div>
    );
  }
}

export default Gallery;
