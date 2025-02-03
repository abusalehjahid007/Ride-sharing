from abc import ABC, abstractmethod
from ride import RideRequesst, RideMatching, RideSharing

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
    
class Rider(User):
    def __init__(self, name, email, nid, curent_location, initial_amount):
        super().__init__(name, email, nid)
        self.curent_location = curent_location
        self.wallet = initial_amount
        self.current_ride = None
        
    def display_profile(self):
        print(f"Rider Name: {self.name}, Rider Email: {self.email}")
        
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Invalid amount..!")
            
    def current_location(self, currentLocation):
        self.currentLocation = currentLocation
        
    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequesst(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("Yeee!! we got a ride")
    
    def show_current_ride(self):
        print("Ride Details..!")
        print(f"Rider Name: {self.name}")
        print(f"Driver Name: {self.current_ride.driver.name}")
        print(f"Selected Vehicle: {self.current_ride.vehicle.vehicle_type}")
        print(f"Start Location: {self.curent_location}")
        print(f"Destination: {self.current_ride.end_location}")
        print(f"Total Cost: {self.current_ride.estimated_fare}")
        
class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0
        
    def display_profile(self):
        print(f"Driver Name: {self.name}, Driver Email: {self.email}")
        
    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)
        
    def reach_destination(self, ride):
        ride.end_ride()
        
        
    