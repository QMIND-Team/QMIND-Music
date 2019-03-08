import React from "react";
import logo from "../../assets/logo.png";

import "./Header.css";

export default () => (
  <header className="Header-root">
    <div className="Header-content">
      <div className="Header-left" align="left">
        <img
          src={logo}
          className="Header-logo"
          height="50px"
          alt="QMUSIC LOGO"
        />
      </div>
      <div className="Header-right" align="right">
        <a href="./">HOME</a>
        <a href="#gallery">GALLERY</a>
        <a href="#about">ABOUT</a>
      </div>
    </div>
  </header>
);
