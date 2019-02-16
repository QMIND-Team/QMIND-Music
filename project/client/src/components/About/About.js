import React from "react";
import spotify from "../../assets/spotify.jpg";
import network from "../../assets/network.png";
import "./About.css";

export default () => (
  <div className="About-root">
    <h1>About</h1>
    <div className="About-main">
      <div className="About-column">
        <img src={spotify} className="About-img" alt="Spotify" />
      </div>
      <div className="About-column About-p">
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus
          quidem, rem vero rerum repudiandae dolore, perferendis nobis
          aspernatur ipsum, odit neque adipisci laborum autem assumenda sint
          consequatur quod eum? Odio doloremque adipisci fugiat consectetur iste
          fugit obcaecati magni aliquid cumque voluptates alias dignissimos
          sequi nam repellendus consequatur, quo quae laborum?
        </p>
      </div>
      <div className="About-column About-p About-bottom-p">
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus
          quidem, rem vero rerum repudiandae dolore, perferendis nobis
          aspernatur ipsum, odit neque adipisci laborum autem assumenda sint
          consequatur quod eum? Odio doloremque adipisci fugiat consectetur iste
          fugit obcaecati magni aliquid cumque voluptates alias dignissimos
          sequi nam repellendus consequatur, quo quae laborum?
        </p>
      </div>
      <div className="About-column">
        <img src={network} className="About-img" alt="Network" />
      </div>
    </div>
    <div className="About-fineprint">Copyright © 2019 QMusic</div>
  </div>
);
