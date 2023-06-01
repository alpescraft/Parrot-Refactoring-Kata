package parrot;

public class AfricanParrot extends Parrot{
    public AfricanParrot(ParrotTypeEnum type, int numberOfCoconuts, double voltage, boolean isNailed) {
        super(type, numberOfCoconuts, voltage, isNailed);
    }

    public AfricanParrot(int numberOfCoconuts, double voltage, boolean isNailed) {
        super(null, numberOfCoconuts, voltage, isNailed);
    }

    @Override
    public double getSpeed() {
        return Math.max(0, getBaseSpeed() - getLoadFactor() * numberOfCoconuts);
    }
}
