from ride import RideSharing
from users import Rider, Driver

#company
chata_company = RideSharing("Chata_company")

#Rider
rahim = Rider("Rahim", "rahim@", 45435453, "Uttara", 500)
chata_company.add_rider(rahim)

#Driver
karim = Driver("karim", "karim@", 464521, "Gulsan")
chata_company.add_driver(karim)

#Check ride status
rahim.request_ride(chata_company, "khilgaon", 'car')
karim.reach_destination(rahim.current_ride)
rahim.show_current_ride()


# print(chata_company)