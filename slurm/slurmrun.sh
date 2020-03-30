#!/bin/bash
#SBATCH --account=def-lacey
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40
#SBATCH --mem=0
#SBATCH --time=0-24:00
#SBATCH --output=freeSlipBlended.out
mpirun -np 80  twoPhaseEulerFoam -parallel
