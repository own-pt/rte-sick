python3 process-freeling-unique.py
cat sentences.tokens | ../parse.sh > sentences.conll
python3 combine-unique.py
rm sentences.conll
cat *.conll > sentences.conll
