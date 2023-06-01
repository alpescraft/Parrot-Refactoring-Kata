<?php

namespace Parrot\Parrot;

class EuropeanParrot extends BaseSpeed implements ParrotInterface
{
    public function getSpeed(): float
    {
        return $this->getBaseSpeed();
    }
}
