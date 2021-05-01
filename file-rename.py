import os

#file_path = 'E:\\practice\\인프라-네트웍\\네트워크 엔지니어의 교과서'
file_path = 'D:\\temp\\Language\\Python\\파이썬을 활용한 네트워크프로그래밍'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

print ("OK")