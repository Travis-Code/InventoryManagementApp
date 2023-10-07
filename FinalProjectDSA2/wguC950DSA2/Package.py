# Package class, representing a delivery package.
# The class has attributes for the package ID, address, city, state, zipcode, deadline time, weight, status, departure time, and delivery time.
# The class also has methods for updating the status of a package.

import datetime


# (Time complexity of O(1))
class Package:
    # The constructor initializes the attributes of the package object.
    def __init__(self, ID: int, address: str, city: str, state: str, zipcode: str, Deadline_time: str, weight: str,
                 status: str):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    # The __str__ method returns a string representation of the package object.
    # (Time complexity of O(1)).
    def __str__(self) -> str:
        return f"{self.ID:<4} {self.address:<22} {self.city:<16} {self.state:<6} {self.zipcode:<10} {self.Deadline_time:<12} {self.weight:<14} {str(self.delivery_time):<21} {str(self.departure_time):<14} {self.status:<15}"

    # update_status updates the status of the package based on its delivery time, departure time, and the current time.
    # it also takes into account the address change of package 9.
    # (Time complexity of O(1)).
    # def update_status(self, convert_timedelta: datetime.timedelta) -> None:
    #     if datetime.time(10, 20) <= (datetime.datetime.min + convert_timedelta).time() <= datetime.time(12, 0) and self.ID == 9:
    #         self.address = "410 S State St., Salt Lake City, UT 84111"
    #     if self.delivery_time < convert_timedelta:
    #         self.status = "Delivered"
    #     elif self.departure_time > convert_timedelta:
    #         self.status = "En Route"
    #     else:
    #         self.status = "At the Hub"
    # def update_status(self, convert_timedelta: datetime.timedelta) -> None:
    #     if datetime.time(10, 20) <= (datetime.datetime.min + convert_timedelta).time() <= datetime.time(12, 0) and self.ID == 9:
    #         self.address = "410 S State St., Salt Lake City, UT 84111"
    #     if self.delivery_time < convert_timedelta:
    #         self.status = "Delivered"
    #     elif self.departure_time > convert_timedelta:
    #         self.status = "En Route"
    #     else:
    #         self.status = "At the Hub"

        # truckOne: Truck = createTruck(1, listForTruckOne, datetime.timedelta(hours=8))
        # truckTwo: Truck = createTruck(2, listForTruckTwo, datetime.timedelta(hours=9, minutes=5))
        # truckThree: Truck = createTruck(3, listForTruckThree, datetime.timedelta(hours=10, minutes=20))

    # def update_status(self, current_time: datetime.timedelta) -> None:
    #     if datetime.time(10, 20) <= (datetime.datetime.min + current_time).time() <= datetime.time(12,
    #                                                                                                0) and self.ID == 9:
    #         self.address = "410 S State St., Salt Lake City, UT 84111"
    #     if self.delivery_time is None and current_time > self.Deadline_time:
    #         self.delivery_time = current_time
    #         self.status = "Delivered"
    #     elif self.departure_time is None and self.status != "Delivered" and self.packages_loaded and current_time >= self.depart_time:
    #         self.departure_time = current_time
    #         self.status = "En Route"
    #     elif self.status != "Delivered" and self.status != "En Route":
    #         self.status = "At the Hub"
    # def update_status(self, convert_timedelta: datetime.timedelta) -> None:
    #     if datetime.time(10, 20) <= (datetime.datetime.min + convert_timedelta).time() <= datetime.time(12, 0) and self.ID == 9:
    #         self.address = "410 S State St., Salt Lake City, UT 84111"
    #     if self.delivery_time is not None and self.delivery_time < convert_timedelta:
    #         self.status = "Delivered"
    #     elif self.departure_time is not None and self.departure_time > convert_timedelta:
    #         self.status = "En Route"
    #     else:
    #         self.status = "At the Hub"
    def update_status(self, convert_timedelta: datetime.timedelta) -> None:
        if datetime.time(10, 20) <= (datetime.datetime.min + convert_timedelta).time() <= datetime.time(17, 0) and self.ID == 9:
            self.address = "410 S State St., Salt Lake City, UT 84111"
        if self.delivery_time is not None and self.delivery_time <= convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time is not None and self.departure_time <= convert_timedelta:
            self.status = "En Route"
        else:
            self.status = "At the Hub"
