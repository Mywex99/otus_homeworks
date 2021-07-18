from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=100, fuel_consumption=10, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low Fuel Level!")
        return self.started

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance < distance:
            raise NotEnoughFuel("Not Enough Fuel!")
        self.fuel -= distance * self.fuel_consumption
        return self.fuel
