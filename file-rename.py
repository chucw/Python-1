import os

file_path = 'E:\\practice\\Data Science\\Kaggle 파이썬을 활용한 머신러닝 실전 예제 분석'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

print ("OK")