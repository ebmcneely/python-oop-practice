"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initiates a new serial number generator with a defult start at 0"""

        self.start = start
        self.next = start

    def generate(self):
        """Generates the next serial number in line"""

        self.next = self.next + 1
        return self.next - 1

    def reset(self):
        """Resets the serial number to the orignal value"""

        self.next = self.start
