import requests
import json

api_key = "4c1d6be0e70269fb9ceaa98e8cb8d9b7"

city = input("Lütfen bir şehir adı girin: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

if response.status_code == 404:
    print("Şehir bulunamadı")
else:
    data = json.loads(response.text)

    
    temperature = data['main']['temp'] - 273.15
    humidity = data['main']['humidity']
    

    print(f"Hava durumu bilgileri {city} için:")
    print(f"Sıcaklık: {temperature:.1f} °C") 
    print(f"Nem: {humidity}%")
    

