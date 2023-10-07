# Traveling-Salesman Problem
Identify a named self-adjusting algorithm (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”) that you used to create your program to deliver the packages.

I’ve chosen to use the “Nearest Neighbor algorithm” for this project in order to deliver packages.  
The Nearest Neighbor algorithm is not difficult to implement since it only requires calculating distances between points and choosing the closest point that has not yet been visited. This makes it a reasonable choice for developers who would like to create a working solution quickly without delving into more complex algorithms.

Overview of Project:
1.  Explain the algorithm’s logic using pseudocode.

The WGUPS program simulates a package delivery system. It reads package data and distance data from CSV files, creates trucks with capacities and speeds, assigns packages to each truck, then uses the nearestNeighbor (NN) algorithm, and allows users to check the status of the package at any given time.

Define classes for Package, Truck, and CreateHashmap.  Assign packages to each truck.
Class Package
Package class represents a package that is being delivered by the WGUPS delivery system.  Each package has an ID, address, city state, zip code, deadline time, weight status, departure time, delivery time.
Int, constructor for initializing package objects and str method for returning a string of the package object
update_status method updates the status of a package based on the provided time.
Handles the special instruction for package #9.  Checks to see If the package id is #9 and the current time is between 10:30am and 5:00pm then it updates the package address to the correct address.
If the delivery time is not “None” and has passed, then the package status gets set to “Delivered”
If the departure time is not “None” and has passed, then the package status gets updated to “En Route”
If the delivery time and departure time are “None” or in in the future, then the package status is set to “At the Hub”
Class Truck: There will be three trucks total, and two drivers.
Represents a truck that is used for delivering packages.  Each truck has an ID, capacity, speed, list of package IDs, current mileage, current address, departure time.
Int constructor for initializing truck objects. and str method for returning a formatted string of the truck object.
Class CreateHashMap
A custom implementation of a hash map(hash table). 
Used for  insert,update, lookup, removal of key-value pairs.
For Package ID and corresponding package object
Int constructor for initializing hash map
Insert method for adding a new key-value pair
Lookup method for finding the value associated with a given key
Hash_remove method for removing a key-value pair from the hash map.
Define then Import libraries and modules
CSV, datetime, Package, createTruck, CreateHashMap, fileUtils, list readCsFile, loadPackageData.
readCsvFIle(filename:str)-> List[List[str]]:
Takes a filename string as input and reads the CSV file
Uses the csv.reader object and returns data as a list of lists 
loadPackageData(filename: object, package_hash_table:object)-> object:
Takes a filename and package hash table as input. 
Opens the file then reads the package using the csv.reader object and inserts them into the package_hash_table using their package ID’s as keys
extractAddressIndex(address:str)-> int:
Takes an address string as input and searches for it in the “CSVAddressList” if the address is found then it returns the index of the row containing the address.
createTruck(truckId: int, packageList:object, start_time:object)->object:
Takes a truckID, package list, start time as input.
Creates a new “Truck” object with given input values and returns it.
Initializes the truck’swith values such as capacity, speed, package list, mileage, starting address, and starting time.
Read CSV files then load package data into the hash table.
Open CSV files with the given file name
Read the CSV data
For each package
Extract package details (ID, address, city, state, etc.)
Create new package object with the data
Insert the package object into package_hash_table
Define functions for calculating distance between two addresses.
distanceBetween(x:int, y:int)-float:
Takes two integers x and y as input and returns the distance between the two points which correspond to the indices in the “CSVDistanceList” It retrieves the distance value and converts it into a float.  
extractAddressIndex(address:str)-> int:
Takes an address string as input and searches for it in the “CSVAddressList” if the address is found then it returns the index of the row containing the address.
Define and Initialize package lists for the trucks, create trucks with package lists, and load package data into the data into the hash table.
Initialize capacity, speed, and starting address
Create the lists for each truck’s packages
Create 3 truck objects with the lists, starting address, and starting times.
Define and Implement the nearest-neighbor (NN) algorithm for each truck 
nearestNeighborDelivery(truck):
Simulates the delivery of packages using the “NN” algorithm.
Takes a truck object as input
Modifies the truck’s and package attributes for the delivery process.
Calculates the closest packages compared to the truck’s current location, delivers to the NN location, then updates the truck’s and continues until all packages are delivered
Call nearestNeighborDeliver function for each truck.
Define and create the main program loop.  Make a user interface for users to check the status of the packages at any specific time including:
Print initial (WGUPS) message
Prompt user to start
Prompt user to enter time to check package status
Ask user to choose between checking individual or all package status’
Display the chosen package(s) status based on user input
If user enters invalid input, exit the program
Handle exceptions for invalid input.
	

