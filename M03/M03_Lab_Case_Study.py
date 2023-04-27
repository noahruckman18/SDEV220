"""
Programmer: Noah Ruckman
Title: M03_Lab_Case_Study.py
Summary: Two classes Vehicle and Automobile. Vehicle is a super class. It takes the specs of a car and prints it out in an easy-to-read format. 
Version: 1.0
Last Revision: 4/9/2023
"""

class Vehicle:
    def __init__(self,type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self,type, year, make, model, doors, roof):
            super().__init__(type)
            self.year = year
            self.make = make
            self.model = model
            self.doors = doors
            self.roof = roof
            
vehicle_type = input("What type of vehicle do you own (car, truck, plane, boat, or a broomstick)? ").lower()
if vehicle_type != "car":
    print("We don't reconize that option. Please pick car.")
else:
    vehicle_year = int(input("What is the year of your car: "))
    vehicle_make = input("What is the make of your car: ").capitalize()
    vehicle_model = input("What is the model of your car: ").capitalize()
    vehicle_doors = int(input("How many doors does you car have (2 or 4): "))
    vehicle_roof = input("What type of roof does your car have (Solid or Sun roof): ").lower()

    vehicle = Automobile(vehicle_type,vehicle_year,vehicle_make,vehicle_model,vehicle_doors,vehicle_roof)

    print(f"Vehicle Type: {vehicle.type}")
    print(f"Year: {vehicle.year}")
    print(f"Make: {vehicle.make}")
    print(f"Model: {vehicle.model}")
    print(f"Number of doors: {vehicle.doors}")
    print(f"Type of roof: {vehicle.roof}")