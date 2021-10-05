from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised Version of Car with reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only if reliability is enough."""
        if self.reliability > random.randint(0, 100):
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven
        