# initialize trucks: 
trucks = initializeTrucks()

# initialize package hash table: 
package_hash_table = initializePackageHashTable()

# load package data from CSV file into hash table: loadPackageDataFromCsv(package_hash_table)

# nearestNeighborDelivery(truck): 
for truck in trucks: nearest_neighbor_delivery(truck)
def nearestNeighborDelivery(truck):
	undeliveredPackages = createUndeliveredPackagesList()
	clearPackagesFromTruck(truck)

	while undeliveredPackages:
    	closestPackage = findClosestPackage(truck.location, undeliveredPackages)
    	undeliveredPackages.remove(closestPackage)
    	updateTruckAttributes(truck, closestPackage)
    	updateClosestPackageDeliveryAndDepartureTime(closestPackage, truck)

# main program: 
main_program():
	inputTime = input("Enter the time to check package(s) status: ")
	packageStatusChoice = input("Choose individual package status (1) or all packages status (2): ")

	if packageStatusChoice == '1':
    	package_id = input("Enter the package ID: ")
    	updatePackageStatusUsingInputTime(package_hash_table[package_id], inputTime)
    	printPackageInformation(package_hash_table[package_id])
	elif packageStatusChoice == '2':
    	for packageId, package in package_hash_table.items():
        	updatePackageStatusUsingInputTime(package, inputTime)
        		printPackageInformation(package)



I have used the Nearest Neighbor Algorithm (NN) to find the closest point to a given point from a list of points.  Here is the Pseudocode for the NN algorithm based on my program:  

The function “nearestNeighborDeliver(truck)” takes a “Truck” object as input and models the delivery of packages using the NN algorithm.  It initializes the list of undelivered packages using the trucks current package list and clears the truck’s package list.


Initialize the list of undelivered packages using the truck’s current package list.
undeliveredPackages = [package_hash_table.lookup(package_id) for package_id in truck.packages]
Clear the truck’s package list
truck.packages.clear()






In the while loop, as long as there are undelivered packages, the NN algorithm finds the closest package to the current address by iterating through the list of undelivered packages and finds the one with the minimum distance. (for each package, the function calculates the distance between the truck’s current address and the package’s address using the extractAddressIndex() and the distanceBetween()) The distance is calculated using ‘distanceBetween()’ If the current package is closer/smaller than the previous found closest package’s distance, the function then updates the closestDistance and closestPackage variables with the current package’s distance and the current package.  After going through all the undelivered packages, the function returns the closestPackage that is the next package to deliver.

While the list of undelivered packages is not empty:
While undeliveredPackages:
Set the closest distance to a number to infinity, 
Set closest package to None, and the current Index to the truck’s current address index
closestDistance = float(‘inf’)
Initialize the closest distance to infinity.
closestPackage = None
Initialize the closest Package to None
currentIndex = extractAddressIndex(truck.address)
Initialize the currentIndex to the index of the truck’s current address in the CSV_AddressList.

For each package in the undelivered package list
Iterate through each undelivered package in the undeliveredPackages list.
For package in undeliveredPackages:
Calculate the distance between the truck’s current address and the packages address.
currentDistance = distanceBetween(currentIndex, extractAddressIndex(package.address))
If the current package is closer(smaller) than the previously found closest package distance, the function updates the closest distance and closest package with the current package’s distance and the current package.
If currentDistance <= closestDistance:
ClosestDistance = currentDistance
closestPackage = package


After finding the closest package, it is removed from the list of undelivered packages, and the truck’s attributes are updated.  The delivery time and departure time of the closest package are also updated.

