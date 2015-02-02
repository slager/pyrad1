# bash script for pyrad step 1

cd /Users/dave/DLS001
mkdir fastq_collection2
mkdir stats_collection2

for x in {A..F}
do
  date
  echo "DLS001$x"
  /Users/dave/pyrad/pyRAD -p /Users/dave/DLS001/paramsDLS001${x}.txt -s 1
  cp fastq/* fastq_collection2
  rm fastq/*
  rmdir fastq
  cp stats/s1.sorting.txt stats_collection2/DLS001${x}.s1.sorting.txt
  rm stats/s1.sorting.txt
done
date