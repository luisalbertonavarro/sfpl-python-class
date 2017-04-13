"""
Generates weather forecast.

This script generates a 7 day weather forecast, either in Celsius or
Fahrenheit, using previously filled weather information.

"""
__author__      = "Luis Navarro"
__copyright__   = "Copyright 2017, Luis Navarro"

# Import Python's date library -- we'll use it to get date information
import datetime

# Declare a list of integers containing assumed weather forecast for the
# next 7 days
weather_forecast_fahrenheit = [59.3, 61.2, 60.4, 57.2, 60.0, 61.9, 60.3]

# Declare a list of strings containing supported temperature scales
scales = ["fahrenheit", "celsius"]

# Create an empty string variable to hold user's temperate scale of choice
scale_choice = ""

# Ask user for preferred temperature scale among valid options
while scale_choice not in scales:
  scale_choice = raw_input("Enter fahrenheit or celsius: ").lower()

# Get today's date
today = datetime.date.today()

# Get tomorrow's date using today's date. Since it's a forecast,
# we want to provide weather information starting tomorrow.
date = today + datetime.timedelta(1)

# Print basic information
print "The weather in San Francisco for the next 7 days is going to be:"

# Main loop -- the app ends after iterating over the 7 days of weather forecast
for temperature_fahrenheit in weather_forecast_fahrenheit:

    if scale_choice == "fahrenheit":
        # Convert temperature from floating point (i.e. 59.3) to integers (i.e. 59)
        temperature_fahrenheit = int(temperature_fahrenheit)

        # Print weather foreacast in Fahrenheit
        print("Date: " + str(date) + " Temperature (F): " + str(temperature_fahrenheit))
    else:
        # Convert temperature from Fahrenheit to Celsius
        temperature_celsius = (temperature_fahrenheit - 32) * 5.0/9.0

        # Convert temperature from floating point (i.e. 15.16) to integer (i.e. 15)
        temperature_celsius = int(temperature_celsius)

        # Print weather foreacast in Celsius
        print("Date: " + str(date) + " Temperature (C): " + str(temperature_celsius))

    # Calculate the next day's date
    date = date + datetime.timedelta(1)
