import os

file_path = 'E:\\practice\\Data Science\\누구나 자료구조와 알고리즘'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

print ("OK")