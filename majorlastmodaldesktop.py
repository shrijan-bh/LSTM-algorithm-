# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 19:25:51 2024

@author: lenovo
"""

# ai modal completed

import os
import pandas as pd
import numpy as np
import math
import datetime as dt
import sklearn

# For Evalution we will use these library

from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score
from sklearn.metrics import mean_poisson_deviance, mean_gamma_deviance, accuracy_score
from sklearn.preprocessing import MinMaxScaler

# For model building we will use these library

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

# For Plotting we will use these library

import matplotlib.pyplot as plt
from itertools import cycle

df = pd.read_csv('C:/Users/lenovo/Downloads/kalimati/dataset/Potato_Red.csv')

closedf = df[['sn', 'price']]

training_size = int(len(closedf) * 0.70)
test_size = len(closedf) - training_size

# Use iloc for selecting specific rows
train_data = closedf.iloc[:training_size]
test_data = closedf.iloc[training_size:]

def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - time_step - 1):
        a = dataset.iloc[i:(i + time_step), 1].values
        dataX.append(a)
        dataY.append(dataset.iloc[i + time_step, 1])
    return np.array(dataX), np.array(dataY)

time_step = 30
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

model = Sequential()
model.add(LSTM(128, input_shape=(None, 1), activation="relu"))
model.add(Dense(1))
model.compile(loss="mean_squared_error", optimizer="adam")

# Early stopping and model checking

# Early Stopping
earlystop = EarlyStopping(
    monitor="val_loss",  # value being monitored for improvement
    min_delta=0.001,  # Abs value and is the main change required before we stop
    mode="auto",
    patience=6,  # no of epochs we wait before stopping
    verbose=1,
    restore_best_weights=True,  # keep the best weights once stopped
)

# Model Checkpoint
checkpoint = ModelCheckpoint(
    monitor="val_loss",
    mode="auto",
    filepath="C:/Users/lenovo/Desktop/major/potatomodel",
    verbose=1,
    save_best_only=True,
)

# Reduce learning Rate
reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.01,
    patience=6,
    verbose=1,
    min_delta=0.001,
)

# we put our callbacks into a callback list
callback = [earlystop, checkpoint, reduce_lr]

train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Replace these lines
# train_predict = 'scaler.inverse_transform(train_predict)'
# test_predict = 'scaler.inverse_transform(test_predict)'
# original_ytrain = 'scaler.inverse_transform(y_train.reshape(-1,1))'
# original_ytest = 'scaler.inverse_transform(y_test.reshape(-1,1))'

scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(train_data[['price']].values)  # Fit the scaler with the training data

train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)
original_ytrain = scaler.inverse_transform(y_train.reshape(-1, 1))
original_ytest = scaler.inverse_transform(y_test.reshape(-1, 1))

# notgpt


import seaborn as sns

look_back=time_step
trainPredictPlot = np.empty_like(closedf)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict
print("Train predicted data: ", trainPredictPlot.shape)

# shift test predictions for plotting
testPredictPlot = np.empty_like(closedf)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(train_predict)+(look_back*2)+1:len(closedf)-1, :] = test_predict
print("Test predicted data: ", testPredictPlot.shape)

x_input = test_data['price'].values[len(test_data) - time_step:].reshape(1, -1)
temp_input = list(x_input)
temp_input = temp_input[0].tolist()

from numpy import array

lst_output=[]
n_steps=time_step
i=0
pred_days = 30    # Prediction for next 30 days

while(i<pred_days):

    if(len(temp_input)>time_step):

        x_input=np.array(temp_input[1:])
        #print("{} day input {}".format(i,x_input))
        x_input = x_input.reshape(1,-1)
        x_input = x_input.reshape((1, n_steps, 1))

        yhat = model.predict(x_input, verbose=0)
        #print("{} day output {}".format(i,yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input=temp_input[1:]
        #print(temp_input)

        lst_output.extend(yhat.tolist())
        i=i+1

    else:

        x_input = x_input.reshape((1, n_steps,1))
        yhat = model.predict(x_input, verbose=0)
        temp_input.extend(yhat[0].tolist())

        lst_output.extend(yhat.tolist())
        i=i+1

print("Output of predicted next days: ", len(lst_output))

last_days=np.arange(1,time_step+1)
day_pred=np.arange(time_step+1,time_step+pred_days+1)

temp_mat = np.empty((len(last_days)+pred_days+1,1))
temp_mat[:] = np.nan
temp_mat = temp_mat.reshape(1,-1).tolist()[0]

last_original_days_value = temp_mat
next_predicted_days_value = temp_mat

last_original_days_value[0:time_step+1] = scaler.inverse_transform(closedf[len(closedf)-time_step:]).reshape(1,-1).tolist()[0]
next_predicted_days_value[time_step+1:] = scaler.inverse_transform(np.array(lst_output).reshape(-1,1)).reshape(1,-1).tolist()[0]

new_pred_plot = pd.DataFrame({
    'last_original_days_value':last_original_days_value,
    'next_predicted_days_value':next_predicted_days_value
})


# Assuming lstmdf is a NumPy array with the 'price' column
lstmdf = closedf['price'].values.reshape(-1, 1)

# Extend lstmdf with lst_output
lstmdf_extended = np.vstack([lstmdf, np.array(lst_output).reshape(-1, 1)])

# Inverse transform using the scaler
lstmdf_inverse = scaler.inverse_transform(lstmdf_extended)

# Convert back to a list
lstmdf_inverse_list = lstmdf_inverse.flatten().tolist()


output=(next_predicted_days_value[:30])
print(output)

