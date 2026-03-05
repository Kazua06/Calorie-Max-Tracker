from django.shortcuts import render

#ei6aQrExr8hdhAp1YYTyJcRVLqH2vHKNOm7ta6d0
# Create your views here.
def home(request):
     import json
     import requests
     if request.method == 'POST':
          query = request.POST['query']
          api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query='
          api_request = requests.get(api_url + query + '&api_key=ei6aQrExr8hdhAp1YYTyJcRVLqH2vHKNOm7ta6d0')
          try:
               data = json.loads(api_request.content)
               food = data['foods'][0]
               nutrients = food['foodNutrients']
               def get(name): return round(next((n['value'] for n in nutrients if n['nutrientName'] == name), 0), 1)
               api = [{
                    'name': food['description'].title(),
                    'calories': get('Energy'),
                    'protein_g': get('Protein'),
                    'carbohydrates_total_g': get('Carbohydrate, by difference'),
                    'sugar_g': get('Total Sugars'),
                    'fat_total_g': get('Total lipid (fat)'),
                    'fat_saturated_g': get('Fatty acids, total saturated'),
                    'cholesterol_mg': get('Cholesterol'),
                    'fiber_g': get('Fiber, total dietary'),
                    'potassium_mg': get('Potassium, K'),
                    'sodium_mg': get('Sodium, Na'),
               }]
               print(api_request.content)
          except Exception as e:
               api = "oops! There was an error"
               print(e)
          return render(request, 'home.html',{'api':api})
     else:
          return render(request, 'home.html',{'query':'Enter a valid query'})
               