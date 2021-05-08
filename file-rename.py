import os

file_path = 'E:\\practice\\Language\\스프링5와 Vue-js로 시작하는 모던 웹 애플리케이션 개발'
#file_path = 'D:\\temp\\System\\\\Docker'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

print ("OK")