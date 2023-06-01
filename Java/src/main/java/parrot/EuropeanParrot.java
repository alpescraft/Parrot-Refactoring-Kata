package parrot;

public class EuropeanParrot extends GenericParrot {
    public EuropeanParrot(int numberOfCoconuts, double voltage, boolean isNailed) {
        super(ParrotTypeEnum.EUROPEAN, numberOfCoconuts, voltage, isNailed);
    }

    @Override
    public double getSpeed() {
        return 12;
    }
}
