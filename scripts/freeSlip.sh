#!/bin/bash

failfunction()
{
    if [ "$1" != 0 ];
    then echo "$2 One of the commands has failed!!";
        if [ "$3" == "fatal" ];
        then echo "The failure was fatal!";
         mail -s "$2 failed" duguay.jason@gmail.com <<< "on job $4 ";
         exit
         fi
    fi
}

module load openfoam/5.0
failfunction "$?" rm fatal freeSlip

rm -r processor*
failfunction "$?" rm pass freeSlip

decomposePar
failfunction "$?" decomposePar fatal freeSlip

#mpirun -np 80 twoPhaseEulerFoam -parallel
#failfunction "$?" twoPhaseEulerFoam fatal freeSlip