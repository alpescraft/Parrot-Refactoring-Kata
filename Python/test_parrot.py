from parrot import Parrot, ParrotType, AfricanParrot, EuropeanParrot, NorwegianParrot


def test_speedOfEuropeanParrot():
    parrot = EuropeanParrot(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_speedOfAfricanParrot_With_One_Coconut():
    parrot = AfricanParrot(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.speed() == 3.0


def test_speedOfAfricanParrot_With_Two_Coconuts():
    parrot = AfricanParrot(ParrotType.AFRICAN, 2, 0, False)
    assert parrot.speed() == 0.0


def test_speedOfAfricanParrot_With_No_Coconuts():
    parrot = AfricanParrot(ParrotType.AFRICAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_speedNorwegianBlueParrot_nailed():
    parrot = NorwegianParrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speedNorwegianBlueParrot_not_nailed():
    parrot = NorwegianParrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speedNorwegianBlueParrot_not_nailed_high_voltage():
    parrot = NorwegianParrot(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.speed() == 24.0
