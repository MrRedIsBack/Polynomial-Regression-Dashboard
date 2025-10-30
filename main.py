import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from random import *

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline

#Generate some sample data
def generate_data(n):
    domain = 20 #Domain of x values that we will use, the lower limit is always 0
    x_values = [random()*domain for _ in range(n)]
    y_values = [0.1*(x**2) - 2*x + 15 + randrange(-2, 2) for x in x_values]
    return np.array(x_values), np.array(y_values)

#Fit polynomial regression with scaling and regularization for stability
def fit_model(x_values, y_values, degree, ridge_value):
    #Scale x for stable polynomial fitting
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x_values.reshape(-1, 1))
    model = make_pipeline(PolynomialFeatures(degree, include_bias = True), Ridge(alpha = ridge_value))
    model.fit(x_scaled, y_values)
    return model, scaler

#Predict using the fitted model
def predict_y(model, scaler, x):
    x_scaled = scaler.transform(np.array(x).reshape(-1, 1))
    return model.predict(x_scaled)

#Plot training, testing, and model fit
def plot_data(training_data_n, testing_data_n, polynomial_degree, ridge_value):
    #Generate some data that we can use for training and testing
    train_x, train_y = generate_data(training_data_n)
    test_x, test_y = generate_data(testing_data_n)

    #Predict y values based on the model which uses train_x and train_y
    model, scaler = fit_model(train_x, train_y, polynomial_degree, ridge_value)
    uniform_x = np.linspace(0, 20, 200)
    pred_y = predict_y(model, scaler, uniform_x)
    
    #Plot our graph
    fig, ax = plt.subplots()
    ax.scatter(train_x, train_y, label="Training Data")
    ax.scatter(test_x, test_y, label="Testing Data")
    ax.plot(uniform_x, pred_y, color="red", label=f"Predicted Polynomial of degree {polynomial_degree}")
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.legend()
    plt.title("A plot of our training data and testing data")
    st.pyplot(fig)

    return test_x, test_y, train_x, train_y

#Calculate the errors so that we can plot them
def find_errors(test_x, test_y, train_x, train_y):
    list_of_biases = []
    list_of_variances = []

    for i in range(2, 101):
        model, scaler = fit_model(train_x, train_y, i, ridge_value)
        predicted_y = predict_y(model, scaler, test_x)

        # True bias^2 (test MSE)
        bias2 = np.mean((predicted_y - test_y) ** 2)
        list_of_biases.append(bias2)

        # Model prediction variance for single fit (should be 0 for deterministic fit)
        var_preds = np.var(predicted_y)
        list_of_variances.append(var_preds)

    return list_of_biases, list_of_variances

#Plot the errors that we calculated
def plot_error(list_of_biases, list_of_variances):
    uniform_n_values = np.arange(2, 101).tolist() #For the x-axis
    fig, ax = plt.subplots()
    ax.plot(uniform_n_values, list_of_biases, label="Bias (Test MSE)")
    ax.plot(uniform_n_values, list_of_variances, label="Variance")
    plt.xlim(0, 101)
    plt.legend()
    plt.xlabel("Degree of polynomial")
    plt.title("Different errors as the degree of polynomial increases")
    st.pyplot(fig)

#Visually display sliders and buttons for all the parameters
st.title("Select the parameters:")

train_n = st.slider("Number of training data points:", 3, 1000)
test_n = st.slider("Number of testing data points:", 3, 1000)   
polynomial_degree = st.slider("Polynomial degree to display:", 2, 100)
ridge_value = st.slider("Ridge Value", 0.0, 5.0, step = 0.1)

test_x_coordinates, test_y_coordinates, train_x_coordinates, train_y_coordinates = plot_data(train_n, test_n, polynomial_degree, ridge_value)
bias, variance = find_errors(test_x_coordinates, test_y_coordinates, train_x_coordinates, train_y_coordinates)
plot_error(bias, variance)