import React, { Component } from 'react';
import './App.css';
import './Map.css';

class App extends Component {

  render() {
    return (
      <div>
        <div class="column info">
          <center>
            <h1>Safe LA</h1>
            <h6>Find out how safe and affordable your area is</h6>
          </center>
          <hr />

          <h2><span class="a">Risk Level: </span><span class="b">10</span></h2>
          <div class="des">
            *Calculated from crime rate data in LA since 2018
            (1 being the safest and 10 being the most dangerous).
            </div>
          {/*<p id="safeLA"> </p> */}
          <br />
          <h2><span class="a">Median Rent Price: </span><span class="b">$1200</span></h2>
          <div class="des">
            *Calculated from housing data in the city of LA since 2010.
            </div>
          {/* <center><h1><p id="rentLA"> </p></h1></center> */}
          <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
        </div>

        <div class="column map">
          <div className="pac-card" id="pac-card">
            <div id="title">
              Search your next home
          </div>
            <br />

            <div className="card">

              <div className="card-body">
                <h4 className="card-title">Projected Rent</h4>
                <p className="card-text">
                  Find out your projected rent based on housing data from the city of LA from 2010 onwards.
    </p>
                <br />
                <p id="rentLA"> </p>

              </div>
            </div>


            <br /><br /><br /><br /><br /><br /><br /><br />

            <div className="card">

              <div className="card-body">
                <h4 className="card-title">Safety Score</h4>
                <p className="card-text">
                  Find a affordable and safe neighbourhood based on our neural network prediction using data from the city of LA.
    </p>
                <br />
                <p id="safeLA"> </p>

              </div>
            </div>

          </div>
          <div className="pac-card" id="pac-card">
            <div>
              <div id="title">
                Search your next home
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

            <div id="map"></div>
            <div id="infowindow-content"></div>
            <img src="" width="20" height="20" id="place-icon"></img>
            <span id="place-name" className="title"></span><br />
            <span id="place-address"></span>

          </div>
        </div>
      </div>
    );
  }

};

export default App
