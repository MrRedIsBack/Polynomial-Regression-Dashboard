# Polynomial Regression Dashboard

## Overview

This interactive Streamlit dashboard demonstrates polynomial regression and bias-variance trade-off in a hands-on, visual way.  
You can explore how model complexity and regularization affect regression fits and generalization error, by adjusting:

- **Number of training data points**
- **Number of testing data points**
- **Degree of polynomial to display**
- **Ridge alpha (regularization strength)**

The dashboard fits a polynomial regression model to randomly generated training data, lets you preview different polynomial degrees, and plots both the regression fit and the bias/variance curve over a range of degrees.

***

## Features

- **Data selection:** Choose the sample size for training and testing sets.
- **Model degree slider:** View the fitted polynomial of your chosen degree instantly.
- **Ridge regularization:** Adjust regularization strength (alpha) for more robust fits.
- **Live model fit plot:** Shows training/testing points and the fitted polynomial curve.
- **Bias & variance analysis:** A separate plot displays bias and variance for polynomial degrees 2–100, helping you see the classic bias-variance trade-off.
- **Easy-to-use interface:** All controls available as Streamlit sliders.

***

## How It Works

1. **Generate training and testing data** — Simulates real-world noisy data for regression.
2. **Fit polynomial regression** — The curve you see adjusts live as you change degree or regularization.
3. **Bias & Variance Plot** — Separately computes mean squared error (bias) and prediction variance for polynomial degrees 2–100, regardless of the degree selected for the live fit.

***

## Demo Screenshots

<img width="934" height="491" alt="image" src="https://github.com/user-attachments/assets/12881bb2-b309-418f-967d-1d209aab88b2" />
<img width="937" height="699" alt="image" src="https://github.com/user-attachments/assets/0450650c-eabe-4e11-b0b6-6836cbbdb03e" />
<img width="910" height="755" alt="image" src="https://github.com/user-attachments/assets/07585483-03ea-41c7-8d2e-eb1dffbdef17" />

***

## Usage

### Installation

Clone the repository:
```bash
git clone https://github.com/MrRedIsBack/Polynomial-Regression-Dashboard.git
cd Polynomial-Regression-Dashboard
```
Install requirements:
```bash
pip install -r requirements.txt
```

### Run the app

Start the dashboard:
```bash
streamlit run main.py
```

***

## Customization

- **Polynomial degree slider** controls the regression fit displayed in the main plot.
- **Bias/variance plot** always uses full range of degrees; slider only affects fit display.
- **Ridge regularization value** lets you reduce model overfitting and instability for high-degree polynomials.

***
[8](https://github.com/Sven-Bo/streamlit-sales-dashboard)
[9](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/deploy-from-a-template)
[10](https://github.com/shamiraty/Streamlit-Dashboard-Descriptive-Analytics-with-MYSQL)
