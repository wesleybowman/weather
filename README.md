weather.py
==========

A simple weather script to use from CLI.

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
- improve time 

**Usage**:

	$ git clone git://github.com/evgorch/weather.git
	$ cd weather/
	$ chmod +x weather.py 
 	$ ./weather.py

**Sample output**:
	
        [evg@arch weather]$ ./weather.py 

                Ottawa, CA
                Updated:        2013-04-20 01:40 GMT
                Time now:       2013-04-20 02:22 GMT
                ------------------------------------
                Temperature:    9  C
                Condition:      overcast clouds
                Wind:           2.57 m/s
                Humidity:       83 %
