#!/bin/bash

failfunction()
{
    if [[ "$1" != 0 && "$2" == fatal ]];
    then echo "One of the commands has failed!!"
         mail -s "$3 failed" duguay.jason@gmail.com <<< "on job $4 "
    fi
}

rm -r processor*
failfunction "$?" rm pass freeSlip

decomosePar
failfunction "$?" decomposePar fatal freeSlip

mpirun -np 8 twoPhaseEulerFoam -parallel
failfunction "$?" twoPhaseEulerFoam fatal freeSlip