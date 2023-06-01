package parrot;

public class NorvergianParrot extends GenericParrot {
    public NorvergianParrot(double voltage, boolean isNailed) {
        super(ParrotTypeEnum.NORWEGIAN_BLUE, 0, voltage, isNailed);
    }

    @Override
    public double getSpeed() {
        return (isNailed) ? 0 : getBaseSpeed(voltage);
    }
}
