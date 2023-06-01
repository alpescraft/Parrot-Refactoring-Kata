export enum ParrotTypes {
}

export class Parrot {
    constructor(private parrotType: ParrotTypes,
                public numberOfCoconuts: number,
                public voltage: number,
                public isNailed: boolean) {
    }

    public getBaseSpeed(): number {
        return 12;
    }

    public getLoadFactor(): number {
        return 9;
    }

}

export class EuropeanParrot extends Parrot {
    constructor( numberOfCoconuts: number,
                 voltage: number,
                 isNailed: boolean) {
        super(0, numberOfCoconuts, voltage, isNailed);
    }

    getSpeed() {
        return 12;
    }
}

export class AfricanParrot extends Parrot {
    constructor( numberOfCoconuts: number,
                 voltage: number,
                 isNailed: boolean) {
        super(0, numberOfCoconuts, voltage, isNailed);
    }

    getSpeed(): number {
        return Math.max(0, this.getBaseSpeed() - this.getLoadFactor() * this.numberOfCoconuts);
    }
}

export class NorwegianBlueParrot extends Parrot {
    constructor( numberOfCoconuts: number,
                 voltage: number,
                 isNailed: boolean) {
        super(0, numberOfCoconuts, voltage, isNailed);
    }

    getSpeed(): number {
        return (this.isNailed) ? 0 : this.getBaseSpeedWithVoltage(this.voltage);
    }

    getBaseSpeedWithVoltage(voltage: number): number {
        return Math.min(24, voltage * this.getBaseSpeed());
    }
}
