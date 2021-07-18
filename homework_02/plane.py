from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        _cargo = self.cargo + load
        if self.max_cargo < _cargo:
            raise CargoOverload("Plane is overloaded!")
        self.cargo += load
        return self.cargo

    def remove_all_cargo(self):
        _cargo = self.cargo
        self.cargo = 0
        return _cargo
