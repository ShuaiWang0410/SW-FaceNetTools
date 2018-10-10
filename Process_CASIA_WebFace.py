import os

cur_people = 0
total_people = 0
select_people = 1000
folders_list = []
source = '~/CASIA-WebFace-Align-1000People'
# dist = '/Volumes/新加卷/CASIA-WebFace-Refine'

def count_folder(path):
    global total_people, folders_list
    folders_list = os.listdir(path)
    total_people = len(folders_list)
    print("There are " + str(total_people) + " people folders")

def count_images(path):

    global folders_list
    k = 0
    for i in folders_list:
        if select_people == k:
            break
        sourceDir = os.path.join(path, i)
        files = os.listdir(sourceDir)
        if len(files) < 40:
            print(i + " < 40")
        k += 1
    print("Folders above have less than 40 images")

def copy_folders_to_dist(source, dist):

    global cur_people, select_people
    print("===============================================")
    print("Start copying " + str(select_people) + " people folders")

    for i in folders_list:
        sourceDir = os.path.join(source, i)
        distDir = os.path.join(dist, i)
        if not os.path.exists(distDir):
            os.makedirs(distDir)
            files = os.listdir(sourceDir)
            for j in files:
                sourceFile = os.path.join(sourceDir, j)
                distFile = os.path.join(distDir, j)
                open(distFile, "wb+").write(open(sourceFile, "rb+").read())

        cur_people += 1
        if cur_people == select_people:
            break
    print("Finish copying " + str(cur_people) + " people folders")
    print("There are " + str(len(os.listdir(dist))) + " people folders copied indeed")



#count_folder(source)
count_folder(source)
count_images(source)
#copy_folders_to_dist(source, dist)

