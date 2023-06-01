package parrot

import kotlin.math.max
import kotlin.math.min

open class Parrot(
    private val type: ParrotTypeEnum,
    val numberOfCoconuts: Int,
    val voltage: Double,
    val isNailed: Boolean
) {

    open val speed: Double
        get() = when (type) {
            ParrotTypeEnum.EUROPEAN -> baseSpeed
            ParrotTypeEnum.AFRICAN -> max(0.0, baseSpeed - loadFactor * numberOfCoconuts)
            ParrotTypeEnum.NORWEGIAN_BLUE -> if (isNailed) 0.0 else getBaseSpeed(voltage)
        }

    val loadFactor: Double
        get() = 9.0

    val baseSpeed: Double
        get() = 12.0

    fun getBaseSpeed(voltage: Double): Double = min(24.0, voltage * baseSpeed)
}
