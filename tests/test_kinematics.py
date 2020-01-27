from . import physics, assertEqual


classObjecttoTest = physics.kinematics.Kinematics(
    initialVelocity=3, acceleration=2, time=20, sigFigs=1)
classObjecttoTest.calculations()
classObjecttoTestTwo = physics.kinematics.Kinematics(
    acceleration=-1, deltaDistance=2, finalVelocity=0, sigFigs=1)
classObjecttoTestTwo.calculations()
classObjecttoTestThree = physics.kinematics.Kinematics(
    finalVelocity=135, acceleration=-41, initialVelocity=372, sigFigs=2)
classObjecttoTestThree.calculations()


def test_kinematics_one_vi():
    assertEqual(classObjecttoTest.initialVelocity, '3')


def test_kinematics_one_vf():
    assertEqual(classObjecttoTest.finalVelocity, '40')


def test_kinematics_one_a():
    assertEqual(classObjecttoTest.acceleration, '2')


def test_kinematics_one_t():
    assertEqual(classObjecttoTest.time, '20')


def test_kinematics_one_d():
    assertEqual(classObjecttoTest.deltaDistance, '500')


def test_kinematics_one_record():
    assertEqual(classObjecttoTest.record, [1, 5])


def test_kinematics_two_vi():
    assertEqual(classObjecttoTestTwo.initialVelocity, '2')


def test_kinematics_two_vf():
    assertEqual(classObjecttoTestTwo.finalVelocity, '0')


def test_kinematics_two_a():
    assertEqual(classObjecttoTestTwo.acceleration, '-1')


def test_kinematics_two_t():
    assertEqual(classObjecttoTestTwo.time, '2')


def test_kinematics_two_d():
    assertEqual(classObjecttoTestTwo.deltaDistance, '2')


def test_kinematics_two_record():
    assertEqual(classObjecttoTestTwo.record, [7, 4])


def test_kinematics_three_vi():
    assertEqual(classObjecttoTestThree.initialVelocity, '372')


def test_kinematics_three_vf():
    assertEqual(classObjecttoTestThree.finalVelocity, '135')


def test_kinematics_three_a():
    assertEqual(classObjecttoTestThree.acceleration, '-41')


def test_kinematics_three_t():
    assertEqual(classObjecttoTestThree.time, '5.8')


def test_kinematics_three_d():
    assertEqual(classObjecttoTestThree.deltaDistance, '1500')


def test_kinematics_three_record():
    assertEqual(classObjecttoTestThree.record, [9, 4])
