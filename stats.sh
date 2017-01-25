#!/bin/bash

cat SICK.txt | awk -F '\t' 'NR > 1 {print $2}' > x
cat SICK.txt | awk -F '\t' 'NR > 1 {print $3}' > y
cat x y | sort | uniq > expanded.txt
cat expanded.txt | tr '[:blank:]' '\n' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn > expanded.words.txt

cat SICK.txt | awk -F '\t' 'NR > 1 {print $8}' > x  
cat SICK.txt | awk -F '\t' 'NR > 1 {print $9}' > y
cat x y | sort | uniq > originals.txt
cat originals.txt | tr '[:blank:]' '\n' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn > originals.words.txt
rm x y
