class Circle:

    def __init__(self, radius):
        self._radius = radius
        self._pi = 3.14159  # Stored internally

    @property
    def pi(self):
        """Read-only property for PI."""
        return self._pi

    @property
    def radius(self):
        return self._radius


c = Circle(5)

# Reading the value works fine
print(c.pi)  # Output: 3.14159
print(c.radius)  # Output: 5

# Trying to change it crashes the program!
c._radius = 3.143221  # AttributeError: can't set attribute 'pi'
print(c.radius)  # Output: 3.14 (but this is not recommended, as it bypasses the property)