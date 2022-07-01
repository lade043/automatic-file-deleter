import sys
from os import listdir
from os.path import isfile, join

directory = input("Which directory should be scanned.\n")

try:
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
except FileNotFoundError:
    print("This directory doesn't exist.")
    sys.exit(-1)

file_type_delete = input("Files from which type should be deleted? [.xyz]\n")

relevant_files = []
for i in files:
    if i[-len(file_type_delete):] == file_type_delete:
        relevant_files.append(i)

files_to_rm = []
for file in relevant_files:
    name = file[:-len(file_type_delete)]
    fitting_file_exists = False
    for _file in files:
        if _file != file and (name == _file[:len(name)] and _file[len(name)] == "."):
            fitting_file_exists = True
    if not fitting_file_exists:
        files_to_rm.append(file)

files_to_rm.sort()

directory_str_has_slash = directory[-1] == "/"
if not directory_str_has_slash:
    directory += "/"
rm_string = "rm"
for i in files_to_rm:
    rm_string += " '" + directory + i + "'"

print("You can run the following command to delete all the files:")
print(rm_string)
with open("rm.sh", 'w') as f:
    f.write(rm_string)
print("This will delete the following files: " + str(files_to_rm))
