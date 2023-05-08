from django.shortcuts import render
import json
import urllib.request

# Create your views here.




def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="+city+ '&appid=70072edd70ca36e1e9bc0eba4b554bae'
            ).read()
        list_of_data = json.loads(source)
        print(list_of_data)
        data = {
            "name": str(list_of_data['name']),
            "weather": str(list_of_data['weather'][0]['main']),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon'])+
                            str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "feelslike": str(list_of_data['main']['feels_like']),
            "windspeed": str(list_of_data['wind']['speed']),
            "winddegree": str(list_of_data['wind']['deg']),
        }
        print(data)
    else:
        data={}
    return render(request, 'index.html',data)

    