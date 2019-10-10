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

	def finalVelocityOne(self):
		'''
		Equation:

        Vf = Vi + a * t

        Solve for Final Velocity with initial velocity, acceleration, and time
        '''

        if self.checkValue(self.initialVelocity) and self.checkValue(self.accelertaion) and self.checkValue(self.time):

            answer = self.initialVelocity + (self.accelertaion * self.time)

            self.finalVelocity = answer

    def deltaDistanceOne():
    	'''
		Equation:

        Δx = Vi * t + 0.5 * a + t^2

        Solve for Delta Distance(Displacment) with initial velocity, acceleration, and time
        '''

    def checkValue(self, value):
        '''
        Check value 
        '''

        typeOfValue = type(value)

        if typeOfValue == int or typeOfValue == float:

            return True

        else:

            return False
