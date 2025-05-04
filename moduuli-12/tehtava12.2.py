import requests
import json

city_name = input("Minkä kaupungin sään haluat: ").capitalize()
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=6f2c05652d50ce1b8ddeaeb5c2080c6f&units=metric"

response = requests.get(request).json()
print(" ")
desc = (response['weather'][0]['description'])
temp = (response['main']['temp'])
print(f"{city_name}ssa on {temp} astetta Celsiusta.")