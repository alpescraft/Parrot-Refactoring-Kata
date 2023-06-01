package parrot

import kotlin.math.max

class AfricanParrot(numberOfCoconuts: Int, voltage: Double, isNailed: Boolean) :
        Parrot(numberOfCoconuts, voltage, isNailed){

            override val speed: Double
                get() = max(0.0, baseSpeed - loadFactor * numberOfCoconuts)
}