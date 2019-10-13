# Imports
import math

'''
Kinematics

Functions to solve time, velocity, accelertaion and distance with the other variables stated.
'''
class Kinematics:

    def __init__(self, initialVelocity=None, finalVelocity=None, time=None, accelertaion=None, deltaDistance=None):
        self.initialVelocity = initialVelocity
        self.finalVelocity = finalVelocity
        self.time = time
        self.accelertaion = accelertaion
        self.deltaDistance = deltaDistance

        sigFigsList = []

        if self.initialVelocity != None:
            sigFigsList.append(count_sig_figs(self.initialVelocity))
        if self.finalVelocity != None:
            sigFigsList.append(count_sig_figs(self.finalVelocity))
        if self.time != None:
            sigFigsList.append(count_sig_figs(self.time))
        if self.accelertaion != None:
            sigFigsList.append(count_sig_figs(self.accelertaion))
        if self.deltaDistance != None:
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

        if self.checkValue(self.initialVelocity) and self.checkValue(self.accelertaion) and self.checkValue(self.time) and self.finalVelocity == None:

            answer = self.initialVelocity + (self.accelertaion * self.time)

            self.finalVelocity = answer

    def deltaDistanceOne(self):
        '''
        Equation:

        Δx = Vi * t + 0.5 * a * t^2

        Solve for Delta Distance(Displacment) with initial velocity, acceleration, and time
        '''
        if self.checkValue(self.initialVelocity) and self.checkValue(self.accelertaion) and self.checkValue(self.time) and self.deltaDistance == None:

        	answer = (self.initialVelocity * self.time) + (0.5 * self.accelertaion * (self.time ** 2))

        	self.deltaDistance = answer

    def finalVelocityTwo(self):
        '''
        Equation:

        Vf^2 = Vi^2 + 2 * a * t^2

        Solve for Final Velocity with initial velocity, acceleration, and delta distance
        '''

        if self.checkValue(self.initialVelocity) and self.checkValue(self.accelertaion) and self.checkValue(self.deltaDistance) and self.finalVelocity == None:

            answer = (self.initialVelocity ^ 2) + (2 * self.accelertaion * self.deltaDistance)

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
    tester = Kinematics(initialVelocity=0, accelertaion=9.8, time=5.7373)
    tester.deltaDistanceOne()
    print(tester.sigFigs)
    print(tester.deltaDistance)