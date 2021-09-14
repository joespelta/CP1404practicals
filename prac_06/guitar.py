YEAR = 2021


class Guitar:
    """Represents a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        return str(f"{self.name} ({self.year}): ${self.cost}")

    def get_age(self):
        age = YEAR - self.year
        return age

    def is_vintage(self):
        return self.age >= 50
