class Engine():
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f'Engine with {self.horsepower} HP has started.'

class Driver():
    def __init__(self, name, license, wins, need = "Speed"):
        self.name = name
        self.license = license
        self.wins = wins
        self.need = need
    
    def drive(self):
        return f'{self.name} is driving.'

class Car():
    def __init__(self, make, model, horsepower):
        self.driver = None
        self.engine = Engine(horsepower)
        self.make = make
        self.model = model
    
    def assign_driver(self, d):
        self.driver = d

    def start_car(self):
        if self.driver:
            return f'{self.driver.name} is starting the car. {self.engine.start()}'
        else:
            return f'No driver is assigned to {self.make} {self.model}.'

#CREATE Wheel Class HERE

#CREATE Team Class HERE

#CREATE Race Class HERE


if __name__ == "main":
    pass
    #remove pass and use this area to test your code