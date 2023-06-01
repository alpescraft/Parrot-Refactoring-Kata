package parrot;

public class NorvegianBlueParrot extends Parrot {

    public NorvegianBlueParrot(ParrotTypeEnum type, int numberOfCoconuts, double voltage, boolean isNailed) {
        super(type, numberOfCoconuts, voltage, isNailed);
    }

    public NorvegianBlueParrot(int numberOfCoconuts, double voltage, boolean isNailed) {
        super(null, numberOfCoconuts, voltage, isNailed);
    }

    @Override
    public double getSpeed() {
        return (isNailed) ? 0 : getBaseSpeed(voltage);
    }
}
