import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}
    
my_car = Car("Toyota", "Camry", 2023, "camry_image.jpg")
print(my_car.display_info()) 

new_car = Car("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

# Load existing data
try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

# Append new car
cars_data.append(new_car.to_dict())

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)