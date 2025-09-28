import os
import random
import shutil

directory_path = 'train'  # Current directory, or specify a path like 'my_folder'
all_entries = os.listdir(directory_path)
files = [entry for entry in all_entries if os.path.isfile(os.path.join(directory_path, entry))]
# random.shuffle(files)

# for i in range(10480):
#     shutil.move("wavs/{}".format(files[i]), "wavs/train/{}".format(files[i]))

with open("train.txt", "a") as f:
    for file in files:
        if file[0] == 'L':
            f.write(file + ", 0" + "\n")
        else:
            f.write(file + ", 1" + "\n")