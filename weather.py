# -*- coding: utf-8 -*-
#! /usr/bin/env python


import requests
import json


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
	city = weather['list'][0]['name']
	country = weather['list'][0]['sys']['country']
	date = weather['list'][0]['date']
	temp = weather['list'][0]['main']['temp']
	desc = weather['list'][0]['weather'][0]['description']
	windspeed = weather['list'][0]['wind']['speed']
	humidity = weather['list'][0]['main']['humidity']

	print(
	"""
	#########################
	{0}
	Last updated: {1} GMT

	Temperature:	{2} C
	Condition:	{3}
	Wind:		{4} m/s
	Humidity:	{5} %
	#########################
	"""
	.format(
		city+', '+country,
		date,
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