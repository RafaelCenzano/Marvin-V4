from . import physics_helpers

from nose2.tools import params
import unittest

class BasicTestSuite(unittest.TestCase):

    def test_kinematics_one(self):
        classObjecttoTest = physics_helpers.kinematics.Kinematics()


if __name__ == '__main__':
    unittest.main()