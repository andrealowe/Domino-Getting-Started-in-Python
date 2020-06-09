#wrapper file to execute notebook
papermill Forecast_Power_Generation_for_Launcher.ipynb forecast.ipynb -p start_date "$1" -p fuel_type $2