import os
source_roots = "/home/ubuntu/ShuaiWang/sw-face-net/facenet"
ignores = ["data"]
def find_all_source_roots(path):
    items = os.listdir(path)

    global source_roots
    for i in items:
        absulute_path = os.path.join(path, i)
        if not os.path.isfile(absulute_path):
            source_roots += absulute_path + ":"
            find_all_source_roots(absulute_path)
    print(source_roots[:-1])
find_all_source_roots(source_roots)


