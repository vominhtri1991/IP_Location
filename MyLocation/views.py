from django.shortcuts import render
import requests
def home(request):
	is_cache=('geo' in request.session)
	get_from_cache="yes"
	if not is_cache:
		respones=requests.get("https://api.myip.com/")
		geo=respones.json()
		ip=geo['ip']
		respones=requests.get("http://ip-api.com/json/"+ip)
		geo=respones.json()
		request.session['geo']=geo
		get_from_cache="no"
	geo=request.session['geo']
	ip=geo['query']
	location=geo['country']+"/"+geo['city']
	latitude=geo['lat']
	longitude=geo['lon']
	return render(request,'MyLocation/home.html',{'ip':ip,'location':location,'is_cache':get_from_cache,'lat':latitude,'lon':longitude})

# Create your views here.
