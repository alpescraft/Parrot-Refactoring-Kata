from enum import Enum  # Enum is introduced in Python 3.4.


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed = False):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        raise ValueError("should be unreachable")

    def _base_speed(self):
        return 12.0

class EuropeanParrot(Parrot):
    def __init__(self):
        super().__init__(ParrotType.EUROPEAN, 0, 0)

    def speed(self):
        return super()._base_speed()

class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts):
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, 0, False)

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def _load_factor(self):
        return 9.0

class NorwegianBlueParrot(Parrot):
    def __init__(self, voltage, nailed = False):
        self._nailed = nailed
        super().__init__(ParrotType.NORWEGIAN_BLUE, 0, voltage, nailed)

    def speed(self):
        if self._nailed:
                return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])
