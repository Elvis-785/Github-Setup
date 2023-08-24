class Car:
    def __init__(self, name, type, manufacturer, top_speed, horsepower, torque) -> None:
        self.name=name
        self.type=type
        self.manufacturer=manufacturer
        self.top_speed=top_speed
        self.horsepower=horsepower
        self.torque=torque

    def __str__(self) -> str:
        return f"The car is called {self.name} manufactured by {self.manufacturer}"
    

car_inst=Car("Vanguard","SUV","Toyota","180km/h","150hp","200Nm/P")

print(car_inst)