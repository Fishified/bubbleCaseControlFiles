#!/bin/bash

failfunction()
{
    if [ "$1" != 0 ];
    then echo "$2 One of the commands has failed!!";
        if [ "$3" == "fatal" ];
        then echo "The failure was fatal!";
         mail -s "$4 failed" duguay.jason@gmail.com <<< "on job $5 ";
         fi
    fi
}

rm -r processor*
failfunction "$?" rm pass freeSlip

decomosePar
failfunction "$?" decomposePar fatal freeSlip

mpirun -np 8 twoPhaseEulerFoam -parallel
failfunction "$?" twoPhaseEulerFoam fatal freeSlip