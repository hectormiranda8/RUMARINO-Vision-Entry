# TODO: function explainers

import os

def files2list(path, file_extension):
    files=[]
    for file in os.listdir(path):
        if file.endswith(file_extension):
            files.append(file)
    return files

def list2file(file, arr):
    with open(file, 'w') as oFile:
        for item in arr:
            file.write(f"{item}\n")