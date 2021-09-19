class ProgrammingLanguage:
    """Represents a programming language object."""

    def __init__(self, field, typing, reflection, year=0):
        self.field = field
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}")

