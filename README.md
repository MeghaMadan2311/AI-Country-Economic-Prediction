# AI Powered Country Economic Prediction System

## Project Overview

This project predicts country GDP growth using economic indicators such as inflation and unemployment.

## Features

- Country-specific GDP prediction
- Predictions for all available countries
- Automated data ingestion
- Machine learning model
- Baseline model comparison
- Exploratory Data Analysis (EDA)
- API unit tests
- Model unit tests
- Logging
- Performance measurement
- Docker support

## API

### Get API status

GET `/`

### Predict for a specific country

GET `/predict?country=India`

### Predict for all countries

GET `/predict`

## Data

The project uses economic data containing:

- Country
- GDP Growth
- Inflation
- Unemployment

## Machine Learning

A Linear Regression model is used to predict GDP growth.

The machine learning model is compared with a simple baseline model.

## Testing

Unit tests are provided for:

- API
- Machine learning model
- Logging

All tests can be executed using:

```bash
python run_tests.py
