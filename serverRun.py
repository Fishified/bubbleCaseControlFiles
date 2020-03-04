import os
import argparse
import subprocess
import shlex

cwd=os.getcwd()


parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Name of text file containing any number of terminal commands as long as they are on separate lines. The name of the name of the text file must correspond with the case file's name. The case file must also be present at the same directory level as the caseControlFile repo.")
args = parser.parse_args()

scriptName = args.n
scriptPath = cwd+'/scripts/%s' %scriptName

caseDirectory=os.path.dirname(cwd)+'/%s' %scriptName
os.chdir(caseDirectory)
launchCommand='bash %s.sh' %scriptName
os.system(launchCommand)