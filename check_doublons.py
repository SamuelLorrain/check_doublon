#!/usr/bin/python3

import hashlib
import os
import sys
from pathlib import Path
import config

def checkpercents(x,y):
    """
    print a percentage
    using ansi escape code
    """
    sys.stdout.write("\u001b[2K")
    sys.stdout.flush()
    sys.stdout.write("\u001b[1000D"+"{:.3f}".format((x/y)*100)+"%")
    sys.stdout.flush()

def md5(fName):
    """
    md5 function, return hash representation
    of the file fName used in the dict
    """
    hash_md5 = hashlib.md5()
    with(open(fName, "rb")) as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def pushdict(md5sum, path):
    """
    add hash to the dict only if.
    the hash doesnt exists in the dict
    """
    if not md5hash.get(md5sum):
        md5hash[md5sum] = []
    md5hash[md5sum].append(path)

if __name__ == '__main__':
    #put every files (how is not a dir) in a tab
    pathToFiles = config.url
    a = Path(pathToFiles).glob('**/*')
    tabFiles = [i.as_posix() for i in a if not i.is_dir()]

    toCalcul = len(tabFiles)
    md5hash = dict()

    print("{} files to check".format(toCalcul))

    for j,i in enumerate(tabFiles[0:toCalcul]):
        checkpercents(j,toCalcul)
        md5File = md5(i)
        pushdict(md5File, i)

    nbrOfDoublons =  len([i for i,j in md5hash.items() if len(j) > 1])
    print("\n{} doublon(s) found".format(nbrOfDoublons))

    #writing result to a file in csv format
    with(open("result.txt",'w')) as f:
        for i,j in md5hash.items():
            if len(j) > 1:
                for k,l in enumerate(j):
                    if k != len(j)-1:
                        f.write("{}, ".format(l))
                    else:
                        f.write("{}".format(l))
                f.write("\n")

    print("Done ! Go check result.txt")
