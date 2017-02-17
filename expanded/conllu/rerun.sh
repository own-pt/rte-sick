#!/bin/bash

rm len.3-5.*
cat len.[0-9]*.conllu > all.conllu
cat len.3.conllu len.4.conllu len.5.conllu > len.3-5.conllu

for f in *.conllu; do 
    ./neg.sh $f
    ./root.sh $f
    cat $f | ~/repos/ud/tools/conllu-stats.pl > $f.stats.xml
done
