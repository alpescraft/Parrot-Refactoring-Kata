import unittest
from parrot import Parrot, AfricanParrot, EuropeanParrot, NorwegianParrot

class TestParrotCase(unittest.TestCase):
    def test_speedOfEuropeanParrot(self):
        parrot = EuropeanParrot(0, 0, False)
        assert parrot.speed() == 12.0


    def test_speedOfAfricanParrot_With_One_Coconut(self):
        parrot = AfricanParrot(1, 0, False)
        assert parrot.speed() == 3.0


    def test_speedOfAfricanParrot_With_Two_Coconuts(self):
        parrot = AfricanParrot(2, 0, False)
        assert parrot.speed() == 0.0


    def test_speedOfAfricanParrot_With_No_Coconuts(self):
        parrot = AfricanParrot(0, 0, False)
        assert parrot.speed() == 12.0


    def test_speedNorwegianBlueParrot_nailed(self):
        parrot = NorwegianParrot(0, 1.5, True)
        assert parrot.speed() == 0.0


    def test_speedNorwegianBlueParrot_not_nailed(self):
        parrot = NorwegianParrot(0, 1.5, False)
        assert parrot.speed() == 18.0


    def test_speedNorwegianBlueParrot_not_nailed_high_voltage(self):
        parrot = NorwegianParrot(0, 4, False)
        assert parrot.speed() == 24.0

    def test_parrot_raise(self):
        parrot = Parrot(0, 4, False)
        with self.assertRaises(ValueError) as ve:
            parrot.speed()
