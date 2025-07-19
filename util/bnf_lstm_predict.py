from keras.models import load_model
import joblib
import pandas as pd
import numpy as np 
import datetime as dt
import requests


FEED_DAYS = 50
model = load_model("model/lstm_bnf_model.h5")
scaler = joblib.load('model/scaler.gz')


def get_1h_url(sym='23', res='1D', days= FEED_DAYS):
    t_to = str(int(dt.datetime.now().timestamp()))
    t_from = str(int((dt.datetime.now()-dt.timedelta(FEED_DAYS)).timestamp()))
    url = "https://priceapi.moneycontrol.com/techCharts/history?symbol="+\
            sym+"&resolution="+res+"&from="+t_from+"&to="+t_to
    return url

def get_bnf_data():
    r = requests.get(get_1h_url())
    data = r.json()
    df = pd.DataFrame(data)
    def convert_to_date(tsmp):
        return dt.datetime.fromtimestamp(tsmp)

    df['t'] = df['t'].apply(convert_to_date)
    df.sort_values(['t'], inplace=True, ascending=False)
    df.drop(['s','t','o','l','h','v'], axis=1, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def create_dataset(dataset, look_back):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)

def get_direction(x, col1, col2):
    if x[col1] - x[col2] > 0:
        return x[col1] - x[col2], "UP"
    elif x[col1] - x[col2] < 0:
        return x[col1] - x[col2], "DOWN"
    else:
        return 0, "NEUTRAL"


def main():
    print()
    print("Fetching Banknifty data...")
    print()
    bnf = get_bnf_data()
    bnf = bnf.iloc[::-1]
    # test data
    time_steps = 20

    test_data = bnf['c'].values
    test_data = test_data.reshape(-1,1)
    test_data = scaler.transform(test_data)

    # Create the data to test our model on:
    X_test, y_test = create_dataset(test_data, time_steps)

    # store the original vals for plotting the predictions 
    y_test = y_test.reshape(-1,1)
    org_y = scaler.inverse_transform(y_test)

    # reshape it [samples, time steps, features]
    X_test = np.reshape(X_test, (X_test.shape[0], time_steps, 1))

    # Predict the prices with the model
    predicted_y = model.predict(X_test)

    predicted_y = scaler.inverse_transform(predicted_y)
    test_data = scaler.inverse_transform(test_data)


    res = pd.DataFrame(org_y, columns=['Input'])
    res['Prediction'] = pd.Series(predicted_y.ravel())

    res['prev_pred'] = res['Prediction'].shift(1)
    res['prev_close'] = res['Input'].shift(1)

    res[['pred_Diff','pred_Direction']] = \
    res.apply(lambda x: get_direction(x,'Prediction','prev_pred'), axis=1, result_type='expand')

    res[['Actual_Diff','Actual_Direction']] = \
        res.apply(lambda x: get_direction(x,'Input','prev_close'), axis=1, result_type='expand')

    res[['Input','prev_close', 'Actual_Diff', 'Actual_Direction', 'Prediction', 'prev_pred', 'pred_Diff', 'pred_Direction']]
    print()
    print("-"*100)
    print("Prediction details")
    print(res.iloc[-1,:])
    print("-"*100)
    print()


if __name__ == "__main__":
    main()