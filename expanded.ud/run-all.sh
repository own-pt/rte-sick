python3 process-freeling.py
cat sentences.tokens | ../parse.sh > sentences-parsey.conllu
mkdir conllu
python3 combine.py
rm sentences-parsey.conllu
# cat *.conll > sentences-parsey-universal.conllu
cat conllu/*.conllu > sentences.conllu

