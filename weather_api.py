import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    weather = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]

    print("Weather Report")
    print("----------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather)
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "km/h")

except:
    print("Unable to fetch weather data.")