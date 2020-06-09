This project contains the code, data, and artifacts for the *Getting Started in Domino* Tutorial, found 
[here](https://docs.dominodatalab.com/en/4.1/get_started/index.html) for Python.

This tutorial will guide you through a common model lifecycle in Domino. 
You will start by working with data from the Balancing Mechanism Reporting Service in the UK. 
We will be exploring the Electricty Generation by Fuel Type and predicting the electricty generation in the future. 
You’ll see examples of Jupyter, Dash, pandas, and Prophet used in Domino.

Table of Contents:

* Forecast_Power_Generation.ipynb
* Scheduled_Forecast_Power_Generation.ipynb
* Forecast_Power_Generation_for_Launcher.ipynb
* forecast.ipynb
* forecast_predictor.py
* data.csv
* app.sh

To run the model API, be sure to set up an environment with the following code in the Dockerfile:

`RUN pip install "pystan==2.17.1.0" "plotly<4.0.0" papermill requests dash && pip install fbprophet==0.6`