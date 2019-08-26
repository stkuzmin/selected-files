import schedule
import time
import sql_manage
import forecast_manage
import margin_manage


# forecast_manage.py


def get_day_manager_spb():
    return margin_manage.orders_margin_next_day_spb()


schedule.every(28).minutes.do(get_day_manager_spb)


def get_day_manager_msc():
    return margin_manage.orders_margin_next_day_msc()


schedule.every(28).minutes.do(get_day_manager_msc)


while True:
    schedule.run_pending()
    time.sleep(10)

#spb - 1 - 1.5
#msc - 1 -2.0