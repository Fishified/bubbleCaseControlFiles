import os
import sys
import argparse

cwd=os.getcwd()
# path=r'../bubbleCaseControlFiles'

parser = argparse.ArgumentParser(description='A class instance of argparse!')
parser.add_argument("-n", help="Case's name. Assumes the case folder will reside at the same directory level as caseControlFiles repo.")
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

with open(refreshDict, 'r') as file:
    for line in file:  
        key,value = line.strip().split(',')

        """0 folder"""

        if "0" in key:
            file='./0/'+value.strip()
            os.system('cp -r %s %s/0' % (file,casePath))           
        
        """system files"""
        
        if 'controlDict' in key:
            file='./system/controlDict/'+value.strip()
            os.system('cp -r %s %s/system/controlDict' % (file,casePath))

        if 'blockMeshDict' in key:
            file='./system/blockMeshDict/'+value.strip()
            os.system('cp %s %s/system/blockMeshDict' % (file,casePath))

        if 'snappy' in key:
            file= './system/snappyHexMeshDict/'+value.strip()
            os.system('cp %s %s/system/snappyHexMeshDict' % (file,casePath) )

        if 'decompose' in key:
            file= './system/decomposeParDict/'+value.strip()
            os.system('cp %s %s/system/decomposeParDict' % (file,casePath) )

        if 'setFields' in key:
            file = './system/setFieldsDict/'+value.strip()
            os.system('cp %s %s/system/setFieldsDict' % (file,casePath) )
            
        if 'fvSchemes' in key:
            file = './system/fvSchemes/'+value.strip()
            os.system('cp %s %s/system/fvSchemes' % (file,casePath) )            
            
        if 'fvSolution' in key:
            file = './system/fvSolution/'+value.strip()
            os.system('cp %s %s/system/fvSolution' % (file,casePath) )
            
        if 'createPatchDict' in key:
            file = './system/createPatchDict/'+value.strip()
            os.system('cp %s %s/system/createPatchDict' % (file,casePath))
           
        if 'setSet' in key:
            file = './system/setSet/'+value.strip()
            os.system('cp %s %s/system/setSet' % (file,casePath))  
            
        if 'surfaceFeatureExtractDict' in key:
            file = './system/surfaceFeatureExtractDict/'+value.strip()
            os.system('cp %s %s/system/surfaceFeatureExtractDict' % (file,casePath)) 


        """constant files"""

        if 'phaseProperties' in key:
            file = './constant/phaseProperties/'+value.strip()
            os.system('cp %s %s/constant/phaseProperties' % (file,casePath))
            
        if 'thermophysicalProperties.air' in key:
            file = './constant/thermophysicalProperties/'+value.strip()
            os.system('cp %s %s/constant/thermophysicalProperties.air' % (file,casePath))

        if 'thermophysicalProperties.water' in key:
            file = './constant/thermophysicalProperties/'+value.strip()
            os.system('cp %s %s/constant/thermophysicalProperties.water' % (file,casePath))

        if 'turbulence.air' in key:
            file = './constant/turbulenceProperties/'+value.strip()
            os.system('cp %s %s/constant/turbulenceProperties.air' % (file,casePath))
        
        if 'turbulence.water' in key:
            file = './constant/turbulenceProperties/'+value.strip()
            os.system('cp %s %s/constant/turbulenceProperties.water' % (file,casePath))
           
        if 'g' in key:
            file = './constant/g/'+value.strip()
            os.system('cp %s %s/constant/g' % (file,casePath))


        """script file"""

        if 'script' in key:
            file = './scripts/'+value.strip()
            os.system('dos2unix %s' %file)
            os.system('cp %s %s/%s' % (file,casePath,value.strip()))               
            
        """slurm file"""  

        if 'slurm' in key:
            file = './slurm/'+value.strip()
            os.system('cp %s %s/%s' % (file,casePath,value.strip()))