Remove the closest package from the list of packages.
undeliveredPackages.remove(closestPackage)
Update the truck’s attributes and closest package’s delivery and departure time.
Truck.mileage += closest distance
Truck.address = closestPackage.address
truck.timePlace += datetime.timedelta(hours=closestDistance / 18)
closestPackage.delivery_time = truck.timePlace
closestPackage.delivery_time = truck.depart_time

The algorithm continues to find and deliver the closest package until all packages are delivered.

#Programming environment you used to create the Python application.

I developed the program using PyCharm, an Integrated Development Environment (IDE) created by the company “JetBrains” which supports Python 3 development.  The program was written in Python 3 and utilized PyCharm’s features such as the console, debugger, and built-in terminal for code execution.  The development was carried out on an older Windows Surface 7 computer.
To start the program, execute the Main.py file in the “WGUC950DSA2” folder that contains all source code.


3. Space-time complexity of each major segment of the program, and the entire program, using big-O notation.

I’ve listed the time-space complexity in the comments throughout the entire program.

The space complexity of the program is governed by the space complexity of the package hash table (O(p)). The space complexity is O(p + k + n).

The time complexity of nearestNeighborDelivery(truck) for the entire program is O(k * n^2) where k is the number of trucks, and the time complexity of the main program is O(n), so the time complexity is O(k * n^2 + n).

4. Capability of solution to scale and adapt to a growing number of packages.

The hash table data structure is used to retrieve the package data. It allows the program to store and retrieve package data efficiently.  When the number of packages increases, the program’s performance will not take much of a performance hit.  

The hash table has a hash function which converts keys into indices of an array.  The hash function then maps each key to a unique index in the array, and the value is stored at the index.  Since the hash function is designed to distribute keys evenly across the array, and incorporates chaining which handles collisions that might occur during the hash table operation, the time complexity for most operations on elements in the hash table (inserting, retrieving, updating, deleting) are constant or O(1) on average.  This means that the program can efficiently store and retrieve package data regardless of the size of input, allowing the program to scale and adapt to a growing number of packages.

The nearest neighbor algorithm is used to determine the optimal delivery route for each truck.  It aims to minimize the total distance traveled by visiting the closest unvisited package location from the current location until all packages are delivered.  As packages are added, the algorithm’s growth and the program’s ability to scale are impacted by many factors.

The nearest neighbor algorithm has a time complexity of O(n^2), where n is the number of packages in the truck.  This means that the algorithm’s growth is proportional to the square of the number of packages that are added.  As the number of packages increases, the problem of finding an optimal route becomes more complex and less efficient.  The nearest neighbor algorithm may not always find an optimal solution.  As the program scales to include more packages, there will be a point where another algorithm such as the “Genetic” algorithm would be better suited.

As the truck capacity and the number of trucks increases, the program must also be changed to include more trucks as well as trucks with larger capacities to ensure efficient package delivery.
The submission describes the hash table's capability to scale. The ability for the entire program to scale, including the algorithm's growth as packages are added, is not observed.




	
5. Why the software is efficient and easy to maintain.

The use of separate functions and classes for each part of the program, makes the program modular and easy to understand. The program also uses a hash table to store package information, which allows for efficient lookups, insertions, updates, and deletions (see 4. Above for detailed explanation on the hash table data structure) while also allowing the program to scale and adapt to a growing number of packages.
6. Strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).
	
Strengths:
The hash table has great performance for lookups, insertions, updates and deletions (O(1)).
The use of chaining in the hash table reduces collisions and improves performance.
The self adjusting hash table is able to handle any data type that can be hashed without requiring much modification to the code.

Weaknesses:
If the hash function does not distribute the keys in a uniform distribution, or the hash table becomes full. The hash table may require a larger amount of memory that the hardware might not have.
As the number of keys in the hash table grows, it may become necessary to resize the table to maintain performance.  Rehashing all the existing keys, and inserting them into a larger table can become a complex and time-consuming process.

C.  Write an original program to deliver all the packages, meeting all requirements, using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and the “WGUPS Package File.”
	
