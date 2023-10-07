# Truck class, which represents a delivery truck.
# it has attributes for the truck ID, capacity, speed, packages, mileage, address, timePlace, and depart_time.

# (Time complexity of O(1)) for initialization and O(1) for the __str__ method.
class Truck:
    # The constructor initializes the attributes of the truck object.
    def __init__(self, ID, capacity, speed, packages, mileage, address, depart_time):
        self.ID = ID
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.timePlace = depart_time
        self.depart_time = depart_time

    # The __str__ method returns a string representation of the truck object.
    # (Time complexity of O(1)).
    def __str__(self):
        truck_info = [
            self.ID, self.capacity, self.speed, self.packages,
            self.mileage, self.address, self.timePlace
        ]
        return ', '.join(map(str, truck_info))


