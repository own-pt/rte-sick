python3 process-freeling.py
for f in pairs.*; do
    pushd $f
    ls -1 *-a.tokens | sort -g | xargs cat | ../parsey.sh > sentences-a.conll
    ls -1 *-b.tokens | sort -g | xargs cat | ../parsey.sh > sentences-b.conll
    popd
done
for f in pairs.*; do
    pushd $f
    python3 ../combine.py
    popd
done
