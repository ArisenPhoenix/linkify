#!/usr/bin/python3
# /mnt/Internal_SSD/Ubuntu/Scripts/from_src_to_dest_soft_symbolic_links.py
import os
import sys
from helpers import *
import time
args = sys.argv

root_dir = args[1]
ending_dir=args[3]

if not os.path.isdir(root_dir):
    find_problematic_point(root_dir)

if not os.path.isdir(ending_dir):
    find_problematic_point(ending_dir)


list_of_desired_dirs=args[2]
print("LIST OF DESIRED DIRS 1: ", list_of_desired_dirs)

if list_of_desired_dirs == "<|>" or list_of_desired_dirs == "*":
    list_of_desired_dirs = os.listdir(root_dir)
else:
    list_of_desired_dirs = handle_potential_list(list_of_desired_dirs)

print("LIST OF DESIRED DIRS 2: ", list_of_desired_dirs)
list_of_desired_dirs.sort()

list_of_exceptions = []
try:
    list_of_exceptions = args[4]
except IndexError:
    pass


try:
    minutes = args[5]
    if "." in minutes:
        try:
            minutes = float(minutes)
        except ValueError:
            minutes = 0
    else:
        try:
            minutes = int(minutes)
        except ValueError:
            minutes = 0
except IndexError:
    minutes = 0




list_of_exceptions = handle_potential_list(list_of_exceptions)



answer = True

seconds = minutes * 60
if minutes > 0:
    print("Will First Be Waiting")
    print(f"In Minutes: {minutes}")
    print(f"In Seconds: {seconds}")
    print("As Per Requested")
    print("No Validation Will Be Requested")
    print("Thank You")

else:
    answer, list_of_desired_dirs = validate(list_of_desired_dirs)
    
time.sleep(seconds)


if answer:
    print("Your Links Are Being Created...")
    all_root_dirs = os.listdir(root_dir)
    for random_dir in all_root_dirs:
        desired_src = os.path.join(root_dir, random_dir) if random_dir in list_of_desired_dirs and random_dir not in list_of_exceptions else False
        if desired_src:
            if os.path.isdir(desired_src):
                desired_dest = os.path.join(ending_dir, random_dir)
                
                if os.path.isdir(desired_dest):
                    print(f"CANNOT MOVE {desired_src} to {desired_dest} ")
                    print(f"Folder {random_dir} Already Exists")
                    continue
                else:
                    print(f"MOVING {desired_src} to {desired_dest} ")
                    os.symlink(desired_src, desired_dest)
            else:
                print(f"Dir {desired_src} Does Not Exist")
    sys.exit(0)
else:
    print("Please Check Your Settings And Make Sure You Add Exceptions If Necessary.")
    sys.exit(0)



