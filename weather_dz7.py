import requests

API_KEY = "09d7b4ec5f2c17cb82b2d3d8701212e7"

# Задание 2: текущая погода в городе через OpenWeather
city = input("Введите город: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Температура: {data['main']['temp']} °C")
    print(f"Погода: {data['weather'][0]['description']}")
else:
    print("Ошибка:", data.get("message", response.status_code))
