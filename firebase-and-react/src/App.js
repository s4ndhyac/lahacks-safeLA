
import React, { Component } from 'react';
import './App.css';
import './Map.css';

class App extends Component {

  render() {
    return (
      <div>
        <div className="column info">
          <center>
            <h1>Safe LA</h1>
            <h6>Find out how safe and affordable your area is</h6>
          </center>
          <hr />

          <h2><span className="a">Risk Level: </span><span id="safeLA" className="b">-</span></h2>
          <div className="des">
            *Calculated from crime rate data in LA since 2018
            (1 being the safest and 10 being the most dangerous).
            </div>

          <br /><br /><br /><br />
          <h2><span className="a">Median Rent Price: </span><span id="rentLA" className="b">$</span></h2>
          <div className="des">
            *Calculated from housing data in the city of LA since 2010.
            </div>

          <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
          <br /><br /><br /><br /><br /><br /><br />

        </div>
        <div className="column right">
          <div className="pac-card" id="pac-card">
            <div>
              <div id="title">
                Search for your next home
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
        </div>


      </div >
    );
  }

};

export default App
