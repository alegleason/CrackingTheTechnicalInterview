## Assignment2 ME369P/ME396P
## Name: Alejandro Gleason Mendez
## EID : ag77698
## Section: Undergrad

## Fill in the class and functions below.
## Make sure your class runs with the tests in main
## You may use any imports, but do not use any import function for
##      norm calculation or matrix operations. Be wary of numpy.

import csv  # used to perform read operations smoothly to the StatePopulations.csv file
import math  # used to test rounding functions
import random  # used to pick random elements for the matrix to be created
from datetime import date  # used to get the current date and print it to the report
from copy import deepcopy  # used to copy class instances (objects)
random.seed(4)
'''
PROBLEM 1
Assume rounding will occur only at the end, and not in middle stages
Assume the default values are to be set in the function definition
Assume the print statements include the brackets in the assignment: < and > 
Undergraduates: Assume all parameters passed in are valid
Graduates: Assume you need to check the validity of passed in arguments
            NOTE: Print the following error message if no file is given: ERROR! No file passed.
            NOTE: For all other invalid parameters, use the default instead. 
Assume any non-rounded values should be formatted to two decimal places.
'''


def RepresentationAnalysis(file, constituentSize=0, delegationState="Wyoming", numOfDelegates=1, roundingFunc=round,
                           includeDC=False, includePR=False):
    ##Put code for question 1 in this function
    delegateToPopulationRatio = []
    results = []
    excluded = {"Puerto Rico", "District of Columbia"}
    totalStates = totalHouseMembers = countedStates = totalPopulation = peoplePerConstituency = 0

    # Helper functions
    def FindStatesPopulation(file, stateName):
        with open(file) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=',')
            for row in csvReader:
                if row[1] == stateName:
                    return row[2]

    if constituentSize == 0:
        # Determine base to the delegation state
        peoplePerConstituency = int(FindStatesPopulation(file, delegationState))
    elif constituentSize > 0:
        peoplePerConstituency = constituentSize

    if includePR is True:
        excluded.remove("Puerto Rico")
    if includeDC is True:
        excluded.remove("District of Columbia")

    with open(file) as csv_file:
        csvReader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        for row in csvReader:
            if row_count > 0:
                if row[1] not in excluded:
                    countedStates += 1
                    houseMembersPerState = int(row[2]) / peoplePerConstituency
                    houseMembersPerState *= numOfDelegates
                    houseMembersPerState = roundingFunc(houseMembersPerState)
                    results.append([row[1], houseMembersPerState])
                    totalPopulation += int(row[2])
                    totalHouseMembers += houseMembersPerState
                    totalStates += 1
                    delegateToPopulationRatio.append([row[1], int(row[2]) / (houseMembersPerState + 2)])
            row_count += 1
    today = date.today()
    print("Report Generation Date: <" + today.strftime("%B") + "> <" +
          today.strftime("%d") + ">, <" + today.strftime("%Y") + ">")
    print("The total population for the <" + str(totalStates) + "> states analyzed is <" + str(totalPopulation) + ">.")
    print("The total number of house members will be <" + str(totalHouseMembers) + ">." + "\n")
    print("The number of house representatives for each state are:")
    results.sort()
    for res in results:
        print(str(res[0]) + ": <" + str(res[1]) + ">")
    print("Target constituency: <{:0.2f}>".format(peoplePerConstituency / numOfDelegates))
    print("Realized constituency: <{:0.2f}>".format(totalPopulation / totalHouseMembers))
    delegateToPopulationRatio.sort(key=lambda x: x[1])
    print("Best represented state: <" + str(delegateToPopulationRatio[0][0]) + ">")
    print("Worst represented state: <" + str(delegateToPopulationRatio[-1][0]) + ">")


def roundNone(n):
    # 1) not rounded
    return int(n)


def round75(n):
    # 2) are rounded up if over .75 is the remainder and down if the remainder is at or below 0.75.
    return int(n) if n - int(n) < .75 else int(n + 1)


'''
PROBLEM 2
Assume all arguments will NOT be key words
Assume at least one argument will be passed
Assume that if two integer arguments are passed, the first is row and the
  second is column
Assume the default list of letters is ['a','b','c']
            NOTE: All characters have an ascii value associated with them
Assume the default format is '[' and ']'
Assume that if two strings are passed in as argument the first is the beginning 
  format string and the second is the ending format string
            NOTE: If one string is passed in, assume it is beginning and end
            but note the reversal in the instructions
Assume all matrix entries are a single digit (i.e. no ['cat','bat','mat'] lists)
'''


