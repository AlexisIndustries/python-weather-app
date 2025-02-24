import requests
from django.shortcuts import render

from pyweatherapp.settings import OWM_API_KEY
from weather.models import QueryHistory


def weather_query(request):
    context = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=en"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data.get('main', {}).get('temp')
                description = data.get('weather', [{}])[0].get('description')
                # Сохраняем запрос в базу данных
                QueryHistory.objects.create(
                    city_name=city,
                    temperature=temperature,
                    description=description
                )
                context['weather'] = {
                    'city': city,
                    'temperature': temperature,
                    'description': description,
                }
            else:
                context['error'] = 'City not found or API error occurred'
    return render(request, 'index.html', context)

def query_history(request):
    queries = QueryHistory.objects.all().order_by('-query_time')
    context = {'queries': queries}
    return render(request, 'history.html', context)
