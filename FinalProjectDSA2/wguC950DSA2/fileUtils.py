# Reads package data from a CSV file and loads it into a hash table.
import csv
from typing import List
from Package import Package


# The readCsvFile function reads a CSV file and returns its contents as a list of lists.
# (Time complexity of O(N)), N is the number of rows in the CSV file.
def readCsvFile(filename: str) -> List[List[str]]:
    with open(filename) as csvfile:
        csv_data = csv.reader(csvfile)
        return list(csv_data)


# loadPackageData loads package data from a CSV file into a hash table.
# (Time complexity of O(N)), N is the number of packages in the CSV file.
def loadPackageData(filename: object, package_hash_table: object) -> object:
    with open(filename) as packageInfo:
        packageData = csv.reader(packageInfo)
        # Loop through each package entry in the CSV file
        for package in packageData:
            # Extract package details from the CSV file
            packageID = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZipcode = package[4]
            packageDeadlineTime = package[5]
            packageWeight = package[6]
            packageStatus = "At the Hub"

            # Create a Package object with the extracted details
            p = Package(packageID, packageAddress, packageCity, packageState, packageZipcode, packageDeadlineTime,
                        packageWeight, packageStatus)

            # Insert the Package object into the hash table using its ID as the key
            package_hash_table.insert(packageID, p)