My program file “WGUC950DSA2” was uploaded along with this write up.

Create an identifying comment within the first line of a file named “main.py” that includes your first name, last name, and student ID.
#Travis Jorel Hipolito
#Student ID: 008276777

Include comments in your code to explain the process and the flow of the program.
Comments are included in the program and explains the process/flow of the application.
Below are screenshots showing the package 9 address change to 410 State St., Salt Lake City, UT 8411  at 12:30


10:40




Prior to the address fix 9:00 the address isn’t changed until 10:20



D. Identify a self-adjusting data structure, such as a hash table, that can be used with the algorithm identified in part A to store the package data.

createHashMap class is the self-adjusting hash table data structure

1.  Explain how your data structure accounts for the relationship between the data points you are storing.

The main data structure used is the custom hash table that has been implemented as the “CreateHashMap”
The hash table stores package objects and is used to simulate package delivery by using the nearest neighbor algorithm to calculate the most efficient route for each truck.  It also handles storing the package data read from the package CSV file and loaded into the hash table using the loadPackageData() function.
loadPackageData(filename: object, package_hash_table:object)-> object:
Takes a filename and package hash table as input. 
Opens the file then reads the package using the csv.reader object and inserts them into the package hash table using their package ID’s as keys
Each package is associated with a unique PID as its key.
The “CreateHashMap" class has an insert method which inserts a package object into the hash table using the PID as the key. 
The “CreateHashMap” class has an “__init__” method that takes an “initial_capacity” parameter which will initialize a list of empty lists (buckets) according to the attributed capacity.  
If the key already exists in the bucket, then the value is updated, otherwise the key value pair is appended to the bucket.  It also uses chaining to handle collisions. We use the insert and update method throughout the program to insert or update a package data.
The “lookup” method of the CreateHashMap class looks up the value associated with the given key by “hashing” the key, locating the bucket, and iterating through the bucket to find the key value pair. We use the lookup method throughout the program to find specific packages by their PID.
The “hash_remove” method of the CreateHashMap class removes a key value pair from the hash table by “hashing” the key, locating the bucket, and removing the key from the bucket if found. We use the hash_remove method throughout the program to remove a specific package.


Note: Use only appropriate built-in data structures, except dictionaries. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the Internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.

E.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the following components as input and inserts the components into the hash table:
•   package ID number
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   delivery status (e.g., delivered, en route)
Included in the attached code.
F.  Develop a look-up function that takes the following components as input and returns the corresponding data elements:
•   package ID number
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time
Included in the attached code.



G. Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks.  (The delivery status should report the package as at the hub, en route, or delivered.  Delivery status must include the time.)
Provide screenshots to show the status of all packages at a time between 8:35am and 9:25am 
8:40am


2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
9:50am 












Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
12:30pm





H. Provide a screenshot or screenshots showing successful completion of the code, free from runtime errors or warnings, that includes the total mileage traveled by all trucks.




Justify the core algorithm you identified in part A and used in the solution by doing the following:
Describe at least two strengths of the algorithm used in the solution.
The core strengths of the algorithm used in the solution are:
The Nearest Neighbor algorithm is not difficult to implement. It only requires calculating distances between points and choosing the closest point that has not been visited yet. This makes it a good choice for developers who want to create a working solution quickly without going into more complex algorithms.
The Nearest Neighbor algorithm works by making optimal choices at each step, which can often lead to reasonably good solutions in practice. While it doesn't guarantee finding the global optimal solution, the algorithm performs well for many real-world problems, especially if the problem size is small or moderate, as in the case of the package delivery problem in the provided code.

Verify that the algorithm used in the solution meets all requirements in the scenario.
Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
The capacity of each truck is set to 16, as seen in the capacity variable. The uniqueness of package IDs is guaranteed by the input data and the loadPackageData() function.

The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
The speed of each truck is set to 18, as seen in the speed variable. The program assumes trucks have an unlimited amount of gas and is not required to stop.

Below are screenshots showing the package 9 address change and delivery to the correct address of 410 State St., Salt Lake City, UT 8411
 10:20

10:40
Prior to the address fix 9:00 the address isn’t changed until 10:20






