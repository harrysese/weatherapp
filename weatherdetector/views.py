from django.shortcuts import render
import requests
from django.http import JsonResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        api_key = "6e5f7b45c9c3e1279fb0c6f6171b21a4"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city.capitalize()}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if response.status_code==200:
            temperature=data["main"]["temp"]
            humidity=data['main']['humidity']
            pressure=data["main"]['pressure']
            description=data["weather"][0]["description"]
            icon=data['weather'][0]['icon']
            speed=data['wind']['speed']
            deg=data['wind']['deg']
        else:
            return render(request,'index.html', {'error':'City not found'})

       
        celsius = round(int(temperature) - 273.15)  # converting kelvin to celsius
        context = {
            "temperature": celsius,
            "humidity": humidity,
            "pressure": pressure,
            "city": city.capitalize(),
            "description": description,
            'icon':icon,
            "speed":speed,
            "deg":deg,
        }
        return render(request, "index.html", context)

    else:
        return render(request, "index.html")
