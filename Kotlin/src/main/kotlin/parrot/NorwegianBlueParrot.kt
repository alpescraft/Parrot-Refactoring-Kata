package parrot

class NorwegianBlueParrot(type: ParrotTypeEnum, numberOfCoconuts: Int, voltage: Double, isNailed: Boolean) :
        Parrot(type, numberOfCoconuts, voltage, isNailed){

            override val speed: Double
                get() = if (isNailed) 0.0 else getBaseSpeed(voltage)
}