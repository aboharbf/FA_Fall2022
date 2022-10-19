# FA_Fall2022
A Repo containing scripts created during 'Python for fMRI Analysis', taught by Dr. Marlen Gonzalez at Cornell in Fall of 2022 (HD4630 / HD6635)

## Data set used
Stroop Task dataset from OpenNeuro - https://openneuro.org/datasets/ds000164/versions/00001
Downloaded using aws command line interface.

## Analysis Pipeline Software
Pipeline developed on Windows 11 system using Ubuntu 18 on Windows Subsystem Linux (Wsl).
Software run in Conda environment w/ Nipype, fslpy (fMRI_Conda.yml environment file present can recreate)

## Hierarchy of files
Core file ('ds000164-download') is resorted to contain 'rawData' (containing sub folders), Admin (containing files previously in the root directory), 'Analysis' (containing a folder each for Preprocessing, LevelOne Analysis, Group Analysis, and Scripts).

## Steps of the Sequence
- Initial preprocessing ('preprocess.py') -> Applies fsl reorient2std and a split/merge sequence to correct TR to 1.5.
- fMRI preprocessing ('fMRI_pipeline_Preprocessing.py') -> Applies ...