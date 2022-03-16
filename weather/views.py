from django.shortcuts import render
import requests
from datetime import datetime


# get data from Weather API
def get_weather(location):
    weather_api = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key=7c170c2ef0f5493b8aa51750221702&q={location}&aqi=no")
    weather_data = weather_api.json()
    return weather_data


def get_quotes():
    quote_api_url = "https://zenquotes.io/api/random"
    quote_response = requests.get(quote_api_url)
    quote_data = quote_response.json()
    return quote_data


def get_holidays(time):
    holidays = requests.get(
        f"https://holidays.abstractapi.com/v1/?api_key=95f11bf299a44e7aad0c7503ef66205f&country=IR&year={time.year}&month={time.month}&day={time.day}")
    holidays = holidays.json()
    return holidays


def main(request):
    location = request.GET.get("location")
    weather_data = get_weather(location)
    time = datetime.now()
    quote_data = get_quotes()
    holidays = get_holidays(time)
    part_of_day = get_part_of_day(int(time.hour))

    return render(request, "index.html",
                  context={"weather": weather_data, "quote": quote_data, "part": part_of_day, "holidays": holidays,
                           "time": time})


# get part of day in each hour
def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )
