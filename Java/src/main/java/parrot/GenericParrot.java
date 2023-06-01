package parrot;

public abstract class GenericParrot {

    public static final double BASE_SPEED = 12.0;
    protected int numberOfCoconuts;
    protected double voltage;
    protected boolean isNailed;

    public GenericParrot(int numberOfCoconuts, double voltage, boolean isNailed) {
        this.numberOfCoconuts = numberOfCoconuts;
        this.voltage = voltage;
        this.isNailed = isNailed;
    }


    public double getSpeed() {return getBaseSpeed();};

    protected double getBaseSpeed(double voltage) {
        return Math.min(24.0, voltage * getBaseSpeed());
    }

    protected double getLoadFactor() {
        return 9.0;
    }

    protected double getBaseSpeed() {
        return BASE_SPEED;
    }

}
