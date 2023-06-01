export class Parrot {
    constructor(
                public numberOfCoconuts: number,
                public voltage: number,
                public isNailed: boolean) {
    }

    public getBaseSpeed(): number {
        return 12;
    }

}

export class EuropeanParrot extends Parrot {
    constructor() {
        super(0, 0, false);
    }

    getSpeed() {
        return 12;
    }
}

export class AfricanParrot extends Parrot {
    constructor( numberOfCoconuts: number) {
        super(numberOfCoconuts, 0, false);
    }

    getSpeed(): number {
        return Math.max(0, this.getBaseSpeed() - this.getLoadFactor() * this.numberOfCoconuts);
    }

    getLoadFactor(): number {
        return 9;
    }
}

export class NorwegianBlueParrot extends Parrot {
    constructor(
                 voltage: number,
                 isNailed: boolean) {
        super( 0, voltage, isNailed);
    }

    getSpeed(): number {
        return (this.isNailed) ? 0 : this.getBaseSpeedWithVoltage(this.voltage);
    }

    getBaseSpeedWithVoltage(voltage: number): number {
        return Math.min(24, voltage * this.getBaseSpeed());
    }
}
