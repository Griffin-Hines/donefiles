import os
directory = "./"
file_list = os.listdir(directory)
for filename in file_list:
        donefile = filename + ".done"
        open(donefile, 'a').close()
