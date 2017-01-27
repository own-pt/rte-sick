#pos=$(mktemp)

for f in $(cat conllu/*.conllu | awk -F '\t' '{print $4}' | sort | uniq); do
    cat conllu/*.conllu | awk -F '\t' "\$4~/^$f$/ {print \$3}" | sort | uniq -c | sort -rn > lemmas/lemmas-$f.txt
done
