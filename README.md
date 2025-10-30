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

| Select parameters and model degree | Regression fit (training/testing points, curve) | Bias-Variance plot |
|:---:|:---:|:---:|
| ![<img width="926" height="410" alt="image" src="https://github.com/user-attachments/assets/68aaed45-0626-4e98-8cda-8039a551a396" />
]( ![<img width="910" height="691" alt="image" src="https://github.com/user-attachments/assets/e3dcac5b-31cc-4e3e-8ad3-08755c34a107" />
]( ![<img width="912" height="750" alt="image" src="https://github.com/user-attachments/assets/03082f48-f7f4-4815-b4bb-2f94f25b2380" />
](

***

## Usage

### Installation

Clone the repository:
```bash
git clone https://github.com/MrRedIsBack/Polynomial-Regression-Dashboard.git
cd polynomial-regression-dashboard
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
