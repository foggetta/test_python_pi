#test weather
from requests import get
import json
from pprint import pprint
from haversine import haversine

def put_stations():
    stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
    all_stations = get(stations).json()['items']
    return all_stations
    
def find_closest(all_stations, my_lon, my_lat):
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

def get_weather(my_lon, my_lat):
    weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
    closest_stn = find_closest(put_stations(), my_lon, my_lat)
    weather_cls = weather + str(closest_stn)
    my_weather = get(weather_cls).json()['items']
    return my_weather
    
