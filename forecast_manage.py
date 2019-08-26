import time
import pandas as pd
from datetime import date, timedelta
import schedule
from utilities import get_conf
from processing_data import pdata, time_unix, str_time, split_fun_time, conver_unix
from prophet import Forecast


def drivers_spb():
    print('table drivers')
    path = 'setting/forecast/drivers_spb_setting.ini'
    columns = [1, 2, 5, 7, 8, 16, 28]
    name_column = 'column_id'
    send_drivers(path, columns, name_column)


def drivers_msc():
    print('table drivers')
    path = 'setting/forecast/drivers_msc_setting.ini'
    columns = [9, 10, 12, 21, 25, 26, 27, 29, 33, 40]
    name_column = 'column_id'
    send_drivers(path, columns, name_column)


def orders_msc():
    print('table orders')
    path = 'setting/forecast/orders_msc_setting.ini'
    send_data_orders(path, city_id=2)


def orders_spb():
    print('table orders')
    path = 'setting/forecast/orders_spb_setting.ini'
    send_data_orders(path, city_id=1)


def closed_orders_msc():
    print('table closed_orders')
    path = 'setting/forecast/closed_orders_msc_setting.ini'
    send_data_orders(path, city_id=2)


def closed_orders_spb():
    print('table closed_orders')
    path = 'setting/forecast/closed_orders_spb_setting.ini'
    send_data_orders(path, city_id=1)


def free_drivers_spb():
    print('table free_drivers')
    path = 'setting/forecast/free_drivers_spb_setting.ini'
    id_cars = pd.read_csv('data/csv/car_id_spb.csv')
    status = pd.read_csv('data/csv/status.csv')
    send_free_drivers(path, id_cars['car_id'], status['status'])


def free_drivers_msc():
    print('table free_drivers')
    path = 'setting/forecast/free_drivers_msc_setting.ini'
    id_cars = pd.read_csv('data/csv/car_id_msc.csv')
    status = pd.read_csv('data/csv/status.csv')
    send_free_drivers(path, id_cars['car_id'], status['status'])


def send_free_drivers(path, id_cars, status):
    confile = get_conf(path)
    column = confile["Data_file"]["column"]
    begin = confile["Period"]["begin"]
    end = yesterday()
    train = int(confile["Prophet"]["train"])
    prediction = int(confile["Prophet"]["prediction"])
    frequency = confile["Prophet"]["frequency"]
    output = confile["Output"]["name"]
    df = pd.read_csv(confile["Data_file"]["data"])
    df = list(map(lambda x: df[df['car_id'] == x], id_cars))
    data = pd.concat(df)
    data = list(map(lambda x: data[data['status_sub'] == x], status))
    data = pd.concat(data)
    f = Forecast(
        data,
        column,
        begin,
        end,
        train,
        prediction,
        frequency,
        output
    ).get_forecast()


def send_data_orders(path, city_id):
    confile = get_conf(path)
    column = confile["Data_file"]["column"]
    begin = confile["Period"]["begin"]
    end = yesterday()
    train = int(confile["Prophet"]["train"])
    prediction = int(confile["Prophet"]["prediction"])
    frequency = confile["Prophet"]["frequency"]
    output = confile["Output"]["name"]

    df = pd.read_csv(confile["Data_file"]["data"])
    data = df[((df['city_id'] == city_id) & (df['status'] == 'DONE')) |
              ((df['city_id'] == city_id) & (df['status'] == 'CANCEL'))]
    f = Forecast(
        data,
        column,
        begin,
        end,
        train,
        prediction,
        frequency,
        output
    ).get_forecast()


def send_drivers(path, columns, name_column):
    confile = get_conf(path)
    column = confile["Data_file"]["column"]
    begin = confile["Period"]["begin"]
    end = yesterday()
    train = int(confile["Prophet"]["train"])
    prediction = int(confile["Prophet"]["prediction"])
    frequency = confile["Prophet"]["frequency"]
    output = confile["Output"]["name"]
    df = pd.read_csv(confile["Data_file"]["data"])
    df = list(map(lambda x: df[df[name_column] == x], columns))
    data = pd.concat(df)
    dftime = data['time'].apply(lambda x: split_fun_time(x))
    dfdate = data['date'].apply(lambda x: time_unix(x).split(' ')[0])
    all_date = dfdate + ' ' + dftime
    all_date = all_date.apply(lambda x: str_time(x))
    all_date = all_date.apply(lambda x: conver_unix(x))
    data = pd.DataFrame(data=all_date, columns=[column])
    f = Forecast(
        data,
        column,
        begin,
        end,
        train,
        prediction,
        frequency,
        output
    ).get_forecast()


def yesterday():
    return date.today().strftime('%Y-%m-%d %H')


def main():
    drivers_spb()
    drivers_msc()
    time.sleep(1)
    orders_msc()
    orders_spb()
    time.sleep(1)
    closed_orders_msc()
    closed_orders_spb()
    free_drivers_spb()
    free_drivers_msc()


if __name__ == '__main__':
    main()
