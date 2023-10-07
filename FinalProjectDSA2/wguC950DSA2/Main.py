# Import libraries and modules
import datetime
import Truck
from CreateHashTable import CreateHashMap
from fileUtils import readCsvFile, loadPackageData

# Read distance information from a CSV file
# (Time complexity: O(m * n), where m and n are the dimensions of the CSV file)
CSVDistanceList = readCsvFile("CSV/Distance_File.csv")
CSVAddressList = readCsvFile("CSV/Address_File.csv")


# Takes two integer arguments and returns a float
# (Time complexity: O(1)).
def distanceBetween(x: int, y: int) -> float:
    try:
        return float(CSVDistanceList[x][y])
    except ValueError:
        pass

    try:
        return float(CSVDistanceList[y][x])
    except ValueError:
        pass

    raise ValueError(f"No distance found between {x} and {y}.")


# Takes a string argument and returns an integer.
# Time complexity: O(a), where a is the number of rows in the CSVAddressList.
def extractAddressIndex(address: str) -> int:
    # Find the index of the address in the CSVAddressList
    for i, row in enumerate(CSVAddressList):
        if address == row[2]:
            return i

    # Return -1 if the address is not found
    return -1


# Creates a Truck object with the specified truckID, capacity, speed, package list, starting address, and starting time
# (Time complexity: O(1))
def createTruck(truckId: int, packageList: object, start_time: object) -> object:
    return Truck.Truck(truckId, capacity, speed, packageList, 0.0, startingAddress, start_time)


# `capacity` is an integer representing the amount of packages that can be put into a Truck.
# `speed` is an integer representing the rate at which the Truck can transfer packages.
# `startingAddress` is a string representing the starting address of the device.
# Initializing the capacity variable to 16
# (Time complexity: O(1))
capacity = 16
# Initializing the speed variable to 18
speed = 18
# Initializing the startingAddress variable to "4001 South 700 East"
startingAddress = "4001 South 700 East"

