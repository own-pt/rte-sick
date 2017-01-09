python3 process-freeling.py
ls -1 *-a.tokens |sort -g | xargs cat | ./parse.sh > sentences-a.conll
ls -1 *-b.tokens |sort -g | xargs cat | ./parse.sh > sentences-b.conll
python3 combine.py
