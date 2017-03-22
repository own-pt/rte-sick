#!/bin/bash

for f in *.conllu; do 
    ./neg.sh $f
    ./root.sh $f
    cat $f | ~/repos/ud/tools/conllu-stats.pl > $f.stats.xml
done
