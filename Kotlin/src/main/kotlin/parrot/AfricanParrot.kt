package parrot

import kotlin.math.max

class AfricanParrot(type: ParrotTypeEnum, numberOfCoconuts: Int, voltage: Double, isNailed: Boolean) :
        Parrot(type, numberOfCoconuts, voltage, isNailed){

            override val speed: Double
                get() = max(0.0, baseSpeed - loadFactor * numberOfCoconuts)
}