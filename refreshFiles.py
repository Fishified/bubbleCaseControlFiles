import os
import argparse

cwd=os.getcwd()
path=r'../bubbleCaseControlFiles'

parser = argparse.ArgumentParser(description='A class instance of argparse!')
parser.add_argument("-file", help="path to refreshDict")
args = parser.parse_args()
refreshDict = args.file
print(file)

if not os.path.isdir('./constant'):
    print('No constant folder present, creating it ...')
    os.system('mkdir ./constant')

if not os.path.isdir('./system'):
    print('No system folder present, creating it ...')
    os.system('mkdir ./system')

if not os.path.isdir(path):
    os.chdir("..")
    os.system('git clone https://github.com/Fishified/bubbleCaseControlFiles.git')
    os.chdir(cwd)

with open(refreshDict, 'r') as file:
    keyDict={}
    for line in file:  
        key,value = line.strip().split(',')
        keyDict[key]=value
    print(keyDict)
    

if 'mesh' in keyDict:
    print(keyDict['mesh'].strip())
    if not os.path.isdir(keyDict['mesh'].strip()):
        print('The specified polyMesh folder %s is not found!' %keyDict['mesh'])
        print('Either remove the mesh keyword or add the correct polyMesh folder to the mesh directory.' %keyDict['mesh'])
        sys.exit("Missing polyMesh error")

    if os.path.isdir(keyDict['mesh'].strip()):
        os.system('cp -r %s ./constant/polyMesh' % keyDict['mesh'].strip())



with open(refreshDict, 'r') as file:
    for line in file:  
        key,value = line.strip().split(',')

        """0 folder"""

        if "0" in key:
            file=path+'/0/'+value.strip()
            os.system('cp -r %s ./0' % file)           
        
        """system files"""
        
        if 'controlDict' in key:
            file=path+'/system/controlDict/'+value.strip()
            os.system('cp -r %s ./system/controlDict' % file)

        if 'blockMeshDict' in key:
            file=path+'/system/blockMeshDict/'+value.strip()
            os.system('cp %s ./system/blockMeshDict' % file)

        if 'snappy' in key:
            file= path+'/system/snappyHexMeshDict/'+value.strip()
            os.system('cp %s ./system/snappyHexMeshDict' % file )

        if 'decompose' in key:
            file= path+'/system/decomposeParDict/'+value.strip()
            os.system('cp %s ./system/decomposeParDict' % file )

        if 'setFields' in key:
            file = path+'/system/setFieldsDict/'+value.strip()
            os.system('cp %s ./system/setFieldsDict' % file )
            
        if 'fvSchemes' in key:
            file = path+'/system/fvSchemes/'+value.strip()
            os.system('cp %s ./system/fvSchemes' % file )            
            
        if 'fvSolution' in key:
            file = path+'/system/fvSolution/'+value.strip()
            os.system('cp %s ./system/fvSolution' % file )
            
        if 'createPatchDict' in key:
            file = path+'/system/createPatchDict/'+value.strip()
            os.system('cp %s ./system/createPatchDict' % file)
           
        if 'setSet' in key:
            file = path+'/system/setSet/'+value.strip()
            os.system('cp %s ./system/setSet' % file)  
            
        if 'surfaceFeatureExtractDict' in key:
            file = path+'/system/surfaceFeatureExtractDict/'+value.strip()
            os.system('cp %s ./system/surfaceFeatureExtractDict' % file) 


        """constant files"""

        if 'phaseProperties' in key:
            file = path+'/constant/phaseProperties/'+value.strip()
            os.system('cp %s ./constant/phaseProperties' % file)
            
        if 'thermophysicalProperties.air' in key:
            file = path+'/constant/thermophysicalProperties/'+value.strip()
            os.system('cp %s ./constant/thermophysicalProperties.air' % file)

        if 'thermophysicalProperties.water' in key:
            file = path+'/constant/thermophysicalProperties/'+value.strip()
            os.system('cp %s ./constant/thermophysicalProperties.water' % file)

        if 'turbulence.air' in key:
            file = path+'/constant/turbulenceProperties/'+value.strip()
            os.system('cp %s ./constant/turbulenceProperties.air' % file)
        
        if 'turbulence.water' in key:
            file = path+'/constant/turbulenceProperties/'+value.strip()
            os.system('cp %s ./constant/turbulenceProperties.water' % file)
           
        if 'g' in key:
            file = path+'/constant/g/'+value.strip()
            os.system('cp %s ./constant/g' % file)
            
            
        """slurm file"""  

        if 'slurm' in key:
            file = path+'/slurm/'+value.strip()
            os.system('cp %s ./%s' % (file,value.strip()))
