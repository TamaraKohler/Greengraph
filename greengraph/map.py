
import numpy as np
from io import BytesIO
from matplotlib import image as img
import requests

class Map(object):
    def __init__(self, lat, long, satellite=True, zoom=10, 
                 size=(400,400), sensor=False):
        base="http://maps.googleapis.com/maps/api/staticmap?"
  
        params=dict(
            sensor= str(sensor).lower(),
            zoom= zoom,
            size= "x".join(map(str, size)),
            center= ",".join(map(str, (lat, long) )),
            style="feature:all|element:labels|visibility:off"
          )
    
        if satellite:
            params["maptype"]="satellite"
            
        self.image = requests.get(base, 
                    params=params).content # Fetch our PNG image data
        content = BytesIO(self.image)
        self.pixels= img.imread(content) # Parse our PNG image as a numpy array
        