def MatrixGeneration(arg1, *argv):
    ## Put code for question 2 in this function
    # Helper functions
    def generateMatrix(numRows, numCols, charList):
        tempMat = []
        for _ in range(numRows):
            rowList = []
            for _ in range(numCols):
                rowList.append(random.choice(charList))
            tempMat.append(rowList)
        return tempMat

    def printMatrix(matrix, startChar, endChar):
        if not startChar and not endChar:
            startChar = "["
            endChar = "]"
        for row in matrix:
            print(startChar + " " + (' '.join(row)) + " " + endChar)

    cols = openChar = closeChar = None
    letters = ['a', 'b', 'c']
    rows = arg1
    tempArgs = []
    for arg in argv:
        tempArgs.append(arg)
    while tempArgs:
        if isinstance(tempArgs[0], int):
            cols = tempArgs[0]
        elif isinstance(tempArgs[0], list):
            letters = tempArgs[0]
        else:
            if not openChar:
                openChar = tempArgs[0]
            else:
                closeChar = tempArgs[0]
        tempArgs.pop(0)
    if not cols: cols = rows
    if openChar and not closeChar:
        closeChar = openChar[::-1]
    elif closeChar and not openChar:
        openChar = closeChar[::-1]
    if len(letters) == 2:
        # Overwrite the range of letters
        letters = list(map(chr, range(ord(letters[0]), ord(letters[1]) + 1)))
        # print(letters)

    mat = generateMatrix(rows, cols, letters)
    printMatrix(mat, openChar, closeChar)

    return


'''
PROBLEM 3
Assume if a kwarg is not present, you should create the basic matrix
Assume the style is default to random
Assume the set is default to [0, 1]
kwargs can be :
    n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
    i =>  number of rows     NOTE: If i is passed, assume j will be too
    j =>  number of columns
    range => [min, max] list
    set   => [number1, ..., numberN]
                NOTE: If set is specified, use that over range
                NOTE: If not specified, assume the set is the range
    style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                NOTE: Any non-square matrix will be random
                NOTE: Different styles will always be square matrices
                NOTE: Use zeroes in the stylized matrices even if not in the given numbers
    format1 => string for formating 1st  element of each row
    format2 => string for formating last element of each row
                NOTE: If both formats are '', assume the default of no format
                NOTE: If one format is '', assume the other format is a string that is reversable
Assume all matrix entries are a single digit (i.e. no 10's 100's, etc)
'''


