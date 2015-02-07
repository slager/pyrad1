#! /usr/bin/python

import os
import string
import subprocess

os.chdir('/Users/dave/DLS001')  #Change to '/Users/dave/DLS001' for final
os.mkdir('fastq_collection')
os.mkdir('stats_collection')

for x in string.uppercase[0:6]:
  subprocess.call("date")
  print('DLS001' + x)
  f1 = open('paramsDLS001A.txt', 'r')
  f2 = open('paramsDLS001' + x + '.tmp.txt', 'w')
  for line in f1:
    f2.write(line.replace('DLS001A', 'DLS001' + str(x)))
  f1.close()
  f2.close()
  subprocess.call('mv paramsDLS001' + x + '.tmp.txt paramsDLS001' + str(x) + '.txt',shell=True)
  subprocess.call('/Users/dave/pyrad/pyRAD -p /Users/dave/DLS001/paramsDLS001' + x + '.txt -s 1',shell=True)
  subprocess.call('cp fastq/* fastq_collection',shell=True)
  subprocess.call('rm fastq/*',shell=True)
  subprocess.call('rmdir fastq',shell=True)
  subprocess.call('cp stats/s1.sorting.txt stats_collection/DLS001' + x + '.s1.sorting.txt',shell=True)
  subprocess.call('rm stats/s1.sorting.txt',shell=True)
subprocess.call('rmdir stats',shell=True)
subprocess.call("date")