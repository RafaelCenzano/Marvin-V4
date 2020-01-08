from . import physics

from nose2.tools import params
import unittest


class BasicTestSuite(unittest.TestCase):

    classObjecttoTest = physics.kinematics.Kinematics(
        initialVelocity=3, acceleration=2, time=20)
    classObjecttoTest.calculations()
    classObjecttoTestTwo = physics.kinematics.Kinematics(
        acceleration=-1, deltaDistance=2, finalVelocity=0)
    classObjecttoTestTwo.calculations()
    classObjecttoTestThree = physics.kinematics.Kinematics(
        finalVelocity=135, acceleration=-41, initialVelocity=372)
    classObjecttoTestThree.calculations()

    def test_kinematics_one_vi(self):
        self.assertEqual(self.classObjecttoTest.initialVelocity, 3)

    def test_kinematics_one_vf(self):
        self.assertEqual(self.classObjecttoTest.finalVelocity, 40)

    def test_kinematics_one_a(self):
        self.assertEqual(self.classObjecttoTest.acceleration, 2)

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
        self.assertEqual(self.classObjecttoTestTwo.acceleration, -1)

    def test_kinematics_two_t(self):
        self.assertEqual(self.classObjecttoTestTwo.time, 2)

    def test_kinematics_two_d(self):
        self.assertEqual(self.classObjecttoTestTwo.deltaDistance, 2)

    def test_kinematics_two_record(self):
        self.assertEqual(self.classObjecttoTestTwo.record, [7, 4])

    def test_kinematics_three_vi(self):
        self.assertEqual(self.classObjecttoTestThree.initialVelocity, 372)

    def test_kinematics_three_vf(self):
        self.assertEqual(self.classObjecttoTestThree.finalVelocity, 135)

    def test_kinematics_three_a(self):
        self.assertEqual(self.classObjecttoTestThree.acceleration, -41)

    def test_kinematics_three_t(self):
        self.assertEqual(self.classObjecttoTestThree.time, 5.8)

    def test_kinematics_three_d(self):
        self.assertEqual(self.classObjecttoTestThree.deltaDistance, 1500)

    def test_kinematics_three_record(self):
        self.assertEqual(self.classObjecttoTestThree.record, [9, 4])


if __name__ == '__main__':
    unittest.main()
