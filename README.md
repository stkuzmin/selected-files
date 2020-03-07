This software is created for Red Crown company, Saint-Petersburg, Russia and all rights belong to this company. 
In this repo I posted only a few files just to demonstrate my programming skills 

The goal of this programm is to generate optimized margin for the sevices of the logistic company. Actually, this software could be use 
at any company that have hourly changes in customer demand. This software help to maximize revenue. 

The functionality of this software is devided on three parts:
A) Acquisition of the time series information from the company DataBase (in our case this is MySQL database) 
B) Generate forecast of the principle parameters of the services under consideration (in our case: the overall number of cars, free cars 
(without order), number of orders, number of phone calls of the potential customers). There are three forecasts: online current day, 
next day, and next week
C) Optimize the margin (factor of the services price) calculations that maximize revenue. 

History:
This software was developed by deep modification of an old company software.
First of all, the new economical model was created. According to this model, the demand/supply curve changes every hour. The model has
classical exponential form with two parameters (amplitude and supply elasticity)

A)  Date acquisition: Executable file - sql_manage.py Uploaded files in the /data/sql folder
B) Calculation of the forecast of the principle parameters for the next day and the next week:
config files in the /settings/forecast folder, executable file forecast_manage.py forecasts in the /data/forecast folder
C) calculation of the prediction of margin for the next day and the next week:
config files in the /settings/margin directory executable file margin_manage.py all markups in the /data/margin folde in json
and csv format

Installation:

The following packages are required:
anaconda with python 3.6 or 3.7 with libraries numpy, cython, time, datetime, schedule, pandas, mysql.connector, configparser, 
json, requests, collections
better that everything be installed with conda in a separate environment
then you need to install the current C ++ gcc compiler
then PyStan is needed: https://pystan.readthedocs.io/en/latest/installation_beginner.html
And finally, you need to install fbprophet-05: https://facebook.github.io/prophet/docs/installation.html

To start software you need to run the schedule file Main01.py
