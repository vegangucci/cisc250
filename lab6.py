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
        
    
 

    
    






        
