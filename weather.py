#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from time import gmtime, strftime

# URLs for retrieving IP, locations, weather data

IP_URL = "http://ipecho.net/plain"
LOCATION_URL = "http://www.geobytes.com/IpLocator.htm?GetLocation"
WEATHER_URL = "http://api.openweathermap.org/data/2.1/find/name"


def get_IP():
	return requests.get(IP_URL).text

def get_location(ip):
	location_params = {'template':'json.txt', 'IpAddress':ip}
	location_json = requests.get(LOCATION_URL, params=location_params).json()
	country = location_json['geobytes']['country']
	city = location_json['geobytes']['city']
	return (city, country)

def get_weather_data(city, country, units='metric'):
	weather_params = {'q':'{0},{1}'.format(city,country), 'units': units}
	weather_json = requests.get(WEATHER_URL, params=weather_params).json()
	return weather_json

def output_weather(weather):
	w=weather['list'][0]  #temp var to decrease number of chars used
	city = w['name']
	country = w['sys']['country']
	date = w['date'][:-3]
	temp = round(w['main']['temp'])
	desc = w['weather'][0]['description']
	windspeed = w['wind']['speed']
	humidity = w['main']['humidity']
	current_time = strftime("%Y-%m-%d %H:%M",gmtime())
	print(
	"""
	{0}
	Updated:	{1} GMT
	Time now:	{2} GMT
	------------------------------------
	Temperature:	{3}  C
	Condition:	{4}
	Wind:		{5} m/s
	Humidity:	{6} %
	"""
	.format(
		city+', '+country,
		date,
		current_time,
		temp,
		desc,
		windspeed,
		humidity		
		)
	)

def main():
	ip=get_IP()
	city,country=get_location(ip)
	weather=get_weather_data(city,country)
	output_weather(weather)

if __name__ == '__main__':
	main()