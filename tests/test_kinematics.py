from . import physics_helpers

from nose2.tools import params
import unittest


class BasicTestSuite(unittest.TestCase):

    classObjecttoTest = physics_helpers.kinematics.Kinematics(initialVelocity=3,accelertaion=2,time=20)
    classObjecttoTest.calculations()

    def test_kinematics_one_vi(self):
        self.assertEqual(self.classObjecttoTest.initialVelocity, 3)
    def test_kinematics_one_vf(self):
        self.assertEqual(self.classObjecttoTest.finalVelocity, 40)
    def test_kinematics_one_a(self):
        self.assertEqual(self.classObjecttoTest.accelertaion, 2)
    def test_kinematics_one_t(self):
        self.assertEqual(self.classObjecttoTest.time, 20)
    def test_kinematics_one_d(self):
        self.assertEqual(self.classObjecttoTest.deltaDistance, 500)


if __name__ == '__main__':
    unittest.main()