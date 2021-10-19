from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Version of Taxi that has a fanciness."""

    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness, price_per_km=1.23):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km = price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                                               self.current_fare_distance,
                                                                               self.price_per_km, self.flag_fall)

    def get_fare(self):
        new_fare = self.flag_fall + super().get_fare()
        return new_fare

    def drive(self, distance):
        return super().drive(distance)

    def start_fare(self):
        super().start_fare()
