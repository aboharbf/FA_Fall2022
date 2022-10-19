def reOrientAndTRCorrect():
    # A simple script which targets all the appropriately laabeled files in a dataDir and applies
    # the fsl command 'reorient2std' (Anatomical) and corrects TR by using FSL Split and Merge (Anatomical)

    # Run on Windows 11 in Windows subsystem Linux (WSL) in Conda Env w/ nipype and fslpy installed.

    import glob, os
    from os.path import exists, abspath
    from nipype.interfaces.fsl import Reorient2Std, Split, Merge

    # Preprocessing for Stroop Data
    dataDir = '/mnt/c/fMRIclass/ds000164-download/'   # Main directory with data
    subjectTag = 'sub-'     # All directories with participant data start with this
    tmpVolTag = "splitVol_"

    # Collect all the files in the data directory which contain the tag.
    dirList = os.listdir(dataDir)                                   # Pull all folders
    dirList = [word for word in dirList if subjectTag in word]      # Filter for subject folder

    # Generate 'Nodes' for tasks to be performed - Reorientation, Splitting, Merging.
    # Reorient Object
    reorient = Reorient2Std()

    # Split Object
    fslsplit = Split()
    fslsplit.inputs.dimension = 't'

    # Merge Object
    fslmerge = Merge()
    fslmerge.inputs.dimension = 't'
    fslmerge.inputs.output_type = 'NIFTI_GZ'
    fslmerge.inputs.tr = 1.5

    # Cycle through subject folders
    for subj_i in range(0, len(dirList)):

        # Define Paths you'll want to have for functions down the line.      
        subj_dir = dirList[subj_i]
        print('Processing ' + subj_dir + ' Files...')
        workingDir = dataDir + subj_dir
        anatPath =  workingDir + '/anat/' + subj_dir + "_T1w.nii.gz"
        anatUpdatePath = workingDir + '/anat/' + subj_dir + "_T1w_reoriented.nii.gz"
        funcPath = workingDir + '/func/' + subj_dir + "_task-stroop_bold.nii.gz"
        funcDir = workingDir + '/func/'
        funcTempFile = workingDir + '/func/' + tmpVolTag
        funcUpdatePath = workingDir + '/func/' + subj_dir + "_task-stroop_bold_1.5TR.nii.gz"


        # Check if the Anatomical file has already been fixed
        if exists(anatUpdatePath):
            print('Skipping Anatomical file, already processed')

        else:
            print("Reorienting Anatomical for " + subj_dir)
            reorient.inputs.in_file = anatPath
            reorient.inputs.out_file = anatUpdatePath
            res = reorient.run()

        # Check to see if Functional data has already been fixed.
        if exists(funcUpdatePath):
            print('Skipping Functional file, already processed')

        else:
            print('Correcting TR for Anatomical File...')

            # split the file
            print('Splitting file...')
            fslsplit.inputs.out_base_name = funcTempFile
            fslsplit.inputs.in_file = funcPath
            splitObj = fslsplit.run()

            # Merge the file with the new TR
            print('Merging file with new TR...')
            allFiles = os.listdir(funcDir)                                      # Pull all the files in the tempDir
            tmpFileList = [word for word in allFiles if tmpVolTag in word]      # Filter for subject folder
            tmpFileList = [funcDir + s for s in tmpFileList]                    # Add the full path to the filenames

            fslmerge.inputs.in_files = tmpFileList
            fslmerge.inputs.merged_file = funcUpdatePath
            mergeObj = fslmerge.run()

            # Clean up, delete old files.
            for tmpFile in tmpFileList:
                os.remove(tmpFile)

            print('Complete!')

# Defined as such to allow for print statements to make it to the terminal.
if __name__ == '__main__':
    reOrientAndTRCorrect()