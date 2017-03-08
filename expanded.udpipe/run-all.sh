cat ../expanded.ud/sentences.conllu | awk -F $'\t' 'OFS="\t" {print $2}' | cat -s > sentences.verticalized                 
~/bin/udpipe.sh --input=vertical --tag --parse sentences.verticalized > sentences.conllu
