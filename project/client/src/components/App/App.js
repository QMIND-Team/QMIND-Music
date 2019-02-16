import React, { Component } from "react";
import Header from "../Header/Header";
import Gallery from "../Gallery/Gallery";
import ImageSelect from "../ImageSelect/ImageSelect";
import About from "../About/About";

import "./App.css";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <ImageSelect />
        <Gallery />
        <About />
      </div>
    );
  }
}

export default App;
