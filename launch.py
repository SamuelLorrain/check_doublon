import subprocess
import re

a = open('result.txt', 'r')
tab = []
for i in a.readlines():
    i = i.strip('\n')
    i = i.split(',')
    for j,_ in enumerate(i):
        i[j] = i[j].strip()
    tab.append(i)


with open("to_remove", "w") as f:
    for i in tab:
        i.insert(0, 'gnome-mpv')
        subprocess.run(i)
        input_responce = input("is it a doublon ? [Yes,No] ")
        if input_responce in ["Yes","yes","y","YES", "Y"]:
            for j in i[2:]:
                f.write("rm '{}'\n".format(j))
            f.write("#======================\n")
