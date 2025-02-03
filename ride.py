from datetime import datetime
from vehicle import Car,Bike

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rids = []
        
    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
        
    def __repr__(self):
        return f"Company Name: {self.company_name}\nTotal Riders: {len(self.riders)} Total Drivers: {len(self.drivers)}"


class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fate(vehicle.vehicle_type)
        self.vehicle = vehicle
        
    def set_driver(self, driver):
        self.driver = driver
        
    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
    def calculate_fate(self, vehicle_type):
        distance = 10
        fare_per_km = {
            'car': 50,
            'bike': 20,
            'cng': 35
        }
        return distance*fare_per_km[vehicle_type]
        
    
    
class RideRequesst:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, available_drivers):
        self.available_drivers = available_drivers
        
    def find_driver(self, ride_request, vehicl_type):
        if len(self.available_drivers) > 0:
            print("Looking for driver...")
            driver = self.available_drivers[0]
            
            if vehicl_type == 'car':
                vehicle = Car("Afsfs77", 50)
            elif vehicl_type == 'bike':
                vehicle = Bike("Afsfs77", 50)
                
            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
            
            driver.accept_ride(ride)
            return ride
            