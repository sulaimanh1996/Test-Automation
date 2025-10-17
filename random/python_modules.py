class Vehicle:
    def __init__(self, brand, doors=4, wheels=4):  
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_greeting(self):  
        print("Hi, I'm your new car. My name is " + self.brand +
              " and I have " + str(self.doors) + " doors, and " +
              str(self.wheels) + " wheels!")

vehicle1 = Vehicle("Volvo", 5, 5)  
vehicle1.car_greeting()
