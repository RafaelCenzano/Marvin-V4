from . import physics_helpers

from nose2.tools import params
import unittest


class BasicTestSuite(unittest.TestCase):

    classObjecttoTest = physics_helpers.kinematics.Kinematics(initialVelocity=3, accelertaion=2, time=20)
    classObjecttoTest.calculations()
    classObjecttoTestTwo = physics_helpers.kinematics.Kinematics(accelertaion=-1, deltaDistance=2, finalVelocity=0)
    classObjecttoTestTwo.calculations()

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
    def test_kinematics_one_record(self):
        self.assertEqual(self.classObjecttoTest.record, [1, 5])

    def test_kinematics_two_vi(self):
        self.assertEqual(self.classObjecttoTestTwo.initialVelocity, 2)
    def test_kinematics_two_vf(self):
        self.assertEqual(self.classObjecttoTestTwo.finalVelocity, 0)
    def test_kinematics_two_a(self):
        self.assertEqual(self.classObjecttoTestTwo.accelertaion, -1)
    def test_kinematics_two_t(self):
        self.assertEqual(self.classObjecttoTestTwo.time, 2)
    def test_kinematics_two_d(self):
        self.assertEqual(self.classObjecttoTestTwo.deltaDistance, 2)
    def test_kinematics_two_record(self):
        self.assertEqual(self.classObjecttoTestTwo.record, [7, 4])

if __name__ == '__main__':
    unittest.main()