# Imports
import math
from marvin.helpers.physics_helpers.numberProcessing import count_sig_figs, properRounding

'''
Kinematics

Functions to solve time, velocity, accelertaion and distance with the other variables stated.
'''


class Kinematics:

    def __init__(
                 self,
                 initialVelocity=None,
                 finalVelocity=None,
                 time=None,
                 accelertaion=None,
                 deltaDistance=None
                ):

        self.initialVelocity = initialVelocity
        self.finalVelocity = finalVelocity
        self.time = time
        self.accelertaion = accelertaion
        self.deltaDistance = deltaDistance

        sigFigsList = []

        if self.initialVelocity is not None:
            sigFigsList.append(count_sig_figs(self.initialVelocity))
        if self.finalVelocity is not None:
            sigFigsList.append(count_sig_figs(self.finalVelocity))
        if self.time is not None:
            sigFigsList.append(count_sig_figs(self.time))
        if self.accelertaion is not None:
            sigFigsList.append(count_sig_figs(self.accelertaion))
        if self.deltaDistance is not None:
            sigFigsList.append(count_sig_figs(self.deltaDistance))

        tempCount = sigFigsList[0]

        for item in sigFigsList:
            if item < tempCount:
                tempCount = item

        self.sigFigs = tempCount

    def finalVelocityOne(self):
        '''
        Equation:

        Vf = Vi + a * t

        Solve for Final Velocity with initial velocity, acceleration, and time
        '''

        if self.checkValue(
            self.initialVelocity) and self.checkValue(
            self.accelertaion) and self.checkValue(
            self.time) and self.finalVelocity is None:

            answer = self.initialVelocity + (self.accelertaion * self.time)

            self.finalVelocity = answer

    def initialVelocityOne(self):
        '''
        Equation:

        Vf - (a * t) = Vi

        Solve for Initial Velocity with final velocity, acceleration, and time
        '''

        if self.checkValue(
            self.finalVelocity) and self.checkValue(
            self.accelertaion) and self.checkValue(
            self.time) and self.initialVelocity is None:

            answer = self.finalVelocity - (self.accelertaion * self.time)

            self.initialVelocity = answer

    def accelerationOne(self):
        '''
        Equation:

        (Vf - Vi) / t = a

        Solve for Acceleration with final velocity, initial velocity, and time
        '''

        if self.checkValue(
            self.finalVelocity) and self.checkValue(
            self.initialVelocity) and self.checkValue(
            self.time) and self.accelertaion is None:

            answer = (self.finalVelocity - self.initialVelocity) / self.time

            self.accelertaion = answer

    def timeOne(self):
        '''
        Equation:

        (Vf - Vi) / a = t

        Solve for Time with final velocity, initial velocity, and acceleration
        '''

        if self.checkValue(
            self.finalVelocity) and self.checkValue(
            self.initialVelocity) and self.checkValue(
            self.accelertaion) and self.time is None:

            answer = (self.finalVelocity - self.initialVelocity) / self.accelertaion

            self.time = answer

    def deltaDistanceOne(self):
        '''
        Equation:

        Δx = Vi * t + 0.5 * a * t^2

        Solve for Delta Distance(Displacment) with initial velocity, acceleration, and time
        '''
        if self.checkValue(
            self.initialVelocity) and self.checkValue(
            self.accelertaion) and self.checkValue(
            self.time) and self.deltaDistance is None:

            answer = (self.initialVelocity * self.time) + \
                (0.5 * self.accelertaion * (self.time ** 2))

            self.deltaDistance = answer

    def finalVelocityTwo(self):
        '''
        Equation:

        Vf^2 = Vi^2 + 2 * a * t^2

        Solve for Final Velocity with initial velocity, acceleration, and delta distance
        '''

        if self.checkValue(
            self.initialVelocity) and self.checkValue(
            self.accelertaion) and self.checkValue(
            self.deltaDistance) and self.finalVelocity is None:

            answer = (self.initialVelocity ^ 2) + \
                (2 * self.accelertaion * self.deltaDistance)

            answerSqrt = Math.sprt(answer)

            self.finalVelocity = answerSqrt

    def checkValue(self, value):
        '''
        Check value to make sure its an int or float
        '''

        typeOfValue = type(value)

        if typeOfValue == int or typeOfValue == float:
            return True

        else:
            return False


if __name__ == '__main__':
    tester = Kinematics(initialVelocity=0, accelertaion=9.8, deltaDistance=5)
    tester.finalVelocityTwo()
    print(tester.finalVelocity)