There are no collisions.
The use of chaining in the CreateHasMap Class ensures that there are no collisions, as each bucket contains a list of items with the same hash value, and new items are simply appended to the end of the list. This allows for efficient lookups and removals, as the search only needs to be performed within the bucket where the item might be found.

Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
The program initializes three truck objects (truckOne, truckTwo, and truckThree) and simulates their deliveries separately.

Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
The program sets the departure times for trucks as 8:00 a.m. for truckOne, 9:05 a.m. for truckTwo, and 10:20 a.m. for truckThree. The trucks are loaded with initial packages before departure. 
The nearest neighbor algorithm effectively ensures packages are picked up and delivered efficiently.

The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
The program does not account for any time spent during delivery or loading, which meets this requirement.

There is up to one special note associated with a package.
The update_status method in the Package class checks if the current time is between 10:20 a.m. and 5:00 p.m. and if the package ID is 9. If both conditions are met, it updates the package address to the correct one.

The delivery address for package #9, Third District Juvenile Court, is wrong and is corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
The update_status method in the Package class checks if the current time is between 10:20 a.m. and 5:00 p.m. and if the package ID is 9. If both conditions are met, it updates the package address to the correct one.

The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
The distanceBetween function retrieves distances from the CSVDistanceList where distances values are equal in both directions.

The day ends when all 40 packages have been delivered.
The nearestNeighborDelivery function delivers all packages for each truck. The program continues to run until all packages have been delivered, at which the day has ended.

Identify two other named algorithms, different from the algorithm implemented in the solution, that would meet the requirements in the scenario.
Two alternative algorithms to the Nearest Neighbor algorithm that can be used in this package delivery scenario are:

Brute Force Algorithm
Genetic Algorithm (GA)

Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.

The Brute Force algorithm computes all possible permutations of the delivery routes and selects the route with the lowest total distance. Unfortunately
According to soubhikmitra98 (2021 May, 04), “this algorithm often goes above the O(n!) order of growth” (soubhikmitra98, 2021 May, 04) making it inefficient for large datasets but would be ok to use in the current WGUPS program. To implement the Brute Force algorithm, we would replace the nearestNeighborDelivery() function with a bruteForce algorithm that calculates all possible permutations of the delivery routes and selects the shortest route. 

Source: 
soubhikmitra98. A (2021, May 04). Brute Force Approach and its Pros and Cons.  https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/ 

Genetic Algorithm (GA):According to GeeksforGeeks (2023 Feb, 21) “Genetic algorithms are heuristic search algorithms inspired by the process that supports the evolution of life.  The algorithm is designed to replicate the natural selection process to carry generation, i.e. survival of the fittest of beings.” (GeeksforGeeks, 2023 Feb, 21)
Source:
GeeksforGeeks. (2023, February 21). Traveling Salesman Problem (TSP) Implementation. https://www.geeksforgeeks.org/traveling-salesman-problem-using-genetic-algorithm/?ref=rp 
The difference between the Nearest Neighbor algorithm and the Genetic Algorithm is that the Nearest Neighbor algorithm is a greedy method that gives a solution by selecting the closest neighbor at each step, while the Genetic Algorithm works with a population of solutions and evolves them through generations to find a near-optimal solution.
We could implement the Genetic Algorithm to find an optimal route for each truck.
The individuals in the population would represent different routes, 
Fitness would be determined by the total distance of the route. 
The algorithm would work by selecting the fittest individuals/routes, then performing crossover and mutation operations to generate new routes, then we could evaluate the fitness/total distance of the new population. 
The process would continue for a specified number of generations, and the best route found during the evolution process would be used as the solution.

Strengths and weaknesses of the self-adjusting data structures (e.g., the hash table):
Strengths:
Fast average-case performance for lookups, insertions, and deletions (O(1)).
Space-efficient when the number of items stored is not much greater than the number of slots in the hash table.
Can handle any data type that can be hashed.

Weaknesses:
Worst-case performance can be slow if the hash function does not distribute keys evenly or the hash table becomes too full.
Requires a good hash function to ensure uniform distribution of keys.
J.  Describe what you would do differently, other than the two algorithms identified in I3, if you did this project again.

