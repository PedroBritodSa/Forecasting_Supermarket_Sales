from datetime import datetime, timedelta
import joblib
import pandas as pd

#load the linear regression model
trends = joblib.load("trends.sav")

final_date_str = '2023-08-01 00:00:00'

final_date = pd.to_datetime(final_date_str)

def feat_eng_data(months):

   # let the months as variable for the user
     forecast_period = final_date + pd.DateOffset(months=months)

     forecast_dates = pd.date_range(start=final_date + pd.DateOffset(days=1), end=forecast_period, freq='MS')

   # Extracting the year and month 
     forecast_years = forecast_dates.year
     forecast_months = forecast_dates.month

   # Using the linear regression model to predict the trend for the new dates
     forecast_trends = trends.predict(pd.to_numeric(forecast_dates).values.reshape(-1, 1))

   # Creating the X_forecasting DataFrame
     X_fct = pd.DataFrame({
        'year': forecast_years,
        'month': forecast_months,
        'Trend': forecast_trends
    })
     return X_fct