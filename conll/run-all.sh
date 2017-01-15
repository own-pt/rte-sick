python3 process-freeling-unique.py
cat sentences.tokens | ../parsey.sh > sentences-parsey.conllu
python3 combine-unique.py
rm sentences-parsey.conllu
cat *.conll > sentences-parsey.conllu
