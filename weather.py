#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from functools import reduce
from time import gmtime, strftime


# URLs for retrieving IP, locations, weather data

IP_URL = "http://ipecho.net/plain"
LOCATION_URL = "http://www.geobytes.com/IpLocator.htm?GetLocation"
WEATHER_URL = "http://api.openweathermap.org/data/2.1/find/name"


def safe_get(*args):
	try:
		return reduce(lambda a,b: a[b], args)
	except KeyError:
		return 'N/A'

def get_IP():
	return requests.get(IP_URL).text

def get_location(ip):
	location_params = {'template':'json.txt', 'IpAddress':ip}
	location_json = requests.get(LOCATION_URL, params=location_params).json()
	country = safe_get(location_json,'geobytes','country')
	city = safe_get(location_json,'geobytes','city')
	return (city, country)

def get_weather_data(city, country, units='metric'):
	weather_params = {'q':'{0},{1}'.format(city,country), 'units': units}
	weather_json = requests.get(WEATHER_URL, params=weather_params).json()

	w = safe_get(weather_json,'list',0)  #temp var 
	
	weather_data = {
		'city' : 		safe_get(w,'name'),
		'country' : 	safe_get(w,'sys','country'),
		'date' : 		safe_get(w,'date'),
		'temp' :		safe_get(w,'main','temp'), 
		'description' :	safe_get(w,'weather',0,'description'),
		'windspeed' : 	safe_get(w,'wind','speed'),
		'humidity' : 	safe_get(w,'main','humidity')
	}

	try:
		weather_data['temp']=round(weather_data['temp'])
	except TypeError:
		pass

	return weather_data

def output_weather(weather_data):
	current_time = strftime("%Y-%m-%d %H:%M:%S",gmtime())

	print(
	"""
	{0}
	Updated:	{1} GMT
	Time now:	{2} GMT
	---------------------------------------
	Temperature:	{3} (C)
	Wind:		{5} (m/s)
	Humidity:	{6} (%)
	Condition:	{4}
	"""
	.format(
		weather_data['city']+', '+weather_data['country'],
		weather_data['date'],
		current_time,
		weather_data['temp'],
		weather_data['description'],
		weather_data['windspeed'],
		weather_data['humidity']		
		)
	)

def main():
	ip=get_IP()
	city,country=get_location(ip)
	weather=get_weather_data(city,country)
	output_weather(weather)

if __name__ == '__main__':
	main()