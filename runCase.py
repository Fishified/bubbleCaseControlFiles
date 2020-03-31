import os
import argparse
import subprocess
import shlex

cwd=os.getcwd()

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Name of text file containing any number of terminal commands as long as they are on separate lines. The name of the name of the text file must correspond with the case file's name. The case file must also be present at the same directory level as the caseControlFile repo.")

parser.add_argument("-np", help="Specify number of processors to run case with.")

parser.add_argument("-test", help="Specifies whether to run the test script, yes/no.")

parser.add_argument("-runOnly", help="Run only the solver and nothing else, yes/no.")

args = parser.parse_args()

scriptName = args.n
scriptPath = cwd+'/scripts/%s' %scriptName

if args.test and args.test == 'yes':

    if args.runOnly == 'yes':
        caseDirectory=os.path.dirname(cwd)+'/%s' %scriptName
        os.chdir(caseDirectory)
        os.system('mpirun -np %s twoPhaseEulerFoam -parallel' % args.np) 
    else:
        caseDirectory=os.path.dirname(cwd)+'/%s' %scriptName
        os.chdir(caseDirectory)
        launchCommand='bash ./localTest.sh %s' % args.np
        os.system(launchCommand)
else:
    print('Running commands in order of appearance ')
    caseDirectory=os.path.dirname(cwd)+'/%s' %scriptName
    os.chdir(caseDirectory)
    # os.system('cp ./system/decomposeParDict.orig ./system/decomposeParDict')
    launchCommand='bash serverRun.sh %s' % scriptName
    os.system(launchCommand)