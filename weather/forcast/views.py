import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import City
from .forms import CityForm
import matplotlib  
matplotlib.use('agg') 
import matplotlib.pyplot as plt
import datetime
from PIL import Image

def index(request):
	data="New York"
	if request.method == 'POST':
		city=request.POST
		data = city.get("name", "0")
		form = CityForm(city)
		form.save()
		
	form = CityForm()

	cities = list(set(City.objects.filter().values_list('name',flat=True)))

	print("Users Location Search History:")
	for c in cities:
		print (c)

	geourl='https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyDwOHWv8ch-6xHf5YnWsGLR2brZLEZvBDY'
	city=data
	geores=requests.get(geourl.format(city)).json()
	if not geores['results']:
		return HttpResponse("Loaction Not Found")
	t=geores['results'][0]
	geo_loc = {
		'lattitude' : t['geometry']['location']['lat'],
		'longitude' : t['geometry']['location']['lng'],
		'address' : t['formatted_address']
	}
	loc=str(geo_loc['lattitude'])+","+str(geo_loc['longitude'])
	url = 'https://api.darksky.net/forecast/841e887ec861b28d41527c5c1370256a/{}'
	r=requests.get(url.format(loc)).json()
	city_weather = {
		'temperature' : r['currently']['temperature'],
		'summary' : r['currently']['summary'],
		'icon' : r['currently']['icon'],
		'realfeel' : r['currently']['apparentTemperature'],
		'humidity' : r['currently']['humidity'],
		'pressure' : r['currently']['pressure'],
		'wind' : r['currently']['windSpeed'],
		'daily' : r['daily']['data'][1]['summary']
	}
	graph(r)
	getStatusIcon(city_weather['icon'])

	context ={'city_weather' : city_weather, 'geo_loc' : geo_loc, 'form' : form}
	
	return render(request, 'forcast/forcast.html', context)

def getStatusIcon(icon):
	if(icon =='rain'):
		logo = Image.open('forcast/static/forcast/icons/rain.png')
	elif (icon =='clear-day'):
		logo = Image.open('forcast/static/forcast/icons/clear-day.png')
	elif(icon =='partly-cloudy-day'):
		logo = Image.open('forcast/static/forcast/icons/partly-cloudy-day.png')
	elif(icon =='clear-night'):
		logo = Image.open('forcast/static/forcast/icons/clear-night.png')
	elif(icon =='partly-cloudy-night'):
		logo = Image.open('forcast/static/forcast/icons/partly-cloudy-night.png')
	elif(icon =='snow'):
		logo = Image.open('forcast/static/forcast/icons/snow.png')
	elif(icon =='fog'):
		logo = Image.open('forcast/static/forcast/icons/fog.png')
	elif(icon =='sleet'):
		logo = Image.open('forcast/static/forcast/icons/sleet.png')
	elif(icon =='wind'):
		logo = Image.open('forcast/static/forcast/icons/wind.png')
	elif(icon =='cloudy'):
		logo = Image.open('forcast/static/forcast/icons/cloudy.png')
	logo.save("forcast/static/forcast/status.png")
	

def graph(r):
	time=[]
	temp=[]
	for i in range(0,24):
		temp.append(r['hourly']['data'][i]['temperature']),
		time.append(datetime.datetime.fromtimestamp(int(r['hourly']['data'][i]['time'])).strftime('%H'))
	plt.plot(time,temp)
	plt.title('Extended Hourly Forcast upto 24 hours from current time')
	plt.ylabel('Temperatur (Farenheit)')
	plt.xlabel('Time-GMT (Hours)')
	plt.xticks(rotation=90)
	plt.savefig('forcast/static/forcast/graph.png')
	plt.clf()
