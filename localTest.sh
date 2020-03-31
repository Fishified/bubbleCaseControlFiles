#!/bin/bash

failfunction()
{
    if [ "$1" != 0 ];
    
    then echo "The $2 command has failed!";
        echo "The $2 command has failed" >> testResult;
        if [ "$3" == "fatal" ];
            then echo "And it was fatal ... too bad try again.";
            echo "The $2 command fatally failed" >> testResult;
            mail -s "$2 failed" duguay.jason@gmail.com <<< "on job $4 ";
            exit -1
        fi

        if [ "$3" == "pass" ]
            then echo "But it was not fatal.";
            echo "The $2 command failed but was not fatal." >> testResult;
        fi 
    fi
}

echo "Running the local tests on the case"
now=$(date)
echo "Test started at $now:" >> testResult;
rm -r processor*
failfunction "$?" rm pass test

decomposePar
failfunction "$?" decomposePar fatal test

mpirun -np $1 twoPhaseEulerFoam -parallel
failfunction"$?" twoPhaseEulerFoam fatal test