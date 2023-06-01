from enum import Enum  # Enum is introduced in Python 3.4.


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def african_speed(self):
            return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def norwegian_speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)

    def speed(self):
        print("Computing speed...")
        if self._type == ParrotType.AFRICAN:
            return self.african_speed()
        if self._type == ParrotType.NORWEGIAN_BLUE:
            return self.norwegian_speed()

        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0

class EuropeanParrot(Parrot):
    def speed(self):
        return self._base_speed()
