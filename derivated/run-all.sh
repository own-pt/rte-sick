python3 process-freeling.py
cat sentences.tokens | ../parsey.sh > sentences-parsey.conllu
python3 combine.py
rm sentences-parsey.conllu
cat *.conll > sentences-parsey.conllu
