from enum import Enum  # Enum is introduced in Python 3.4.


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self, type_of_parrot):
        self._type = type_of_parrot

    def speed(self):
        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0


class EuropeanParrot(Parrot):

    def __init__(self):
        super().__init__(ParrotType.EUROPEAN)

    def speed(self):
        return super()._base_speed()


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts
        super().__init__(ParrotType.AFRICAN)

    def speed(self):
        return max(0, super()._base_speed() - super()._load_factor() * self._number_of_coconuts)


class NorwegianParrot(Parrot):

    def __init__(self, voltage, nailed):
        self._nailed = nailed
        self._voltage = voltage
        super().__init__(ParrotType.NORWEGIAN_BLUE)

    def speed(self):
        if self._nailed:
            return 0
        else:
            return super()._compute_base_speed_for_voltage(self._voltage)
