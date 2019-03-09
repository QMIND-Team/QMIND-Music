import React from "react";
import spotify from "../../assets/spotify.jpg";
import network from "../../assets/network.png";
import "./About.css";

export default () => (
  <div className="About-root" id="about">
    <h1>About</h1>
    <div className="About-main">
      <div className="About-column">
        <img src={spotify} className="About-img" alt="Spotify" />
      </div>
      <div className="About-column About-p">
        <p>
          This website displays a project made by the 2019 QMIND Music Team. To
          learn more about QMIND <a href="http://qmind.ca">click here</a>. The
          project is the accumulation of hours of hard work planning, designing,
          and programming by Queen's Students. The goal was to create a neural
          network capable of generating a song from an image. We did this by
          compiling 30 second audio clips as well as cover artwork from Spotify
          for 100 songs across multiple genres.
        </p>
      </div>
      <div className="About-column About-p About-bottom-p">
        <p>
          After collecting our data sets, the team explored ways of converting
          the audio and images into useable formats for training. For audio, the
          melody was extracted from songs using the{" "}
          <a href="http://www.justinsalamon.com/melody-extraction.html">
            Melodia Algorithm
          </a>
          , and the result was turned into a MIDI file. For images, the{" "}
          <a href="https://www.doc.ic.ac.uk/~ajd/Publications/alcantarilla_etal_eccv2012.pdf">
            KAZE Algorithm
          </a>{" "}
          was used for feature extraction, specifically detecting edges and
          shapes within the album artwork. The image and music data was used to
          train an LSTM Neural Network (largely based on{" "}
          <a href="https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5">
            this article
          </a>
          ). When the trained network is fit with image data, the ouptut is then
          converted back into a .WAV file, check out the section{" "}
          <a href="#gallery">above</a> to see the results!
        </p>
      </div>
      <div className="About-column">
        <img src={network} className="About-img" alt="Network" />
      </div>
    </div>
    <div className="About-fineprint">Copyright © 2019 QMusic</div>
  </div>
);
