weather
=======

A simple and straightforward weather script to use with CLI.
Maximum 20 requests/hour due to API limitations.

**How it works**:

1. get external IP
2. get location by external IP
3. get weather data by location

**What it uses**:
* [requests](http://docs.python-requests.org/) module
* [OpenWeatherMap JSON API](http://openweathermap.org/wiki/API/JSON_API)
* [geobytes IP locator](http://www.geobytes.com/IpLocator.htm?GetLocation)

**To Do**:
- [GMT => localtime conversion]
- [degree sign]
- [wind direction]

**Usage**:
	 git clone git://github.com/evgorch/weather.git
	 chmod +x weather.py 
then
	 ./weather.py

**Sample output**:

	#########################
	Ottawa, CA
	Last updated: 2013-04-18 00:50:47 GMT

	Temperature:	7.74 C
	Condition:		overcast clouds
	Wind:			3.1 m/s
	Humidity:		31 %
	#########################
