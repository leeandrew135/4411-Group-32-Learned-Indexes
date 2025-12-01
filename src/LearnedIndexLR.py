# LearnedIndexLR.py
# IMPLEMENTS LINEAR REGRESSION FOR A SINGLE COUNTRY
# https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/
# https://www.w3schools.com/python/python_ml_linear_regression.asp

class LearnedIndexLR:
    def __init__(self, countryCode: str, countryData: list):
        self.countryCode = countryCode
        self.data = countryData # CONSIDER SORTING IN ASC. ORDER

        # THESE WILL BE USE FOR OUR [mx + b] LINEAR REGRESSION
        self.m = 0
        self.b = 0

        self.maxError = 0

    # LOAD THEN SORT INTO KEYS AND VALUES
    def trainModel(self):
        # SEPARATE THE YEARS AND VALUES
        dataYears, dataValues = zip(*self.data)

        # CALCULATE AVERAGES FOR LINEAR REGRESSION FORMULA
        numberOfPoints = len(dataYears)
        avgX = sum(dataYears) / numberOfPoints
        avgY = sum(dataValues) / numberOfPoints

        # CALCULATE THE SLOPE


        # CALCULATE THE INTERCEPT 



    # USE [year] TO PREDICT POSITION BY [mx + b]
    def predict(self, year: int):
        returnValue = self.m * year + self.b
        return returnValue

    def printModel(self):
        pass