#!/bin/bash

failfunction()
{
    if [ "$1" != 0 ]
    then echo "One of the commands has failed!!"
         mail -s "$2 failed" duguay.jason@gmail.com <<< "on job $3"
    fi
}

rm -r processor*
failfunction "$?" rm freeSlip

decomosePar
failfunction "$?" decomposePar freeSlip

mpirun -np 8 twoPhaseEulerFoam -parallel
failfunction "$?" twoPhaseEulerFoam freeSlip