class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return (self.make, self. model, self.year)
        
    

Leonard = Car('Toyota', 'Corolla', 2007)
print(Leonard.display_info())