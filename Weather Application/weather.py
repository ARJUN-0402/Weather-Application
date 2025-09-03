import requests # The requests library is for making HTTP requests to a URL.

# --- IMPORTANT SETUP ---
# Replace this placeholder with your actual API key from OpenWeatherMap.
# You can get one for free by signing up at https://openweathermap.org/api
API_KEY = "YOUR_OWN_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches and displays the current weather for a given city.

    Args:
        city_name (str): The name of the city to get the weather for.
    """
    try:
        # Construct the full URL for the API request.
        # We use f-strings for clean string formatting.
        # This is the corrected line, using the API_KEY variable.
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

        # Make the API request.
        # requests.get() sends a GET request to the specified URL.
        response = requests.get(url)

        # Raise an HTTPError if the response status code is 4xx or 5xx.
        response.raise_for_status()

        # Parse the JSON response.
        weather_data = response.json()

        # Check if the city was found.
        if weather_data["cod"] == 200:
            # Extract key information from the JSON data.
            main_data = weather_data["main"]
            weather_desc = weather_data["weather"][0]["description"]
            
            temperature = main_data["temp"]
            humidity = main_data["humidity"]

            # Print the weather information in a user-friendly format.
            print("-" * 30)
            print(f"Weather in {city_name.title()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_desc.title()}")
            print("-" * 30)
        else:
            # Handle cases where the city is not found.
            print(f"Error: Could not find weather data for '{city_name}'.")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors.
        print(f"An error occurred: {e}")
    except KeyError:
        # This handles cases where the API response structure is unexpected.
        print(f"Error: Invalid API key or data format for '{city_name}'.")
    except Exception as e:
        # Catch any other unexpected errors.
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # The code inside this block will only run when the script is executed directly.
    print("Welcome to the Command-Line Weather App!")
    while True:
        city = input("Enter a city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            break
        get_weather(city)

    print("Thank you for using the Weather App!")


