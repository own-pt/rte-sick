cat $1 | grep $'\tROOT\t' | awk -F '\t' '{print $4}' | sort | uniq -c | sort -rn > $1.root.txt

