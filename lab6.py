#task 1
class Vehicle:

    '''A class represeting the vehicle'''

 #task1a   
    def __init__(self,make,model,year,max_fuel=8.0):
        self.make = make
        self.model = model
        self.model = year
        self.max_fuel = max_fuel
        

        self.current_fuel = 0.0 
        self.is_almost_empty = True

#task1b 
    def fuel_level(self, gallons):
        if gallons < 0:
            print(f"Warning! Cannot set a negative fuel level for {self.make} {self.mode}." f"Fuel level unchanged.")
            return
        
        if gallons > self.max_fuel:
            print(f"  [Warning] {gallons} gallons exceeds max capacity ({self.max_fuel}) "
                  f"for {self.make} {self.model}. Fuel level unchanged.")
            return
        
         # Set the fuel level and update the warning flag
        self.current_fuel = float(gallons)
        self.empty_warning_check()
 
    # Task 1b 2
    def details(self):
        """Returns a formatted string with the vehicle's make, model, and year."""
        return f"{self.year} {self.make} {self.model}"
 
    # Task 1b 3
    def fuel_left(self):
        """Return the percentage of fuel remaining as a float rounded to 1 decimal place.
        """
        percentage = (self.current_fuel / self.max_fuel) * 100
        return round(percentage, 1)
 
    # Task 1b 4
    def empty_warning_check(self):
        """Checks that if fuel left is less than 10% and set is_almost_empty accordingly."""
        if self.fuel_left() < 10.0:
            self.is_almost_empty = True
        else:
            self.is_almost_empty = False
        

 
#Task 2a
vehicles = []
 
#Task 2b
vehicle1 = Vehicle("Toyota", "Camry",    2020, max_fuel=13.2)
vehicle2 = Vehicle("Honda",  "Civic",    2019, max_fuel=12.4)
vehicle3 = Vehicle("Ford",   "Mustang",  2022, max_fuel=16.0)
vehicle4 = Vehicle("BMW",    "3 Series", 2021, max_fuel=15.6)
 
# Vehicle list 
vehicles.append(vehicle1)
vehicles.append(vehicle2)
vehicles.append(vehicle3)
vehicles.append(vehicle4)
 
#Task 2c
print("=" * 55)
print("Setting fuel levels for each vehicle:")
print("=" * 55)
 
vehicles[0].fuel_level(5.3)   # Vehicle 1 = 5.3 gallons
vehicles[1].fuel_level(2.2)   # Vehicle 2 = 2.2 gallons
vehicles[2].fuel_level(10.1)  # Vehicle 3 = 10.1 gallons
vehicles[3].fuel_level(0.5)   # Vehicle 4 = 0.5 gallons
 
#Task 2d

print()
print("Attempting to set Vehicle 2 fuel level to -4.4 (invalid - negative value):")
vehicles[1].fuel_level(-4.4)
 
#Task 2e
print()
print("Attempting to set Vehicle 4 fuel level to 100 (invalid - exceeds max capacity):")
vehicles[3].fuel_level(100)
 
#Task 2f
print()
print("=" * 55)
print("Vehicle Summary:")
print("=" * 55)
 
for i, vehicle in enumerate(vehicles, start=1):
    print(f"\nVehicle {i}: {vehicle.details()}")
    print(f"  Current Fuel : {vehicle.current_fuel} gallons")
    print(f"  Max Fuel     : {vehicle.max_fuel} gallons")
    print(f"  Fuel Left    : {vehicle.fuel_left()}%")
    print(f"  Almost Empty : {vehicle.is_almost_empty}")
 
print()
print("=" * 55)
print("End of Lab 6 - Part 1")
print("=" * 55)
 

    
    






        
