import os
x = os.environ['x']

f1 = open('paramsDLS001A.txt', 'r')
f2 = open('paramsDLS001' + str(x) + '.tmp.txt', 'w')
for line in f1:
    f2.write(line.replace('DLS001A', 'DLS001' + str(x)))
f1.close()
f2.close()
os.system('mv paramsDLS001' + str(x) + '.tmp.txt paramsDLS001' + str(x) + '.txt')