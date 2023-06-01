package parrot;

public abstract class GenericParrot {

    protected ParrotTypeEnum type;
    protected int numberOfCoconuts;
    protected double voltage;
    protected boolean isNailed;

    public GenericParrot(ParrotTypeEnum type, int numberOfCoconuts, double voltage, boolean isNailed) {
        this.type = type;
        this.numberOfCoconuts = numberOfCoconuts;
        this.voltage = voltage;
        this.isNailed = isNailed;
    }


    public abstract double getSpeed();

    private double getBaseSpeed(double voltage) {
        return Math.min(24.0, voltage * getBaseSpeed());
    }

    protected double getLoadFactor() {
        return 9.0;
    }

    protected double getBaseSpeed() {
        return 12.0;
    }

}
