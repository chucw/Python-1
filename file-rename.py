import os

file_path = 'E:\\practice\\제안서\\입찰전쟁에서 승리하는 제안의 기술'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

print ("OK")