from enum import Enum  # Enum is introduced in Python 3.4.


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        if self._type == ParrotType.NORWEGIAN_BLUE:
            if self._nailed:
                return 0
            else:
                return self._compute_base_speed_for_voltage(self._voltage)

        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0


class EuropeanParrot(Parrot):

    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)

    def speed(self):
        return super()._base_speed()


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)

    def speed(self):
        return max(0, super()._base_speed() - super()._load_factor() * self._number_of_coconuts)


class NorwegianParrot(Parrot):

    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)
