import os
source_roots = "/home/ubuntu/ShuaiWang/sw-face-net/facenet"
paths = ":"
#source_roots = "/Users/gm-vv-ang/Documents/UBCSE/courses/2018 FALL/CSE 676/Projects/facenet/"
ignores = ["data", ".idea", ".git", ".project", ".pydevproject", ".DS_Store", ".pylintrc"]
def find_all_source_roots(path):
    items = os.listdir(path)

    global paths
    for i in items:
        if i in ignores:
            continue
        absulute_path = os.path.join(path, i)
        if not os.path.isfile(absulute_path):
            paths += absulute_path + ":"
            find_all_source_roots(absulute_path)

find_all_source_roots(source_roots)
print(paths[:-1])


