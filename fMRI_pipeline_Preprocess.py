def fMRIpreprocess():
    # a script which identifies anatomicial/functional files and applies preprocessing steps
    # - Skull stripping using BET
    # - Motion correction using MCFLIRT

    # Run on Windows 11 in Windows subsystem Linux (WSL) in Conda Env w/ nipype and fslpy installed.

    import glob, os
    from os.path import exists, abspath
    from nipype.interfaces.fsl import BET, MCFLIRT

    # Preprocessing for Stroop Data
    dataDir = '/mnt/c/fMRIclass/ds000164-download/'   # Main directory with data
    subjectTag = 'sub-'     # All directories with participant data start with this
    tmpVolTag = "splitVol_"

    # Collect all the files in the data directory which contain the tag.
    dirList = os.listdir(dataDir)                                   # Pull all folders
    dirList = [word for word in dirList if subjectTag in word]      # Filter for subject folder

    # Generate 'Nodes' for tasks to be performed - this case, BET and MCLFIRT
    # BET
    btr = BET()
    btr.inputs.frac = 0.7
    btr.cmdline

    # MCFLIRT
    mcflt = fsl.MCFLIRT()
    mcflt.inputs.in_file = 'functional.nii'
    mcflt.inputs.cost = 'mutualinfo'
    mcflt.inputs.out_file = 'moco.nii'
    mcflt.cmdline

    # Cycle through subject folders
    for subj_i in range(0, len(dirList)):

        # Define Paths you'll want to have for functions down the line.      
        subj_dir = dirList[subj_i]
        print('Processing ' + subj_dir + ' Files...')
        workingDir = dataDir + subj_dir
        
        # Paths for BET skull stripping
        anatPath = workingDir + '/anat/' + subj_dir + "_T1w_reoriented.nii.gz"
        anatUpdatePath = workingDir + '/anat/' + subj_dir + "_T1w_reoriented_BET.nii.gz"

        # Paths for Functional scan motion correct
        funcDir = workingDir + '/func/'
        funcPath = funcDir + subj_dir + "_task-stroop_bold_1.5TR.nii.gz"
        funcUpdatePath = funcDir + subj_dir + "_task-stroop_bold_1.5TR_MoCo.nii.gz"

        # Check if the Anatomical file has already been fixed
        if exists(anatUpdatePath):
            print('Skipping Anatomical file, already processed')

        else:
            print("Reorienting Anatomical for " + subj_dir)
            btr.inputs.in_file = anatPath
            btr.inputs.out_file = anatUpdatePath
            BETout = btr.run()

        # Check to see if Functional data has already been fixed.
        if exists(funcUpdatePath):
            print('Skipping Functional file, already processed')

        else:
            print('Motion correcting Functional File...')
            mcflt.inputs.in_file = funcPath
            mcflt.inputs.out_file = funcUpdatePath
            MCFLIRTout = mcflt.run()

            print('Complete!')

# Defined as such to allow for print statements to make it to the terminal.
if __name__ == '__main__':
    fMRIpreprocess()