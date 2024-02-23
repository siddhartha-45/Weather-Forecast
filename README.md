# Weather-Forecast
This Python script defines a function get_weather(location) that fetches and displays weather information for a given location (city name or zip code). 
Here's how it works:

It imports the requests module to make HTTP requests.
The function takes a location parameter, which can be either a city name or a zip code.
It uses the OpenWeatherMap API to retrieve weather data. It constructs the API URL based on whether the location input is a digit (zip code) or a string (city name).
It sends a GET request to the API and stores the response in data.
If the API response indicates a successful request ("cod" is not "404"), it extracts and prints various weather parameters such as temperature (in Celsius), atmospheric pressure (in hPa), humidity (in percentage), and a brief description of the weather.
If the location is not found (404 error), it prints "City not found!".
When the script is run directly (using if __name__ == "__main__":), it prompts the user to enter a city name or zip code, and then calls the get_weather() function with the entered location to display the weather information.






