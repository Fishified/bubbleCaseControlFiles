import os
import sys
import argparse

cwd=os.getcwd()
# path=r'../bubbleCaseControlFiles'

parser = argparse.ArgumentParser(description='A class instance of argparse!')
parser.add_argument("-n", help="Case's name. Assumes the case folder will reside at the same directory level as caseControlFiles repo.")

parser.add_argument("-test", help="yes/no whether you want the local testScripts to overwrite the server specific files (e.g. a decompose dict with only 8 cores for local testing compared to a decomposeDict with 80 cores for use on the server).")

args = parser.parse_args()
case = args.n

refreshDict= './refreshDict/refreshDict.%s' %case

casePath='../%s' % case

if not os.path.isdir(casePath):
    print('Case folder for %s not present, creating an empty folder named case at  ...' %casePath)
    os.system('mkdir %s' % casePath)

if not os.path.isdir('%s/constant' %casePath):
    print('No constant folder present, creating it ...')
    os.system('mkdir %s/constant' %casePath)

if not os.path.isdir('%s/system' %casePath):
    print('No system folder present, creating it ...')
    os.system('mkdir %s/system' %casePath)

# if not os.path.isdir('%s/localTest' %casePath):
#     print('No localTest folder present, creating it ...')
#     os.system('mkdir %s/localTest' %casePath)


with open(refreshDict, 'r') as file:
    keyDict={}
    for line in file:  
        key,value = line.strip().split(',')
        keyDict[key]=value

if 'mesh' in keyDict:
    print(keyDict['mesh'].strip())
    if not os.path.isdir(keyDict['mesh'].strip()):
        print('The specified polyMesh folder is not found!')
        print('Either remove the mesh keyword or add the correct polyMesh folder to the mesh directory.')
        sys.exit("Missing polyMesh error")

    if os.path.isdir(keyDict['mesh'].strip()):
        os.system('cp -r %s %s/constant/polyMesh' % (keyDict['mesh'].strip(),casePath))

def addFileTrue(filename):
    print("Successfully added %s" % filename)

with open(refreshDict, 'r') as file:
    for line in file:  
        key,value = line.strip().split(',')

        """0 folder"""

        if "0" in key:
            file='./0/'+value.strip()
            os.system('cp -r %s %s/0' % (file,casePath))  
            addFileTrue(value.strip())       
        
        """system files"""
        
        if 'controlDict' in key:
            file='./system/controlDict/'+value.strip()
            os.system('cp -r %s %s/system/controlDict' % (file,casePath))
            addFileTrue(value.strip())

        if 'blockMeshDict' in key:
            file='./system/blockMeshDict/'+value.strip()
            os.system('cp %s %s/system/blockMeshDict' % (file,casePath))
            addFileTrue(value.strip())

        if 'snappy' in key:
            file= './system/snappyHexMeshDict/'+value.strip()
            os.system('cp %s %s/system/snappyHexMeshDict' % (file,casePath) )
            addFileTrue(value.strip())

        if 'decompose' in key:
            file= './system/decomposeParDict/'+value.strip()
            os.system('cp %s %s/system/decomposeParDict.orig' % (file,casePath) )
            addFileTrue(value.strip())

        if 'setFields' in key:
            file = './system/setFieldsDict/'+value.strip()
            os.system('cp %s %s/system/setFieldsDict' % (file,casePath) )
            addFileTrue(value.strip())

        if 'fvSchemes' in key:
            file = './system/fvSchemes/'+value.strip()
            os.system('cp %s %s/system/fvSchemes' % (file,casePath) ) 
            addFileTrue(value.strip())           
            
        if 'fvSolution' in key:
            file = './system/fvSolution/'+value.strip()
            os.system('cp %s %s/system/fvSolution' % (file,casePath) )
            addFileTrue(value.strip())

        if 'createPatchDict' in key:
            file = './system/createPatchDict/'+value.strip()
            os.system('cp %s %s/system/createPatchDict' % (file,casePath))
            addFileTrue(value.strip())
            addFileTrue(value.strip())

        if 'setSet' in key:
            file = './system/setSet/'+value.strip()
            os.system('cp %s %s/system/setSet' % (file,casePath))  
            addFileTrue(value.strip())

        if 'surfaceFeatureExtractDict' in key:
            file = './system/surfaceFeatureExtractDict/'+value.strip()
            os.system('cp %s %s/system/surfaceFeatureExtractDict' % (file,casePath)) 
            addFileTrue(value.strip())


        """constant files"""

        if 'phaseProperties' in key:
            file = './constant/phaseProperties/'+value.strip()
            os.system('cp %s %s/constant/phaseProperties' % (file,casePath))
            addFileTrue(value.strip())
            
        if 'thermophysicalProperties.air' in key:
            file = './constant/thermophysicalProperties/'+value.strip()
            os.system('cp %s %s/constant/thermophysicalProperties.air' % (file,casePath))
            addFileTrue(value.strip())

        if 'thermophysicalProperties.water' in key:
            file = './constant/thermophysicalProperties/'+value.strip()
            os.system('cp %s %s/constant/thermophysicalProperties.water' % (file,casePath))
            addFileTrue(value.strip())

        if 'turbulence.air' in key:
            file = './constant/turbulenceProperties/'+value.strip()
            os.system('cp %s %s/constant/turbulenceProperties.air' % (file,casePath))
            addFileTrue(value.strip())
        
        if 'turbulence.water' in key:
            file = './constant/turbulenceProperties/'+value.strip()
            os.system('cp %s %s/constant/turbulenceProperties.water' % (file,casePath))
            addFileTrue(value.strip())
           
        if 'g' in key:
            file = './constant/g/'+value.strip()
            os.system('cp %s %s/constant/g' % (file,casePath))
            addFileTrue(value.strip())


        """script file"""

        if 'script' in key:
            file = './scripts/'+value.strip()
            os.system('dos2unix %s' %file)
            os.system('cp %s %s/%s' % (file,casePath,value.strip()))  
            addFileTrue(value.strip())             
        
        if 'localTest' in key:
            testFolder = './localTest'
            os.system('dos2unix %s/localTest.sh' % testFolder)
            os.system('cp -r %s %s' % (testFolder,casePath))  
            addFileTrue(value.strip())           
            
        """slurm file"""  
        
        if 'slurm' in key:
            file = './slurm/'+value.strip()
            os.system('cp %s %s/%s' % (file,casePath,value.strip()))
            addFileTrue(value.strip())

if args.test and args.test == 'yes':
    print("Test specified. Files in case with the same name as those in the test folder will be overwritten.")

    testDecompose=file = './localTest/decomposeParDict'
    os.system('cp -r %s %s/system/decomposeParDict' % (testDecompose,casePath))

    testFolder=file = './localTest'
    os.system('cp -r %s %s' % (testFolder,casePath))

else:
    print("Creating a server version of the case.")