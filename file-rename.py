import os

file_path = 'E:\\practice\\Data Science\\파이썬 기반의 AI를 위한 기초수학, 확률 및 통계'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

print ("OK")