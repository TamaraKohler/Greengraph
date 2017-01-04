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
        
def test_steps_type_1():
    with assert_raises(TypeError):
        assert Greengraph('London', 'Oxford').green_between('green')

def test_steps_type_2():
    with assert_raises(TypeError):
        assert Greengraph('London', 'Oxford').green_between('3.5')
        
def test_steps_value():
    with assert_raises(ValueError):
        assert Greengraph('London', 'Oxford').green_between('-3')
        
def test_for_false_positive_steps_type():
    with assert_raises(TypeError):
        assert Greengraph('London', 'Oxford').green_between('3')
        
def test_for_false_positive_steps_value():
    with assert_raises(ValueError):
        assert Greengraph('London', 'Oxford').green_between('3')