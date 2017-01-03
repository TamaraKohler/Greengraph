import numpy as np
import geopy
from .map import Map

class Greengraph(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        
    def geolocate(self, place):
        return self.geocoder.geocode(place, exactly_one=False)[0][1]