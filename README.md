# FA_Fall2022
A Repo containing scripts created during 'Python for fMRI Analysis', taught by Dr. Marlen Gonzalez at Cornell in Fall of 2022 (HD4630 / HD6635)

## Data set used
Stroop Task dataset from OpenNeuro - https://openneuro.org/datasets/ds000164/versions/00001
Downloaded using aws command line interface. Recommended getting AWS CLI - https://aws.amazon.com/cli/, and running

'''
  aws s3 sync --no-sign-request s3://openneuro.org/ds000164 ds000164-download/
'''

## Analysis Pipeline Software
Pipeline developed on Windows 11 system using Ubuntu 18 on Windows Subsystem Linux (Wsl).
Software run in Conda environment w/ Nipype, fslpy (fMRI_Conda.yml environment file present can recreate)
- Install Anaconda (Anaconda3-2022.10-Linux-x86_64.sh used in WSL here)

'''
  conda env create -f fMRI_Conda.yml
'''

Activate the environment and you should be ready to go. Running VS Code in this environment is simple ('code .')

## Hierarchy of files
Core file ('ds000164-download') is resorted to contain 'rawData' (containing sub folders), Admin (containing files previously in the root directory), 'Analysis' (containing a folder each for Preprocessing, LevelOne Analysis, Group Analysis, and Scripts).

## Steps of the Sequence
- Initial preprocessing ('preprocess.py') -> Applies fsl reorient2std and a split/merge sequence to correct TR to 1.5.
- fMRI preprocessing ('fMRI_pipeline_Preprocessing.py') -> Applies ...
