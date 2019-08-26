import schedule
import time
from utilities import  get_conf
from pdsql import Pysql


def drivers():
    path = 'setting/sql/drivers_setting.ini'
    send_request_sql(path)


def orders():
    path = 'setting/sql/orders_setting.ini'
    send_request_sql(path)


def planning_data():
    path = 'setting/sql/planning_data_setting.ini'
    send_request_sql(path)


def cars_status():
    path = 'setting/sql/cars_status_setting.ini'
    send_request_sql(path)


def planning_status():
    path = 'setting/sql/planning_status_setting.ini'
    send_request_sql(path)


def send_request_sql(path):
    confile = get_conf(path)
    host = confile['Param_db']['host']
    table_name = confile['Param_db']['table_name']
    user = confile['Param_db']['user']
    password = confile['Param_db']['password']
    database = confile['Param_db']['database']
    fields = confile['Param_db']['fields']
    column_index = confile['Param_db']['column_index']
    mod = confile['Form_Record']['mod']
    optionally_argument = confile['Param_db']['optionally_argument']
    name = confile['Param_file']['name']
    header = confile['Param_file']['header']
    row = confile['Rows']['row']
    ps = Pysql(
        path,
        host,
        table_name,
        user,
        password,
        database,
        fields,
        column_index,
        mod,
        optionally_argument,
        name,
        header,
        row,
    ).template_sql()


def main():
    drivers()
    orders()
    planning_data()
    cars_status()
    planning_status()


if __name__ == '__main__':
    main()