class myAwesomeMatrix:
    ## Put code for question 3 in this function
    ## print out matrix with newlines between rows
    ## print out elements in rows 1 space apart, with space between the format strings and the values
    # Class properties
    _n = None
    _i = None
    _j = None
    _range = None
    _set = None
    _style = None
    _format1 = None
    _format2 = None
    mat = None

    def get_i(self):
        return self._i

    def get_j(self):
        return self._j

    def __init__(self, **kwargs):
        # Set properties
        self._n = kwargs.get('n', 4)
        self._i = kwargs.get('i', None)
        self._j = kwargs.get('j', None)
        self._range = kwargs.get('range', ['0', '1'])
        self._set = kwargs.get('set', None)
        self._style = kwargs.get('style', 'random')
        self._format1 = kwargs.get('format1', "")
        self._format2 = kwargs.get('format2', "")
        if not self._i and not self._j:
            self._i = self._j = self._n
        if not self._set:
            # Adjust range
            self._range = list(map(chr, range(ord(str(self._range[0])), ord(str(self._range[1])) + 1)))
        else:
            # Transform set to chars
            self._range = list(map(str, self._set))
        if self._format1 and not self._format2:
            self._format2 = self._format1[::-1]
        elif self._format2 and not self._format1:
            self._format1 = self._format2[::-1]

        if self._style == "random" or self._i != self._j:
            self.generateRandomMatrix()
        elif self._style == "diagonal":
            self.generateDiagonalMatrix()
        elif self._style == "upper":
            self.generateUpperDiagonalMatrix()
        elif self._style == "lower":
            self.generateLowerDiagonalMatrix()
        elif self._style == "symmetric":
            self.generateSymmetricMatrix()

    # Overriding print() method
    def __str__(self):
        retString = ""
        if self._format1 == "" and self._format2 == "":
            for row in self.mat:
                retString += str((' '.join(row))) + "\n"
        else:
            for row in self.mat:
                retString += self._format1 + " " + str((' '.join(row))) + " " + self._format2 + "\n"
        return retString

    def generateRandomMatrix(self):
        tempMat = []
        for _ in range(self._i):
            rowList = []
            for _ in range(self._j):
                rowList.append(random.choice(self._range))
            tempMat.append(rowList)
        self.mat = tempMat

    def generateDiagonalMatrix(self):
        tempMat = self.generateZeroMatrix()
        for i in range(self._i):
            tempNum = random.choice(self._range)
            while tempNum == '0':
                tempNum = random.choice(self._range)
            tempMat[i][i] = tempNum
        self.mat = tempMat

    def generateUpperDiagonalMatrix(self):
        tempMat = self.generateZeroMatrix()
        for i in range(self._i):
            for j in range(i, self._j):
                tempNum = random.choice(self._range)
                while tempNum == '0':
                    tempNum = random.choice(self._range)
                tempMat[i][j] = tempNum
        self.mat = tempMat

    def generateLowerDiagonalMatrix(self):
        tempMat = self.generateZeroMatrix()
        for i in range(self._i):
            for j in range(i + 1):
                tempNum = random.choice(self._range)
                while tempNum == '0':
                    tempNum = random.choice(self._range)
                tempMat[i][j] = tempNum
        self.mat = tempMat

    def generateSymmetricMatrix(self):
        tempMat = self.generateZeroMatrix()
        # Generate one side
        for i in range(self._i):
            for j in range(i + 1):
                tempNum = random.choice(self._range)
                while tempNum == '0':
                    tempNum = random.choice(self._range)
                tempMat[i][j] = tempNum
        # Copy to the other side
        for i in range(self._i):
            for j in range(i, self._j):
                tempMat[i][j] = tempMat[j][i]

        self.mat = tempMat

    def generateZeroMatrix(self):
        tempMat = []
        for _ in range(self._i):
            rowList = []
            for _ in range(self._j):
                rowList.append('0')
            tempMat.append(rowList)
        return tempMat

    def Add(self, otherMatrix):
        tempMat = deepcopy(self)
        minRow = min(self._i, otherMatrix.get_i())
        minCol = min(self._j, otherMatrix.get_j())
        for row in range(minRow):
            for col in range(minCol):
                temp = int(self.mat[row][col]) + int(otherMatrix.mat[row][col])
                tempMat.mat[row][col] = str(temp)
        return tempMat

    def __add__(self, otherMatrix):
        tempMat = deepcopy(self)
        minRow = min(self._i, otherMatrix.get_i())
        minCol = min(self._j, otherMatrix.get_j())
        for row in range(minRow):
            for col in range(minCol):
                temp = int(self.mat[row][col]) + int(otherMatrix.mat[row][col])
                tempMat.mat[row][col] = str(temp)
        return tempMat

    def __lt__(self, other):
        return self.get1Norm() < other.get1Norm()

    def get1Norm(self):
        # The 1-norm is the maximum of the column sums
        maxSum = -1
        for col in range(self.get_j()):
            currSum = 0
            for row in range(self.get_i()):
                currSum += abs(int(self.mat[row][col]))
            maxSum = max(maxSum, currSum)
        return maxSum


