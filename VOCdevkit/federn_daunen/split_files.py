import os
import random

file_path = "E:\\code\\PythonProject\\faster_rcnn\\data_source\\federn_daunen\\Annotations"

if not os.path.exists(file_path):
    print("this dictioinary not exist")
    exit(-1)

val_rate = 0.5

files_name = sorted([file.split(".")[0] for file in os.listdir(file_path)])
files_num = len(files_name)
val_index = random.sample(range(0, files_num), k=int(val_rate * files_num))
train_files = []
val_files = []

for index, file_name in enumerate(files_name):
    if index in val_index:
        val_files.append(file_name)
    else:
        train_files.append(file_name)

try:
    train_f = open("train.txt", "x")
    eval_f = open("val.txt", "x")
    train_f.write("\n".join(train_files))
    eval_f.write("\n".join(val_files))
except FileExistsError as e:
    print(e)
    exit(1)
    
