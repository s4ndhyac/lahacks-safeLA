import React, { Component } from 'react';
import './App.css';
import './Map.css';

class App extends Component {

  render() {
    return (
      <div className="pac-card" id="pac-card">
        <div>
          <div id="title">
            Autocomplete search
          </div>
          <br />
          <div id="pac-container">
            <input id="pac-input" type="text"
              placeholder="Enter a location"></input>
          </div>
          <div id="map"></div>
          <div id="infowindow-content"></div>
          <img src="" width="20" height="20" id="place-icon"></img>
          <span id="place-name" className="title"></span><br />
          <span id="place-address"></span>
        </div>
      </div>

    );
  }

};

export default App
