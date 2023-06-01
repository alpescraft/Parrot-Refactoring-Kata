export class Parrot {
    constructor() {
    }

    public getBaseSpeed(): number {
        return 12;
    }

}

export class EuropeanParrot extends Parrot {
    constructor() {
        super();
    }

    getSpeed() {
        return 12;
    }
}

export class AfricanParrot extends Parrot {
    constructor(public numberOfCoconuts: number) {
        super();
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
                 public voltage: number,
                 public isNailed: boolean) {
        super();
    }

    getSpeed(): number {
        return (this.isNailed) ? 0 : this.getBaseSpeedWithVoltage(this.voltage);
    }

    getBaseSpeedWithVoltage(voltage: number): number {
        return Math.min(24, voltage * this.getBaseSpeed());
    }
}
