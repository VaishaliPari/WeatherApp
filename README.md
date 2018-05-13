## WeatherApp
Language: Python 3
Server: Django Framework

# Project Setup:
•	To start a virtual environment, Run: 	
virtualenv weathersetup
source weathersetup/bin/activate
•	To install requirments, Run:
Pip3 install –r requirments.txt
(This will install Django, matplotlib, requests and pillow)

To run the server and host the webpage:
•	Go into the weather folder of the project: cd weather
•	Command: python3 manage.py runserver
•	To access go to: http://127.0.0.1:8000/

# Description: 
•	The default development location New York’s weather forcast is displayed.
•	Enter the desired location to fetch the current weather information and extended forcast.
•	The user’s location search history is stored in the DB and is printed out on the terminal. (This Additional requirement mentioned, could be extended to implementation using cookies and session in the webpage) 

# Documentation:
•	Views.py - This Python function takes a Web request and returns a Web response. It takes the location input from forms and makes a API call to google maps to get the latitude and longitude. If it’s an invalid input returns a HTTP response “Location not found”. With the location information makes another web request to get the weather data. This json response is parsed into a python dictionary and the context is rendered with the HTML content. It also contains other arbitrary logic such as plotting graph for the collected data using matplotlib and get weather icon images based on status.
•	Models.py - It contains a City model, which takes city name as input from the form and maps to database table forcast_city.
•	Forms.py – Here we are creating a model form, which has a name field for city name as text input.
•	Forcast.html – user interface of the webapp, this file has the page layout and contents design. 
