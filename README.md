# WeatherApp
Designed to leverage a weather API combined with a geolocation API to allow users to retrieve current and extended weather forecast for any location of search<br /><br />
Language: Python 3 <br />
Server: Django Framework <br />

## Project Setup:<br />
•	To start a virtual environment, Run: 	<br />
virtualenv weathersetup <br />
source weathersetup/bin/activate <br />
•	To install requirments, Run: <br />
Pip3 install –r requirments.txt <br />
(This will install Django, matplotlib, requests and pillow) <br />
<br />
To run the server and host the webpage:<br />
•	Go into the weather folder of the project: cd weather<br />
•	Command: python3 manage.py runserver<br />
•	To access go to: http://127.0.0.1:8000/<br />

## Description: 
•	The default development location New York’s weather forcast is displayed.<br />
•	Enter the desired location to fetch the current weather information and extended forcast.<br />
•	The user’s location search history is stored in the DB and is printed out on the terminal. (This Additional requirement mentioned, could be extended to implementation using cookies and session in the webpage)<br /> 

## Documentation:
•	Views.py - This Python function takes a Web request and returns a Web response. It takes the location input from forms and makes a API call to google maps to get the latitude and longitude. If it’s an invalid input returns a HTTP response “Location not found”. With the location information makes another web request to get the weather data. This json response is parsed into a python dictionary and the context is rendered with the HTML content. It also contains other arbitrary logic such as plotting graph for the collected data using matplotlib and get weather icon images based on status.<br />
•	Models.py - It contains a City model, which takes city name as input from the form and maps to database table forcast_city.<br />
•	Forms.py – Here we are creating a model form, which has a name field for city name as text input.<br />
•	Forcast.html – user interface of the webapp, this file has the page layout and contents design. <br />
<br />
