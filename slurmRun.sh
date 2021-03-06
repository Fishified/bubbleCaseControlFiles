#!/bin/bash
#SBATCH --account=def-lacey
#SBATCH --nodes=24
#SBATCH --ntasks-per-node=8
#SBATCH --mem=0
#SBATCH --time=0-28:00
#SBATCH --output=solverOutput.out
mpirun -np 192 twoPhaseEulerFoam -parallel