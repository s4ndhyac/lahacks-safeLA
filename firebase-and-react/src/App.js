import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div class="pac-card" id="pac-card">
        <div>
          <div id="title">
            Autocomplete search
          </div>
          <div id="type-selector" class="pac-controls">
            <input type="radio" name="type" id="changetype-all" checked="checked">
              <label for="changetype-all">All</label>

              <input type="radio" name="type" id="changetype-establishment">
                <label for="changetype-establishment">Establishments</label>

                <input type="radio" name="type" id="changetype-address">
                  <label for="changetype-address">Addresses</label>

                  <input type="radio" name="type" id="changetype-geocode">
                    <label for="changetype-geocode">Geocodes</label>
          </div>
                  <div id="strict-bounds-selector" class="pac-controls">
                    <input type="checkbox" id="use-strict-bounds" value="">
                      <label for="use-strict-bounds">Strict Bounds</label>
          </div>
                  </div>
                  <div id="pac-container">
                    <input id="pac-input" type="text"
                      placeholder="Enter a location">
        </div>
                  </div>
                  <div id="map"></div>
                  <div id="infowindow-content">
                    <img src="" width="16" height="16" id="place-icon">
                      <span id="place-name" class="title"></span><br>
                        <span id="place-address"></span>
      </div>
                      );
                    }
                  }
                  
                  export default App;
