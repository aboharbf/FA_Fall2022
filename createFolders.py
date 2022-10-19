# Create a hierarchy of folders for each subject, 

from os import mkdir, listdir

path2Dir = 'C:\\fMRIclass\ds000164-download\Analysis\\'     # Where the 3 folders are, each gets a full hierarchy put within.
path2Tree = 'C:\\fMRIclass\ds000164-download\\rawData\\'    # Where the subject list comes from

folder2Make = ['Group\\', 'LevelOne\\', 'Preproc\\']        # 3 folder names

# Identify subjFolders to make
dir2MakeList = listdir(path2Tree)

for coreFolder in folder2Make:
    makeDirPath = path2Dir + coreFolder
    print(makeDirPath)
    for subjFold in dir2MakeList:
        mkdir(makeDirPath + subjFold)