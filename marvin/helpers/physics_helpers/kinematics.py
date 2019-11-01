# Imports
import math
from marvin.helpers.physics_helpers.numberProcessing import count_sig_figs, properRounding, checkValue

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
        acceleration=None,
        deltaDistance=None
    ):

        self.initialVelocity = initialVelocity
        self.finalVelocity = finalVelocity
        self.time = time
        self.acceleration = acceleration
        self.deltaDistance = deltaDistance
        self.test = False

        sigFigsList = []

        if self.initialVelocity is not None:
            sigFigsList.append(count_sig_figs(self.initialVelocity))
        if self.finalVelocity is not None:
            sigFigsList.append(count_sig_figs(self.finalVelocity))
        if self.time is not None:
            sigFigsList.append(count_sig_figs(self.time))
        if self.acceleration is not None:
            sigFigsList.append(count_sig_figs(self.acceleration))
        if self.deltaDistance is not None:
            sigFigsList.append(count_sig_figs(self.deltaDistance))

        tempCount = sigFigsList[0]

        for item in sigFigsList:
            if item < tempCount:
                tempCount = item

        self.sigFigs = tempCount

        self.record = []

    def calculations(self):
        count = 0

        while(checkValue(self.initialVelocity) == False or checkValue(self.deltaDistance) == False or checkValue(self.finalVelocity) == False or checkValue(self.time) == False or checkValue(self.acceleration) == False):
            if count > 9:
                break
            self.finalVelocityOne()
            self.finalVelocityTwo()
            self.initialVelocityOne()
            self.initialVelocityTwo()
            self.accelerationOne()
            self.accelerationTwo()
            self.deltaDistanceOne()
            self.deltaDistanceTwo()
            self.timeOne()
            count += 1

    def finalVelocityOne(self):
        '''
        Equation:

        Vf = Vi + a * t

        Solve for Final Velocity with initial velocity, acceleration, and time
        '''

        if checkValue(
                self.initialVelocity) and checkValue(
                self.acceleration) and checkValue(
                self.time) and self.finalVelocity is None:

            answer = self.initialVelocity + (self.acceleration * self.time)

            self.finalVelocity = properRounding(answer, self.sigFigs)

            self.record.append(1)

    def initialVelocityOne(self):
        '''
        Equation:

        Vf - (a * t) = Vi

        Solve for Initial Velocity with final velocity, acceleration, and time
        '''

        if checkValue(
                self.finalVelocity) and checkValue(
                self.acceleration) and checkValue(
                self.time) and self.initialVelocity is None:

            answer = self.finalVelocity - (self.acceleration * self.time)

            self.initialVelocity = properRounding(answer, self.sigFigs)

            self.record.append(2)

    def accelerationOne(self):
        '''
        Equation:

        (Vf - Vi) / t = a

        Solve for Acceleration with final velocity, initial velocity, and time
        '''

        if checkValue(
                self.finalVelocity) and checkValue(
                self.initialVelocity) and checkValue(
                self.time) and self.acceleration is None:

            answer = (self.finalVelocity - self.initialVelocity) / self.time

            self.acceleration = properRounding(answer, self.sigFigs)

            self.record.append(3)

    def timeOne(self):
        '''
        Equation:

        (Vf - Vi) / a = t

        Solve for Time with final velocity, initial velocity, and acceleration
        '''

        if checkValue(
                self.finalVelocity) and checkValue(
                self.initialVelocity) and checkValue(
                self.acceleration) and self.time is None:

            answer = (self.finalVelocity - self.initialVelocity) / \
                self.acceleration

            self.time = properRounding(answer, self.sigFigs)

            self.record.append(4)

    def deltaDistanceOne(self):
        '''
        Equation:

        Δx = Vi * t + 0.5 * a * t^2

        Solve for Delta Distance(Displacment) with initial velocity, acceleration, and time
        '''
        if checkValue(
                self.initialVelocity) and checkValue(
                self.acceleration) and checkValue(
                self.time) and self.deltaDistance is None:

            answer = (self.initialVelocity * self.time) + \
                (0.5 * self.acceleration * (self.time ** 2))

            self.deltaDistance = properRounding(answer, self.sigFigs)

            self.record.append(5)

    def finalVelocityTwo(self):
        '''
        Equation:

        Vf^2 = Vi^2 + 2 * a * Δx

        Solve for Final Velocity with initial velocity, acceleration, and delta distance
        '''

        if checkValue(
                self.initialVelocity) and checkValue(
                self.acceleration) and checkValue(
                self.deltaDistance) and self.finalVelocity is None:

            answer = (self.initialVelocity ** 2) + \
                (2 * self.acceleration * self.deltaDistance)

            answerSqrt = math.sqrt(abs(answer))

            answerCorrected = answerSqrt * (answer / abs(answer))

            self.finalVelocity = properRounding(answerCorrected, self.sigFigs)

            self.record.append(6)

    def initialVelocityTwo(self):
        '''
        Equation:

        Vf^2 - (2 * a * Δx) = Vi^2

        Solve for Initial Velocity with final velocity, acceleration, and delta distance
        '''

        if checkValue(
                self.finalVelocity) and checkValue(
                self.acceleration) and checkValue(
                self.deltaDistance) and self.initialVelocity is None:

            answer = (self.finalVelocity ** 2) - \
                (2 * self.acceleration * self.deltaDistance)

            answerSqrt = math.sqrt(abs(answer))

            answerCorrected = answerSqrt * (answer / abs(answer))

            self.initialVelocity = properRounding(
                answerCorrected, self.sigFigs)

            self.record.append(7)

    def accelerationTwo(self):
        '''
        Equation:

        ((Vf^2 - Vi^2) / 2) / Δx = a

        Solve for Acceleration with initial velocity, final velocity, and delta distance
        '''

        if checkValue(
                self.initialVelocity) and checkValue(
                self.finalVelocity) and checkValue(
                self.deltaDistance) and self.acceleration is None:

            answer = (((self.finalVelocity ** 2) -
                       (self.initialVelocity ** 2)) / 2) / self.deltaDistance

            self.acceleration = properRounding(answer, self.sigFigs)

            self.record.append(8)

    def deltaDistanceTwo(self):
        '''
        Equation:

        ((Vf^2 - Vi^2) / 2) / a = Δx

        Solve for Delta Distance(Displacment) with initial velocity, acceleration, and final velocity
        '''

        if checkValue(
                self.initialVelocity) and checkValue(
                self.acceleration) and checkValue(
                self.finalVelocity) and self.deltaDistance is None:

            answer = (((self.finalVelocity ** 2) -
                       (self.initialVelocity ** 2)) / 2) / self.acceleration

            self.deltaDistance = properRounding(answer, self.sigFigs)

            self.record.append(9)
