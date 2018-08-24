# ---|---------------|---
# ---|- Python OOP  -|---
# ---|---------------|---
# ---|   Multiple    |---
# ---|  Inheritence  |---
# ---|---------------|---


class Vehicle:
    wheel = int()
    engine = bool()

    def __init__(self, wheel, engine):
        self.wheel = wheel
        self.engine = engine


class Brand():

    def set(self, name, founded, country, market_value):
        self.name = name
        self.founded = founded
        self.country = country
        self.market_value = market_value

    def brand_info(self):
        print(
            "\nBrand info: \n\tName: {name}\n\tFounded: {start}\n\tCountry: {country}\n\tValue: {value}"
            .format(
                name=self.name, start=self.founded, country=self.country, value=self.market_value
            )
        )


# Muliple Inheritence Class

class Car(Vehicle, Brand):

    def __init__(self, top_speed, fuel_capacity, wheel=4, engine=True):
        super().__init__(wheel, engine)

        self.top_speed = top_speed
        self.fuel_capacity = fuel_capacity

    def info(self):
        print("Car info: ")
        print("\tMax Speed: {speed}\n\tFuel Capacity: {fuel}"
              .format(speed=self.top_speed, fuel=self.fuel_capacity))


# Create Car object
lancer = Car(top_speed=200, fuel_capacity=59)

lancer.set(name="Mitsubishi", founded="‎1973",
           country="Japan", market_value='11.7 Billion')

lancer.brand_info()
lancer.info()
