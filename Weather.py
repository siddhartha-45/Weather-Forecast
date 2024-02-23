import requests
def get_weather(location):
    api_key = "bb197c411e866ae3f1479038cba43e97"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    if location.isdigit():
        main_url = base_url + "zip=" + location + "&appid=" + api_key
        response = requests.get(main_url)
        data = response.json()

    else:
        main_url = base_url + "q=" + location + "&appid=" + api_key
        response = requests.get(main_url)
        data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        temp_kelvin = main_data["temp"]
        temp_celsius = round(temp_kelvin - 273.15, 2)
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]

        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]

        print("Temperature (in Celsius unit) :", temp_celsius)
        print("Atmospheric pressure (in hPa unit) :", pressure)
        print("Humidity (in percentage) :", humidity)
        print("Description:", weather_description)

    else:
        print("City not found!")

if __name__ == "__main__":
    location = input("Enter city name or zipcode: ")
get_weather(location)
