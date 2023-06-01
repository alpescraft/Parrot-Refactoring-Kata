import {AfricanParrot, EuropeanParrot, NorwegianBlueParrot, Parrot, ParrotTypes} from '../src/parrot'

describe('Parrot', () => {

    it('gets speed of European Parrot', () => {
        const parrot = new EuropeanParrot( 0, 0, false);
        expect(parrot.getSpeed()).toBe(12);
    });

    it('gets speed of African Parrot with one coconut', () => {
        const parrot = new AfricanParrot( 1, 0, false);
        expect(parrot.getSpeed()).toBe(3);
    });

    it('gets speed of African Parrot with two coconuts', () => {
        const parrot = new AfricanParrot( 2, 0, false);
        expect(parrot.getSpeed()).toBe(0);
    });

    it('gets speed of African Parrot with no coconuts', () => {
        const parrot = new AfricanParrot( 0, 0, false);
        expect(parrot.getSpeed()).toBe(12);
    });

    it('gets speed of Norwegian Blue Parrot nailed', () => {
        const parrot = new NorwegianBlueParrot(ParrotTypes.NORWEGIAN_BLUE, 0, 1.5, true);
        expect(parrot.getSpeed()).toBe(0);
    });

    it('gets speed of Norwegian Blue Parrot not nailed', () => {
        const parrot = new NorwegianBlueParrot(ParrotTypes.NORWEGIAN_BLUE, 0, 1.5, false);
        expect(parrot.getSpeed()).toBe(18);
    });

    it('gets speed of Norwegian Blue Parrot not nailed high voltage', () => {
        const parrot = new NorwegianBlueParrot(ParrotTypes.NORWEGIAN_BLUE, 0, 4, false);
        expect(parrot.getSpeed()).toBe(24);
    });

});
