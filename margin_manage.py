import pandas as pd
from datetime import datetime, date, timedelta
from utilities import get_conf
from margin import Margin


def orders_margin_week_msc():
    path = 'setting/margin/margin_week_msc_setting.ini'
    next_week(path)


def orders_margin_week_spb():
    path = 'setting/margin/margin_week_spb_setting.ini'
    next_week(path)


def orders_margin_next_day_msc():
    path = 'setting/margin/margin_next_day_msc_setting.ini'
    next_day(path)


def orders_margin_next_day_spb():
    path = 'setting/margin/margin_next_day_spb_setting.ini'
    next_day(path)


def next_week(path):
    confile = get_conf(path)
    orders_forecast = pd.read_csv(confile['Param_files']['orders_forecast'])
    orders_forecast = orders_forecast.set_index(orders_forecast['ds'])
    all_drivers = pd.read_csv(confile['Param_files']['all_drivers'])
    all_drivers = all_drivers.set_index(all_drivers['ds'])
    drivers_forecast = pd.read_csv(confile ['Param_files']['drivers_forecast'])
    drivers_forecast = drivers_forecast.set_index(drivers_forecast['ds'])
    days = confile['Number_days']['days']
    up_bound = confile['Bound']['up']
    lb_bound = confile['Bound']['lb']
    column = confile['Param_array']['name_column']
    root_request = confile['Param_json']['root_request']
    city_id = confile['Param_json']['city_id']
    direction_id = confile['Param_json']['direction_id']
    label = confile['Param_json']['label']
    url = confile['Param_request']['url']
    key = confile['Keys']['key']
    mm = Margin(
        orders_forecast,
        all_drivers,
        drivers_forecast,
        days,
        column,
        up_bound,
        lb_bound,
        root_request,
        city_id,
        direction_id,
        label,
        url,
        key,
    ).orders_margin()



def next_day(path):
    confile = get_conf(path)
    orders_forecast = pd.read_csv(confile['Param_files']['orders_forecast'])
    orders_forecast = orders_forecast.set_index(orders_forecast['ds'])
    all_drivers = pd.read_csv(confile['Param_files']['all_drivers'])
    all_drivers = all_drivers.set_index(all_drivers['ds'])
    drivers_forecast = pd.read_csv(confile ['Param_files']['drivers_forecast'])
    drivers_forecast = drivers_forecast.set_index(drivers_forecast['ds'])
    days = confile['Number_days']['days']
    up_bound = confile['Bound']['up']
    lb_bound = confile['Bound']['lb']
    column = confile['Param_array']['name_column']
    root_request = confile['Param_json']['root_request']
    city_id = confile['Param_json']['city_id']
    direction_id = confile['Param_json']['direction_id']
    label = confile['Param_json']['label']
    url = confile['Param_request']['url']
    key = confile['Keys']['key']
    mm = Margin(
        orders_forecast,
        all_drivers,
        drivers_forecast,
        days,
        column,
        up_bound,
        lb_bound,
        root_request,
        city_id,
        direction_id,
        label,
        url,
        key,
    ).orders_margin()



def main():
    print('orders_margin_week_msc()')
    orders_margin_week_msc()
    print('orders_margin_week_spb()')
    orders_margin_week_spb()
    print('orders_margin_next_day_msc()')
    orders_margin_next_day_msc()
    print('orders_margin_next_day_spb()')
    orders_margin_next_day_spb()


if __name__ == '__main__':
    main()
