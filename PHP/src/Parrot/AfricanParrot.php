<?php

namespace Parrot\Parrot;

class AfricanParrot implements ParrotInterface
{

    public function getSpeed(): float
    {
        // TODO: Implement getSpeed() method.
    }

    private function getLoadFactor(): float
    {
        return 9.0;
    }
}
