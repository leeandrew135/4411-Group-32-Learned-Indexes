# LRManager.py
# PROCESSES THE CSV INTO INSTANCES OF MODELS FOR EACH COUNTRY

import sys
import csv

class LRManager:
    # CONSTRUCTOR
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.dataByCountry = {}
        self.models = {}

    # PROCESSES THE CSV INPUT FILE,
    # SORTED BY COUNTRY NAME, THEN DESCENDING YEAR (2024, THEN 2023, ...)
    def processInputFile(self):
        with open(self.filepath, "r") as inputFile:
            input = csv.reader(inputFile)

            for row in input:
                # FOR NOW, WILL SKIP OVER ROWS WITH LESS THAN 4 ELEMENTS
                if len(row) < 4 or row[0] == "Country":
                    continue

                # IF ROW HAS 4 ELEMENTS
                # PROCEED BY EXTRACTING DATA

                countryName = row[0].strip() # UNUSED, BUT CAN ADD BACK LATER
                countryCode = row[1].strip()
                inputYear = row[2].strip()
                inputValue = row[3].strip()

                # IF inputValue == "", THEN continue BECAUSE OF BLANK LINES
                if inputValue == "":
                    continue

                # PROCESS INTO CORRECT FORMAT
                year = int(inputYear)
                value = float(inputValue)

                # ADD COUNTRY CODE IF DOES NOT ALREDAY EXIST
                if countryCode not in self.dataByCountry:
                    self.dataByCountry[countryCode] = []

                # ADD TO LIST
                self.dataByCountry[countryCode].append((year, value))
                
    # OUTPUT dataByCountry TO COMMAND LINE
    def printAllData(self):
        print("DATA BY COUNTRY")

        for countryCode, dataList in self.dataByCountry.items():
            print("\n" + countryCode + ":")
            for (year, value) in dataList:
                print("\t" + str(year) + " -> " + str(value))

    # GETS THE DATA OF A SINGLE COUNTRY BY COUNTRY CODE
    def getCountryData(self, countryCode: str):
        returnValue = self.dataByCountry.get(countryCode, [])
        return returnValue

# MAIN
if __name__ == "__main__":
    # GET INPUT FILE FROM COMMAND LINE
    filepath = sys.argv[1]

    # CREATE MANAGER INSTANCE
    manager = LRManager(filepath)

    # CALL METHODS HERE
    manager.processInputFile()
    # manager.printDataByCountry()

    canadaData = manager.getCountryData("CA")
    print(canadaData)