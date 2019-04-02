# SaferLA

## About
With rising crime rates and the ever-increasing housing prices in Los Angeles, it is getting more difficult to find a safe and affordable place to stay in LA. SaferLA helps people find out how safe a neighbourhood in LA is and also how much it would cost to live there.

## Architecture
There are 3 componenets to the application:
- At the core are the 2 neural networks that predict the rent at the given location and generate a safety score for the location.
    - A classification model is used to generate a safety score
    - A regression model is used to predict the rent of a house at the place
- We use the Flask framework to create APIs to output the result of the neural networks
- At the top is the react firebase application that comprises the user interface
- The dataset used was from the lacity open data and the USC socrata dataset:
    - https://data.lacity.org/A-Safe-City/Crime-Data-from-2010-to-Present/y8tr-7khq/data
    - https://usc.data.socrata.com/widgets/4a97-v5tx

## Build Instructions

`git clone https://github.com/s4ndhyac/lahacks-safeLA.git`

`cd flask`

`export FLASK_APP=main.py`

`FLASK_APP=main.py flask run`

`cd ../firebase-and-react`

`npm run start`

Now navigate to `http://localhost:3000` to see the app in action

NOTE: Also ensure that CORS is enabled on your browser. An easy hacky way is to install the chrome extension Allow-Control-Allow-Origin: *


## Future Work
- Adjust the hyperparameters of the neural network to improve the prediction accuracy
- Deploy the flask application to an application server such as Google AppEngine 
- Deploy the react application to Firebase
- Enable CORS in the application itself


