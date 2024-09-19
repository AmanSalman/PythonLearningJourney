from pyowm import OWM

API_KEY = "28942728fee9468f43a27def803e9623"
owm = OWM(API_KEY)

# Get the weather manager
weather_manager = owm.weather_manager()

# Get the weather observation for a specific location
observation = weather_manager.weather_at_place("Tulkarm")
weather = observation.weather

# Print general weather information
print("Weather Details:")
print("Temperature (Celsius):", weather.temperature('celsius'))
print("Weather Status:", weather.status)
print("Weather Description:", weather.detailed_status)

# Print wind details
wind = weather.wind()
print("Wind Speed (m/s):", wind.get('speed'))
print("Wind Gusts (m/s):", wind.get('gust'))
print("Wind Direction (degrees):", wind.get('deg'))

# Print humidity
humidity = weather.humidity
print("Humidity (%):", humidity)
