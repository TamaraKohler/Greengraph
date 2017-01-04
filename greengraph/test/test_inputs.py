from greengraph import Greengraph
from nose.tools import assert_raises

def test_begin_type():
    with assert_raises(TypeError):
        assert Greengraph('5','Oxford')

        
def test_end_type():
    with assert_raises(TypeError):
        assert Greengraph('London','7')
        
        
def test_for_false_positive_location_type():
    with assert_raises(TypeError):
        assert Greengraph('London', 'Oxford')