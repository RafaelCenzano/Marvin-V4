# Imports
import math
from marvin.helpers.physics.numberProcessing import count_sig_figs, properRounding, checkValue, cleanValue

'''
Kinematics

Functions to solve time, velocity, accelertaion and distance with the other variables stated.
'''


class Vectors:

    def __init__(
            self,
            theta1=None,
            x1=None,
            y1=None,
            magnitude1=None,
            theta2=None,
            x2=None,
            y2=None,
            magnitude2=None,
            resultingX=None,
            resultingY=None,
            resultingTheta=None,
            resultingMagnitude=None):

        self.theta1 = theta1
        self.x1 = x1
        self.y1 = y1
        self.magnitude1 = magnitude1
        self.theta2 = theta2
        self.x2 = x2
        self.y2 = y2
        self.magnitude2 = magnitude2
        self.resultingX = resultingX
        self.resultingY = resultingY
        self.resultingTheta = resultingTheta
        self.resultingMagnitude = resultingMagnitude

        sigFigsList = []

        if self.theta1 is not None:
            sigFigsList.append(count_sig_figs(self.theta1))
        if self.x1 is not None:
            sigFigsList.append(count_sig_figs(self.x1))
        if self.y1 is not None:
            sigFigsList.append(count_sig_figs(self.y1))
        if self.magnitude1 is not None:
            sigFigsList.append(count_sig_figs(self.magnitude1))
        if self.theta2 is not None:
            sigFigsList.append(count_sig_figs(self.theta2))
        if self.x2 is not None:
            sigFigsList.append(count_sig_figs(self.x2))
        if self.y2 is not None:
            sigFigsList.append(count_sig_figs(self.y2))
        if self.magnitude2 is not None:
            sigFigsList.append(count_sig_figs(self.magnitude2))
        if self.resultingTheta is not None:
            sigFigsList.append(count_sig_figs(self.resultingTheta))
        if self.resultingX is not None:
            sigFigsList.append(count_sig_figs(self.resultingX))
        if self.resultingY is not None:
            sigFigsList.append(count_sig_figs(self.resultingY))
        if self.resultingMagnitude is not None:
            sigFigsList.append(count_sig_figs(self.resultingMagnitude))

        tempCount = sigFigsList[0]

        for item in sigFigsList:
            if item < tempCount:
                tempCount = item

        self.sigFigs = tempCount

        self.record = []

    def calculations(self):
        count = 0

        while(checkValue(self.theta1) == False or checkValue(self.x1) == False or checkValue(self.y1) == False or checkValue(self.magnitude1) == False or checkValue(self.theta2) == False or checkValue(self.x2) == False or checkValue(self.y2) == False or checkValue(self.magnitude2) == False or checkValue(self.resultingTheta) == False or checkValue(self.resultingX) == False or checkValue(self.resultingY) == False or checkValue(self.resultingMagnitude) == False):
            if count > 20:
                break
            count += 1

        self.theta1 = cleanValue(self.theta1)
        self.x1 = cleanValue(self.x1)
        self.y1 = cleanValue(self.y1)
        self.magnitude1 = cleanValue(self.magnitude1)
        self.theta2 = cleanValue(self.theta2)
        self.x2 = cleanValue(self.x2)
        self.y2 = cleanValue(self.y2)
        self.magnitude2 = cleanValue(self.magnitude2)
        self.resultingX = cleanValue(self.resultingX)
        self.resultingY = cleanValue(self.resultingY)
        self.resultingTheta = cleanValue(self.resultingTheta)
        self.resultingMagnitude = cleanValue(self.resultingMagnitude)

    def xComponent(magnitude, theta):
        '''
        Equation:

        x = H * cos(Ѳ)

        Solve for x component of vector using vector magnitude and vector angle
        '''

        answer = magnitude * (math.degrees(math.cos(theta)))

        return properRounding(answer, self.sigFigs)

    def yComponent(magnitude, theta):
        '''
        Equation:

        y = H * sin(Ѳ)

        Solve for y component of vector using vector magnitude and vector angle
        '''

        answer = magnitude * (math.degrees(math.sin(theta)))

        return properRounding(answer, self.sigFigs)

    def vectorMagnitude(x, y):
        '''
        Equation:

        H = (x^2 + y^2)^(1/2)

        Solve for magnitude of vector using vector x and y components
        '''

        answer = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        return properRounding(answer, self.sigFigs)

    def vectorAngle(x, y):
        '''
        Equation:

        Ѳ = tan^-1(x/y)

        Solve for theta of vector using vector x and y components
        '''

        answer = math.degrees(math.atan(x / y))

        return properRounding(answer, self.sigFigs)