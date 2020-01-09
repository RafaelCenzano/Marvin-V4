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
        self.magnitude1
        self.theta2 = theta2
        self.x2 = x2
        self.y2 = y2
        self.magnitude2
        self.resultingX
        self.resultingY
        self.resultingTheta
        self.resultingMagnitude

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
