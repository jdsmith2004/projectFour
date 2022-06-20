from django.shortcuts import render
from weather.models import Observation
from django.utils import timezone
import requests

# Create your views here.

def my_weather(request):
    if request.method == "POST":
        params = request.POST
        new_obs = Observation(
            time = timezone.now(), 
            temp = params["obsTemp"],
            sky = params["obsSky"])
        new_obs.save()
        
    all_obs = Observation.objects.all()
    
    if len(all_obs) == 0:
        avg_temp = 0
    else:
        total_temp = 0
        for obs in all_obs:
            total_temp += obs.temp
        avg_temp = total_temp / len(all_obs)

    data = {"all_obs" : all_obs, "avg_temp" : avg_temp}
    return render(request, "weather/display_my_weather.html", data)

def nws_weather(request, site):
    url = "https://api.weather.gov/stations/"+site+"/observations"
    server_data = requests.get(url).json()
    all_obs = []
    for feature in server_data["features"]:
        try:
            obs = feature["properties"]
            time = obs["timestamp"]
            temp = (float(obs["temperature"]["value"]) * 9 / 5) + 32
            sky = obs["textDescription"]
            all_obs.append({
                "time" : time,
                "temp" : temp,
                "sky" : sky})
        except Exception:
            pass
    sorted_all_obs = sorted(all_obs, key = lambda x : x["time"], reverse=True)
    data = {"site" : site, "all_obs" : sorted_all_obs}
    return render(request, "weather/display_nws_weather.html", data)



