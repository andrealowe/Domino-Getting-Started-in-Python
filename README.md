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

Before using this project in a training, follow the steps below:
(Note you will need Admin access for the following)

* Check that the `com.cerebro.domino.builder.job.environment.buildMemory` central config is set to `4294967294` (a requirement for PyStan). 

* Then create environment with this base image: quay.io/domino/base:Ubuntu18_DAD_Py3.6_R3.6_20190918 and the following dockerfile instructions:

`RUN pip install "pystan==2.17.1.0" "plotly<4.0.0" requests && pip install fbprophet==0.6`
`RUN pip install --upgrade nbclient nbconvert`
`RUN pip install papermill`

* Set the `ShortLived.iFrameSecurityEnabled` to `false` (this is so that the Dash app plot can render).

* Publish the app, create a model API, launcher, and scheduled job to test functionality. 

* The app in this file is compatible with dash < 2.0.0. Ensure you install the following version of dash:
`RUN pip install dash==1.20.0 dash-core-components==1.16.0 dash-html-components==1.1.3 dash-renderer==1.9.1 dash-table==4.11.3`