If I would do the project over again I'd try to implement an algorithm called the “Backtracking” algorithm is a more exhaustive search algorithm that explores all possible solutions, According to md1844(2022 June, 22) it calculates the cost of every traversal and “keeps track of minimum cost and keeps updating the value of minimum cost stored value, and returns the permutation with minimum” (md1844, 2022 June, 22)

Source: md1844(2022 June, 22). Traveling Salesman Problem implementation using Backtracking. https://www.geeksforgeeks.org/travelling-salesman-problem-implementation-using-backtracking/ 

I’d also implement a nicer looking GUI that gives a visual representation of the trucks, packages, locations and delivery statuses.

The submission states that brute force and the genetic algorithm would be implemented if the project were attempted again. As these are algorithms identified in part I3, this aspect is incomplete.

K.  Justify the data structure you identified in part D by doing the following:
Verify that the data structure used in the solution meets all requirements in the scenario.

Below are screenshots showing the package 9 address change and delivery to the correct address of 410 State St., Salt Lake City, UT 8411
10:20

10:40
Prior to the address fix 9:00 the address isn’t changed until 10:20



Explain how the time needed to complete the look-up function is affected by changes in the number of packages to be delivered.
The lookup function in the CreateHashMap class uses a hash table to find a specific package based on its packageID.  The time complexity of the lookup function is O(1) in best cases and O(n) in Worst-case performance can be slow if the hash function does not distribute keys evenly or the hash table becomes too full.

Explain how the data structure space usage is affected by changes in the number of packages to be delivered.
The size of the hash table is proportional to the number of packages to be delivered.  As the number of packages increases, so does the hash table, so space usage increases linearly with the number of packages.  

Describe how changes to the number of trucks or the number of cities would affect the look-up time and the space usage of the data structure.
If the number of trucks increases, the lookup time for packages in the hash table will not be affected because the hash table is independent of the number of trucks.  The usage of space with the data structure won’t be affected by the number of trucks because it only stores package information.
If the number of cities increases then the look-up time for packages in the hash table will not be affected since it depends on the number of packages, not the cities.  


2.  Identify two other data structures that could meet the same requirements in the scenario.
	
Singly-Linked Lists:
We could use a singly-linked list as a linear data structure where each node contains a reference to the next node.  In this case, each node would keep a package instance stored along with a reference to the next package.
Sorted and Unsorted arrays:
In a sorted array packages would be stored in ascending order based on the package IDs.  
By using an unsorted array we could store the package in any order.  When inserting a new package or searching or removing or updating or deleting a package we could just iterate through the array to find the appropriate position or target package.
	
	
Describe how each data structure identified in part K2 is different from the data structure used in the solution.
Singly-Linked lists:
A singly-linked list organizes its elements linearly, where each element points to the next.  In contrast, the hash table maps keys(package IDs) to indices similar to an array.
Singly-linked lists don’t need to be resized since they grow and shrink with the addition and removal of elements.  In contrast, the hash table needs to be resized when the number of elements goes past its capacity. 
Sorted array:
Sorted arrays have a O(log n) lookup time.  This would be slower than the hash tables O(1).  Insertion and deleting in the sorted array would also be slower O(n) (worst case) as the sorted array would need to be reordered after the operation.  One positive that a sorted array has over the hash table is that it does not need to store additional data structures to handle chaining.
Unsorted Array:
Arrays would have a lookup time of O(n), where n is the number of packages.  It would be slower than the implemented hash table’s lookup time which has an average case of O(1).  
	

L.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

soubhikmitra98. A (2021 May, 04). Brute Force Approach and its Pros and Cons.  https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/ 

GeeksforGeeks. (2023, February 21). Traveling Salesman Problem (TSP) Implementation. https://www.geeksforgeeks.org/traveling-salesman-problem-using-genetic-algorithm/?ref=rp 

md1844(2022, June, 22). Traveling Salesman Problem implementation using Backtracking. https://www.geeksforgeeks.org/travelling-salesman-problem-implementation-using-backtracking/ 