if __name__ == '__main__':
    ###Problem 1
    # Testing the defaults
    print('1st Test')
    RepresentationAnalysis(file='StatePopulations.csv')

    # Testing roundingFunc
    print('\n2nd Test')
    RepresentationAnalysis(file='StatePopulations.csv', constituentSize=150000)

    print('\n3rd Test')
    RepresentationAnalysis(file='StatePopulations.csv', constituentSize=150000,
                           roundingFunc=math.ceil)
    print('\n4th Test')
    RepresentationAnalysis(file='StatePopulations.csv', constituentSize=150000,
                           roundingFunc=math.floor)

    # Testing the delegates
    print('\n5th Test')
    RepresentationAnalysis(file='StatePopulations.csv', delegationState="Wyoming",
                           numOfDelegates=2)
    print('\n6th Test')
    RepresentationAnalysis(file='StatePopulations.csv', delegationState="Vermont",
                           numOfDelegates=2)
    print('\n7th Test')
    RepresentationAnalysis(file='StatePopulations.csv', delegationState="Texas",
                           numOfDelegates=50)
    print('\n8th Test')
    RepresentationAnalysis(file='StatePopulations.csv', delegationState="California",
                           numOfDelegates=50)

    # Testing DC and PR
    print('\n9th Test')
    RepresentationAnalysis(file='StatePopulations.csv')
    print('\n10th Test')
    RepresentationAnalysis(file='StatePopulations.csv', includePR=True, includeDC=False)
    print('\n11th Test')
    RepresentationAnalysis(file='StatePopulations.csv', includePR=False, includeDC=True)
    print('\n12th Test')
    RepresentationAnalysis(file='StatePopulations.csv', includePR=True, includeDC=True)

    ###This section is for graduate students, undergrads may comment it out
    # Testing custom rounding functions
    print('\nNo rounding test')
    RepresentationAnalysis(file='StatePopulations.csv', constituentSize=150000,
                           roundingFunc=roundNone)
    print('\n75 percent rounding test')
    RepresentationAnalysis(file='StatePopulations.csv', constituentSize=150000,
                           roundingFunc=round75)

    ###Problem 2
    # Testing the letter matrices
    print("\n\nTesting the MatrixGeneration function\n")
    print('1st Test')
    MatrixGeneration(4)

    print('\n2nd Test')
    MatrixGeneration(4, 3)

    print('\n3rd Test')
    MatrixGeneration(2, 5)

    print('\n4th Test')
    MatrixGeneration(1, 7)

    print('\n5th Test')
    MatrixGeneration(7, 1)

    print('\n6th Test')
    MatrixGeneration(4, 4, '<', '>')

    print('\n7th Test')
    MatrixGeneration(3, 3, '+-+-')

    print('\n8th Test')
    MatrixGeneration(3, 3, ['a', 'z', 'c'])

    print('\n9th Test')
    MatrixGeneration(7, 3, ['d', 'p'], '+-+-')

    ###Problem 3
    # Testing matrix constructions
    print("\n\nTesting the myAwesomeMatrix class\n")
    print('1st Test')
    m = myAwesomeMatrix()
    print(m)

    print('\n2nd Test')
    kwargs = {'n': 4}
    print(myAwesomeMatrix(**kwargs))

    print('\n3rd Test')
    kwargs = {'i': 3, 'j': 4}
    print(myAwesomeMatrix(**kwargs))

    print('\n4th Test')
    kwargs = {'n': 6, 'range': [1, 3], 'format1': '[', 'format2': ']'}
    print(myAwesomeMatrix(**kwargs))

    print('\n5th Test')
    kwargs = {'n': 2, 'set': [1, 2, 3], 'style': 'lower'}
    print(myAwesomeMatrix(**kwargs))

    print('\n6th Test')
    kwargs = {'n': 4, 'format1': 'cool', 'format2': 'cool'}
    print(myAwesomeMatrix(**kwargs))

    print('\n7th Test')
    kwargs = {'n': 4, 'style': 'diagonal', 'set': [1]}
    print(myAwesomeMatrix(**kwargs))

    print('\n8th Test')
    kwargs = {'n': 5, 'set': [5, 7, 8, 3, 2, 4, 9], 'format1': 'ed!#', 'style': 'symmetric'}
    print(myAwesomeMatrix(**kwargs))

    # Testing Addition with Add method
    print('\nAdd Methods')
    kwargs = {'n': 4, 'style': 'upper', 'set': [4, 3, 6, 7], 'format2': '@-!-'}
    m2 = myAwesomeMatrix(**kwargs)
    print('m')
    print(m)
    print('m2')
    print(m2)
    print('m2.Add(m)')
    print(m2.Add(m))

    # Testing Addition with overloaded add (+)
    print('m2 + m')
    print(m2 + m)

    # Testing overloaded '<' operator
    kwargs = {'n': 4, 'style': 'upper', 'set': [4, 3, 6, 7]}
    m2 = myAwesomeMatrix(**kwargs)
    print('m2')
    print(m2)
    kwargs = {'n': 6, 'set': [0, 1]}
    m = myAwesomeMatrix(**kwargs)
    print('m')
    print(m)
    print('It is', m < m2, 'that m is less than m2', end='\n\n')

    print("Done")

    # You can do any testing you want here
    # Anycode you run here will not run when being graded...
