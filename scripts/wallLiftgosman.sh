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

echo "Loading openfoam modules"
module load openfoam/7
failfunction "$?" load fatal wallLiftgosman

rm -r processor*
failfunction "$?" rm pass wallLiftgosman

decomposePar
failfunction "$?" decomposePar fatal wallLiftgosman

sbatch slurmwallLiftgosman.sh
failfunction "$?" sbatch fatal wallLiftgosman

#mpirun -np 80 twoPhaseEulerFoam -parallel
#failfunction "$?" twoPhaseEulerFoam fatal gosman