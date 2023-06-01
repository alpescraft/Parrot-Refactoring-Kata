package parrot

class NorwegianBlueParrot(numberOfCoconuts: Int, voltage: Double, isNailed: Boolean) :
        Parrot(numberOfCoconuts, voltage, isNailed){

            override val speed: Double
                get() = if (isNailed) 0.0 else getBaseSpeed(voltage)
}