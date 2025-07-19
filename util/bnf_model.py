import pickle

import numpy as np
import tensorflow as tf

MODEL_FILEPATH = 'model/lstm_bnf_model_v2.h5'
SCALER_FILEPATH = 'model/MinMaxScaler_v2.pkl'

print(f"Running tensorflow version : {tf.__version__}")

model = tf.keras.models.load_model(
    MODEL_FILEPATH, custom_objects=None, compile=True, options=None
)
scaler = pickle.load(open(SCALER_FILEPATH, 'rb'))


def predict(input_data:list, lag=60)->float:

    if len(input_data) != lag:
        raise ValueError(f"Require past {lag} days of data to predict using this model")

    prevClose = input_data[-1]
    data = np.array(input_data).reshape(-1,1)
    scaled_input = scaler.fit_transform(data)
    reshaped_input = scaled_input.reshape(1,lag,1)
    
    pred = model.predict(reshaped_input)
    pred = scaler.inverse_transform(pred)
    predValue = pred.tolist()[0][0]

    direction = 'Bearish'
    if prevClose - predValue < 0:
        direction = 'Bullish'

    return {
        'status': 'ok',
        'pred': predValue,
        'prevClose': prevClose,
        'direction': direction
    }
