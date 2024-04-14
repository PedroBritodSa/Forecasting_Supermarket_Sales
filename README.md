

# Supermarket Sales Forecasting
This project aims to forecast sales for supermarkets using historical sales data. The dataset contains information about sales and CDI (Certificate of Deposit Interbank), and we aim to explore these features and them predict the sales.

## Getting Started
The dataset used in this project (VendasSupermercados+CDI.csv) contains historical sales data along with CDI information. The data is stored in a CSV format and contains only one column, which can be separeted in three:

Date: Date of the sales record
VendasSupermercados: Sales amount in supermarkets
CDI: Certificate of Deposit Interbank rate

## Data Preprocessing
The following steps were performed for data preprocessing:

Splitting the combined features in the dataset into separate columns.
Converting the Date column to datetime format and other features to numerical format.
Checking for missing values and outliers.
Exploratory Data Analysis (EDA) to understand the distribution of data.

## Training the Model
Three different machine learning models were trained for sales forecasting: Random Forest Regressor, XGBoost Regressor, and Decision Tree Regressor. The models were evaluated using Mean Absolute Percentage Error (MAPE) as the performance metric.

## Model Evaluation
The trained models were evaluated using two backtests to assess their performance. The Mean Absolute Percentage Error (MAPE) was calculated for each backtest to measure the accuracy of the predictions.

## Forecasting
The best performing model was used to forecast sales for the next 12 months. The forecasted sales data is provided along with the actual sales data for visualization.

## Deployment
The trained model is deployed using Streamlit, allowing users to make predictions for a specified number of months ahead. The deployment did work locally, but due problemns on the deployment using the Github repository and the Streamlit, we still working on the online version of the application.  

## Appendix: LSTM Implementation
An LSTM neural network was implemented to assess its performance on the dataset. However, due to the small size of the training data, the performance of the neural network model was poor.
