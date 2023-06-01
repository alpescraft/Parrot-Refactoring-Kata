package parrot

class EuropeanParrot(type: ParrotTypeEnum, numberOfCoconuts: Int, voltage: Double, isNailed: Boolean) :
        Parrot(type, numberOfCoconuts, voltage, isNailed){

            override val speed: Double
                get() = baseSpeed
}