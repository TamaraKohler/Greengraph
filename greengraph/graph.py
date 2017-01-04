
import numpy as np
import geopy
from .map import Map

def is_number(s):    #Function checks if string has a representation as a float.
            try:
                float(s)
                return True
            except ValueError:
                return False

class Greengraph(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end
        if is_number(start):
            raise TypeError("Starting point should be a string (name of location)")
        if is_number(end):
            raise TypeError("Ending point should be a string (name of location)")
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        
    def geolocate(self, place):
        return self.geocoder.geocode(place, exactly_one=False)[0][1]
    
    def location_sequence(self, start,end,steps):
        if not is_number(steps):
            raise TypeError('Number of steps must be a number')
        if float(steps) != int(float(steps)):
            raise TypeError('Number of steps must be an integer')
        if int(steps) <= 0:
            raise ValueError('Number of steps must be positive')
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        if not is_number(steps):
            raise TypeError('Number of steps must be a number')
        if float(steps) != int(float(steps)):
            raise TypeError('Number of steps must be an integer')
        if int(steps) <= 0:
            raise ValueError('Number of steps must be positive')
        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start), 
                    self.geolocate(self.end),
                    steps)]