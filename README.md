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

## Build Instructions

`git clone https://github.com/s4ndhyac/lahacks-safeLA.git`

`cd flask`

`export FLASK_APP=main.py`

`FLASK_APP=main.py flask run`

`cd ../firebase-and-react`

`npm run start`

Now navigate to `http://localhost:3000` to see the app in action

## Future Work
- Adjust the hyperparameters of the neural network to improve the prediction accuracy
- Deploy the flask application to an application server such as Google AppEngine 
- Deploy the react application to Firebase


