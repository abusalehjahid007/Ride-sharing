from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_location = current_location
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
        self.current_location = currentLocation
        
    def request_ride(self, ride_sharing, destination):
        pass
    
    def show_current_ride(self):
        print(f"Current Ride: {self. current_ride}")
        
class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0
        
    def display_profile(self):
        print(f"Driver Name: {self.name}, Driver Email: {self.email}")
        
    def accept_ride(self, ride):
        pass
        
        
    