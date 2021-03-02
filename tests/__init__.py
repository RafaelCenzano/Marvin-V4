import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../marvin/helpers')))

import physics
from marvin.helpers import numberProcessing

def assertEqual(value, equalTo):
    assert value == equalTo

def assertTrue(value):
    assert value is True

def assertFalse(value):
    assert value is False