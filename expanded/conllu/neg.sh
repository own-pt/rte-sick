cat $1 | awk '$8 ~ /ROOT/ {print $4}' | sort | uniq -c | sort -rn > $1.neg.txt

