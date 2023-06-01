package parrot;

public class NorvegianBlueParrot extends Parrot {

    public NorvegianBlueParrot(int numberOfCoconuts, double voltage, boolean isNailed) {
        super(null, numberOfCoconuts, voltage, isNailed);
    }

    @Override
    public double getSpeed() {
        return (isNailed) ? 0 : getBaseSpeed(voltage);
    }
}
