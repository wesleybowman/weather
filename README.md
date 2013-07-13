weather.py
==========

A simple weather script to use from CLI.

Maximum 20 requests/hour due to API limitations.

**How it works**:

1. get location by external IP
2. get weather data by location

**What it uses**:
* [requests](http://docs.python-requests.org/) module
* [OpenWeatherMap JSON API](http://openweathermap.org/wiki/API/JSON_API)
* [geobytes IP locator](http://www.geobytes.com/IpLocator.htm?GetLocation)

**Requirements**:
* python3
* [requests](http://docs.python-requests.org/) module

**Usage**:

	$ git clone git://github.com/evgorch/weather.git
	$ cd weather/
	$ chmod +x weather.py 
 	$ ./weather.py

**Sample output**:
	
[evg@arch weather]$ ./weather.py 

        Ottawa, CA
        Updated:        2013-04-20 18:42:31 GMT
        Time now:       2013-04-20 19:17:40 GMT
        ---------------------------------------
        Temperature:    4 (C)
        Wind:           9.8 (m/s)
        Humidity:       48 (%)
        Condition:      overcast clouds

[wesley@ArchLinux weather]$ python weather.py

	Halifax, CA
	Updated:	2013-07-13 12:00:00 GMT
	Time now:	2013-07-13 13:38:38 GMT
	---------------------------------------
	Temperature:	20 (°C)
	Wind:		3.1 (m/s)
	Humidity:	72 (%)
	Condition:	few clouds

