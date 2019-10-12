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
            sigFigsList.append(self.count_sig_figs(self.initialVelocity))
        if self.finalVelocity != None:
            sigFigsList.append(self.count_sig_figs(self.finalVelocity))
        if self.time != None:
            sigFigsList.append(self.count_sig_figs(self.time))
        if self.accelertaion != None:
            sigFigsList.append(self.count_sig_figs(self.accelertaion))
        if self.deltaDistance != None:
            sigFigsList.append(self.count_sig_figs(self.deltaDistance))

        tempCount = sigFigsList[0]

        for item in sigFigsList:
            if item < tempCount:
                tempCount = item

        self.sigFigs = tempCount
        '''
        if self.initialVelocity != None:
            self.initialVelocity = self.properRounding(self.initialVelocity, self.sigFigs)
        if self.finalVelocity != None:
            self.finalVelocity = self.properRounding(self.finalVelocity, self.sigFigs)
        if self.time != None:
            self.time = self.properRounding(self.time, self.sigFigs)
        if self.accelertaion != None:
            self.accelertaion = self.properRounding(self.accelertaion, self.sigFigs)
        if self.deltaDistance != None:
            self.deltaDistance = self.properRounding(self.deltaDistance, self.sigFigs)
        '''
    def finalVelocityOne(self):
        '''
        Equation:

        Vf = Vi + a * t

        Solve for Final Velocity with initial velocity, acceleration, and time
        '''

        if self.checkValue(self.initialVelocity) and self.checkValue(self.accelertaion) and self.checkValue(self.time):

            answer = self.initialVelocity + (self.accelertaion * self.time)

            self.finalVelocity = round(answer, self.sigFigs)

    def deltaDistanceOne(self):
        '''
        Equation:

        Δx = Vi * t + 0.5 * a * t^2

        Solve for Delta Distance(Displacment) with initial velocity, acceleration, and time
        '''
        if self.checkValue(self.initialVelocity) and self.checkValue(self.accelertaion) and self.checkValue(self.time):

        	answer = (self.initialVelocity * self.time) + ( 0.5 * self.accelertaion * (self.time ** 2))

        	self.deltaDistance = round(answer, self.sigFigs)

    def checkValue(self, value):
        '''
        Check value to make sure its an int or float
        '''

        typeOfValue = type(value)

        if typeOfValue == int or typeOfValue == float:
            return True

        else:
            return False

    def count_sig_figs(self, value):
        '''
        This fucntion will count the sigfigs of a value
        '''

        if value == 0 or abs(value) == 9.8:
        	return 90000

        sig_fig_count = 0
        num_list = list(str(value))

        for index in range(len(num_list)):

            try:

                fig = int(num_list[index])

                if fig != 0:
                    sig_fig_count += 1

                elif self.check_zero_sig(index, num_list, sig_fig_count):
                    sig_fig_count += 1

            except:
                continue

        return sig_fig_count

    def check_zero_sig(self, index, num_list, sig_fig_count):
        '''
        Checks for significance in a zero from a list
        '''

        try:

            decimal = num_list.index('.')

            if index > decimal and sig_fig_count > 0:
                return True

        except:

            if index == 0 or index == len(num_list):
                return False

            new_index = index + 1

            if num_list[new_index] == '.' and sig_fig_count > 0:
                return True

            elif num_list[new_index] == '.' and sig_fig_count == 0:
                return False

            elif num_list[new_index] != '.' and sig_fig_count > 0:

                fig = int(num_list[new_index])

                if fig != 0:
                    return True

                else:
                    return self.check_zero_sig(new_index, num_list, sig_fig_count)

            elif num_list[new_index] != '.' and sig_fig_count == 0:

                fig = int(num_list[new_index])

                if fig != 0:
                    return True

                else:
                    return self.check_zero_sig(new_index, num_list, sig_fig_count)

            else:
                return False

    def convertToStringFromList(self, s): 
  
        # initialization of string to "" 
        new = ""
  
        # traverse in the string  
        for x in s:
            new += x
  
        # return string
        return new

    def splitString(self, word): 
        return [char for char in word] 

    def properRounding(self, value):

        splitValue = str(value).split('.')

        splitValueFirst = self.splitString(str(splitValue[0]))

        count = 0

        for nums in splitValueFirst:

            if nums != 0:
                count += 1

        if count > self.sigFigs:

            digitsToRemove = count - self.sigFigs

            tempCount = 0

            reverseSplitValueFirst = splitValueFirst

            reverseSplitValueFirst.reverse()

            for i in range(len(splitValueFirst)):

                if reverseSplitValueFirst[i] != '0' and tempCount <= digitsToRemove:

                    reverseSplitValueFirst[i] = '0'

            reverseSplitValueFirst.reverse()

            print(reverseSplitValueFirst)

            return float(self.convertToStringFromList(reverseSplitValueFirst))
        return 5

        #nonDecimalValues = len(splitValueFirst[0])

        #numToRoundTo = self.sigFigs - nonDecimalValues

if __name__ == '__main__':
    tester = Kinematics(initialVelocity=0, accelertaion=9.8, time=5.7373)
    tester.deltaDistanceOne()
    print(tester.sigFigs)
    print(tester.deltaDistance)
    num = tester.properRounding(5737390)
    print(type(num))
    print(num)