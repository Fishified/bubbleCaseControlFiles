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
module load nixpkgs/16.09
module load gcc/7.3.0 
module load openmpi/3.1.2
module load openfoam/7
failfunction "$?" load fatal contCl125

rm -r processor*
failfunction "$?" rm pass contCl125

decomposePar
failfunction "$?" decomposePar fatal contCl125

sbatch slurmgowallLift.sh
failfunction "$?" sbatch fatal contCl125