# Initialize package lists for each truck
# (Time complexity: O(1))
listForTruckOne = [1, 5, 8, 10, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
listForTruckTwo = [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
listForTruckThree = [2, 4, 7, 9, 11, 25, 28, 32, 33]

# Create three Truck objects with their initial package lists, starting addresses, and starting times
# (Time complexity: O(1))
truckOne: Truck = createTruck(1, listForTruckOne, datetime.timedelta(hours=8))
truckTwo: Truck = createTruck(2, listForTruckTwo, datetime.timedelta(hours=9, minutes=5))
truckThree: Truck = createTruck(3, listForTruckThree, datetime.timedelta(hours=10, minutes=20))

# Create an instance of CreateHashMap class and store it in package_hash_table
# (Time complexity: O(1))
package_hash_table: CreateHashMap = CreateHashMap()

# Load package data from CSV file into package_hash_table
# Time complexity: O(p), where p is the number of rows in the Package_File.csv
loadPackageData("CSV/Package_File.csv", package_hash_table)


# Simulates delivery of packages using the nearest-neighbor algorithm

def nearestNeighborDelivery(truck) -> None:
    """
    Simulates delivery of packages using the nearest-neighbor algorithm.
    time complexity of this function is O(n^2), where n is the number of packages in the truck.
    """
    # Create a list of undelivered packages
    # (Time complexity: O(n))
    undeliveredPackages = [package_hash_table.lookup(package_id) for package_id in truck.packages]

    # Clear packages from the truck object
    # (Time complexity: O(1))
    truck.packages.clear()

    # Loop until all packages are delivered
    # (Time complexity: O(n^2))
    while undeliveredPackages:
        # Initialize the closestDistance, closestPackage, and currentIndex variables
        closestDistance = float('inf')
        closestPackage = None
        currentIndex = extractAddressIndex(truck.address)

        # Iterate through each undelivered package
        # (Time complexity: O(n))
        for package in undeliveredPackages:
            # Calculate distance between the truck's current address and the package's address
            # (Time complexity: O(1))
            currentDistance = distanceBetween(currentIndex, extractAddressIndex(package.address))

            # If the current package is closer than the previous closest package, update the closestDistance and
            # closestPackage variables
            # (Time complexity: O(1))
            if currentDistance <= closestDistance:
                closestDistance = currentDistance
                closestPackage = package

        # Remove the closest package from list of undelivered packages
        # (Time complexity: O(n))
        undeliveredPackages.remove(closestPackage)

        # Update truck's attributes and closest package's delivery and departure time
        # (Time complexity: O(1))
        truck.mileage += closestDistance
        truck.address = closestPackage.address
        truck.timePlace += datetime.timedelta(hours=closestDistance / 18)
        closestPackage.delivery_time = truck.timePlace
        closestPackage.departure_time = truck.depart_time


# Call nearestNeighborDelivery function for each truck
# (Time complexity: O(k * n^2), where k is the number of trucks)
nearestNeighborDelivery(truckOne)
nearestNeighborDelivery(truckTwo)

# Set the departure time for truckThree to be the later of the two other truck times
# (Time complexity: O(1))
if truckOne.timePlace < truckTwo.timePlace:
    truckThree.depart_time = truckOne.timePlace
else:
    truckThree.depart_time = truckTwo.timePlace

nearestNeighborDelivery(truckThree)

# Start of main program-----------------------------------------------------------------------------------------
class Main:
    # Print initial messages
    # (Time complexity: O(1))
    print("WGUPS Delivery System!")
    # Prompt user to start program
    # (Time complexity: O(1))
    inputOne = input("To start please type the number '1' and press enter.")

    # If the user enters "1"
    # (Time complexity: O(1))
    if inputOne == "1":
        try:

            # Prompt user to enter time to check status of packages
            # (Time complexity: O(1))
            print("Mileage for each truck route is:")
            print("Truck One: " + str(int(truckOne.mileage)))
            print("Truck Two: " + str(int(truckTwo.mileage)))
            print("Truck Three: " + str(int(truckThree.mileage)))
            print("Total Milage: " + str(int(truckOne.mileage + truckTwo.mileage + truckThree.mileage)))
            userTime = input("Enter a time to check package(s) status in the following format, HH:MM:SS")

            # Split user's input into hours, minutes, and seconds
            # (Time complexity: O(1))
            (hour, minute, second) = userTime.split(":")

            # Convert input into a datetime.timedelta object
            # (Time complexity: O(1))
            convert_timedelta = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))

            # Ask the user if they want to see the status of all packages or only one
            # (Time complexity: O(1))
            secondInput = input(
                "For individual package status please type '2'. To view all packages status "
                "type 'all'.")

            if secondInput == "2":
                try:
                    # Prompt the user to enter a package ID and look up the corresponding package
                    # (Time complexity: O(1))
                    soloInput = input("Enter the numeric package ID")

                    if soloInput == "9":
                        print(
                            "-------------------------------------------------------------------------------------------------------------------------------------------")
                        print("PLEASE NOTE: Package ID:9's displays a wrong address until the time of 10:20.")

                    package = package_hash_table.lookup(int(soloInput))

                    # Update the package's status using the user's input time
                    # (Time complexity: O(1))
                    package.update_status(convert_timedelta)

                    # Print a header and the package's information
                    # (Time complexity: O(1))
                    print(
                        "-------------------------------------------------------------------------------------------------------------------------------------------")
                    print(
                        "PID  Address               City             State Zipcode    Deadline     Weight          Delivery Time          Departure Time   Status")
                    print(
                        "---------------------------------------------------------------------------------------------------------------------------------------------")
                    print(str(package))

                # Handle a ValueError if the user's input is invalid
                # (Time complexity: O(1))
                except ValueError:
                    print("Entry invalid. Please try again.")
                    exit()

            # If the user enters "all"
            # (Time complexity: O(n), where n is the number of packages)
            elif secondInput == "all":
                try:
                    print(
                        "-------------------------------------------------------------------------------------------------------------------------------------------")
                    print(
                        "PID  Address               City             State Zipcode    Deadline     Weight          Delivery Time          Departure Time    Status")
                    print(
                        "---------------------------------------------------------------------------------------------------------------------------------------------")

                    # Iterate through all packages and print their information
                    # (Time complexity: O(n))
                    for packageID in range(1, 41):
                        package = package_hash_table.lookup(packageID)

                        # Update each package's status using the user's input time and print its information
                        # (Time complexity: O(1))
                        package.update_status(convert_timedelta)
                        print(str(package))

                # Time complexity: O(1))
                except ValueError:
                    print("Entry invalid. Please try again.")
                    exit()

            # If the user enters something other than "solo" or "all", exit the program
            # (Time complexity: O(1))
            else:
                exit()

        # Handle a ValueError if the user's input time is invalid
        # (Time complexity: O(1))
        except ValueError:
            print("Time format invalid.  Please try again")
            exit()

    # If user enters something other than "1", exit program
    # (Time complexity: O(1))
    elif input != "1":
        print("Entry invalid. Please try again.")
        exit()
