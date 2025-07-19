import datetime as dt
import requests


def get_1h_url(from_timestamp, to_timestamp, sym='23', res='1D'):
    url = "https://priceapi.moneycontrol.com/techCharts/history?symbol="+\
            sym+"&resolution="+res+"&from="+from_timestamp+"&to="+to_timestamp
    return url


def fetch_last_x_days_data(x=120, max=0):

    to_timestamp = str(int(dt.datetime.now().timestamp()))
    from_timestamp = str(int((dt.datetime.now()-dt.timedelta(x)).timestamp()))

    url = get_1h_url(from_timestamp, to_timestamp)
    print("Fetching data from URL:", url)
    r = requests.get(url)
    print("Response status code:", r.status_code)
    data = r.json()

    dataClose = data['c']
    dataTime = data['t']
    if max:
        dataClose = dataClose[-max:]
        dataTime = dataTime[-max:]

    return {
        'status': 'ok',
        'from_date': from_timestamp,
        'to_date': to_timestamp,
        'data': dataClose,
        'timestamp': dataTime
    }