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

    def componentsOfOne():

        '''
        Equation:

        x1 = H * cos(Ѳ)

        y1 = H * sin(Ѳ)
        
        Solve for x and y components of vector using vector magnitude and vector angle
        '''

        if checkValue(
                self.magnitude1) and checkValue(
                self.theta1) and self.x1 is None:

            answer = self.magnitude1 * (math.degrees(math.cos(self.theta1)))

            self.x1 = properRounding(answer, self.sigFigs)

        if checkValue(
                self.magnitude1) and checkValue(
                self.theta1) and self.y1 is None:

            answer = self.magnitude1 * (math.degrees(math.sin(self.theta1)))

            self.y1 = properRounding(answer, self.sigFigs)

    def componentsOfTwo():

        '''
        Equation:

        x2 = H * cos(Ѳ)

        y2 = H * sin(Ѳ)
        
        Solve for x and y components of vector using vector magnitude and vector angle
        '''

        if checkValue(
                self.magnitude2) and checkValue(
                self.theta2) and self.x2 is None:

            answer = self.magnitude2 * (math.degrees(math.cos(self.theta2)))

            self.x2 = properRounding(answer, self.sigFigs)

        if checkValue(
                self.magnitude2) and checkValue(
                self.theta2) and self.y2 is None:

            answer = self.magnitude2 * (math.degrees(math.sin(self.theta2)))

            self.y2 = properRounding(answer, self.sigFigs)

    def componentsOfResult():

        '''
        Equation:

        xR = H * cos(Ѳ)

        yR = H * sin(Ѳ)
        
        Solve for x and y components of vector using vector magnitude and vector angle
        '''

        if checkValue(
                self.resultingMagnitude) and checkValue(
                self.resultingTheta) and self.resultingX is None:

            answer = self.resultingMagnitude * (math.degrees(math.cos(self.resultingTheta)))

            self.resultingX = properRounding(answer, self.sigFigs)

        if checkValue(
                self.magnitude2) and checkValue(
                self.theta2) and self.resultingY is None:

            answer = self.resultingMagnitude * (math.degrees(math.sin(self.resultingTheta)))

            self.resultingY = properRounding(answer, self.sigFigs)


