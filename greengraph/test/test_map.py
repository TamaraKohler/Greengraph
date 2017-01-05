
from unittest.mock import Mock, patch
from greengraph import Greengraph
from greengraph.map import Map
import requests
import os
import numpy.testing as npt
from matplotlib import image as img
import numpy
from io import BytesIO
from nose.tools import assert_equals


lat = 51.5073509
long = -0.1277583

def test_build_map():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures/london_map.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        mock_get.assert_called_with(
            'http://maps.googleapis.com/maps/api/staticmap?',
            params=dict(size='400x400', zoom=10, center='51.5073509,-0.1277583',
                        style='feature:all|element:labels|visibility:off', sensor='false', maptype='satellite')
        )
        
        
def test_pixels():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures/london_map.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, long)
        expected_pixels = numpy.load(os.path.join(os.path.dirname(__file__),
                                   'fixtures/test_pixels.npy'))
        npt.assert_array_equal(test_map.pixels,expected_pixels)