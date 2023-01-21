import requests
import pandas as pd

def request_daily_time_series(start_date, end_date, symbol):
    requestParams = {'start_date': start_date, 'end_date': end_date, 'symbol': symbol, 'interval': '1day', 'apikey': '565663eb5ded412cbbdbe5ef49f0997b'}
    try:
        response = requests.get("https://api.twelvedata.com/time_series", params=requestParams, timeout=15)
        response.raise_for_status()
        response_data = response.json()
        stockData = pd.DataFrame(response_data['values'])
        stockData.drop(columns='volume', inplace=True, errors='ignore', axis=1)
        stockData['datetime'] = pd.to_datetime(stockData['datetime'], format='%Y-%m-%d')
        stockData['open'] = pd.to_numeric(stockData['open'])
        stockData['high'] = pd.to_numeric(stockData['high'])
        stockData['low'] = pd.to_numeric(stockData['low'])
        stockData['close'] = pd.to_numeric(stockData['close'])
        stockData.set_index('datetime', inplace=True, drop=True)
        return stockData[::-1]
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error: " + http_err)
        raise Exception('Server error')
    except requests.exceptions.ConnectionError as con_err:
        print("Connection error: " + con_err)
        raise Exception('Server error')
    except requests.exceptions.Timeout as timeout_errt:
        print("Timeout error: " + timeout_errt)
        raise Exception('Server error')
    except requests.exceptions.RequestException as request_err:
        print("Request error: " + request_err)
        raise Exception('Server error')
    except:
        print("Sever error")
        raise Exception('Server error')
        