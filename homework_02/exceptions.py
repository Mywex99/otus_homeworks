class LowFuelError(BaseException):
    print("Low Fuel!")


class NotEnoughFuel(BaseException):
    print("Not Enough Fuel!")


class CargoOverload(BaseException):
    print("Overload!")
