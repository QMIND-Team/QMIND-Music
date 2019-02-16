import React, { Component } from "react";
import Header from "../Header/Header";
import Gallery from "../Gallery/Gallery";
import ImageSelect from "../ImageSelect/ImageSelect";

import "./App.css";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <ImageSelect />
        <Gallery />
      </div>
    );
  }
}

export default App;
