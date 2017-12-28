#add_data
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

f = open("새파일.txt",'a')

for i in range(11,21):
    f.write("%d번째 줄입니다.\n" % i)

f.close()
