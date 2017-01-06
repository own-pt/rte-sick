#!/usr/bin/python3

import sys
import freeling
import csv
import subprocess
import re

## Modify this line to be your FreeLing installation directory
FREELINGDIR = "/home/fcbr/bin/freeling-4.0/";

DATA = FREELINGDIR+"/share/freeling/";
LANG="en";

freeling.util_init_locale("default");

# create language analyzer
la=freeling.lang_ident(DATA+"common/lang_ident/ident.dat");

# create options set for maco analyzer. Default values are Ok, except for data files.
op= freeling.maco_options("en");
op.set_data_files( "", 
                   DATA + "common/punct.dat",
                   DATA + LANG + "/dicc.src",
                   DATA + LANG + "/afixos.dat",
                   "",
                   DATA + LANG + "/locucions.dat", 
                   DATA + LANG + "/np.dat",
                   DATA + LANG + "/quantities.dat",
                   DATA + LANG + "/probabilitats.dat");

# create analyzers
tk=freeling.tokenizer(DATA+LANG+"/tokenizer.dat");
sp=freeling.splitter(DATA+LANG+"/splitter.dat");

mf=freeling.maco(op);

# defaults
# (umap,num,pun,dat,dic,aff,comp,rtk,mw,ner,qt,prb)=(False,True,True,True,True,True,False,True,True,True,True,True)

(umap,num,pun,dat,dic,aff,comp,rtk,mw,ner,qt,prb)=(False,True,True,True,True,True,False,True,False,False,False,True)

# activate mmorpho odules to be used in next call
mf.set_active_options(umap,num,pun,dat,dic,aff,comp,rtk,mw,ner,qt,prb)

# create tagger, sense anotator, and parsers
tg=freeling.hmm_tagger(DATA+LANG+"/tagger.dat",True,2);
sen=freeling.senses(DATA+LANG+"/senses.dat");
ukb = freeling.ukb(DATA+LANG+"/ukb.dat")

def process (lin,sumo,glos):
    sid=sp.open_session();
    l = tk.tokenize(lin);
    ls = sp.split(sid,l,False);

    ls = mf.analyze(ls);
    ls = tg.analyze(ls);
    ls = sen.analyze(ls);
    ls = ukb.analyze(ls)

    words = []
    lemmas = []
    senses = []
    concepts = []

    ## output results
    for s in ls :
        ws = s.get_words();
        for w in ws:
            words.append(w.get_form())
            lemmas.append(w.get_lemma())
            ss = w.get_senses()
            if (ss): 
                concepts.append(sumo[ss[0][0]])
                senses.append(ss[0][0])
            else:
                concepts.append("?")
                senses.append("?")

    tokenized_string = (" ".join(words))
    output = subprocess.check_output(["./parse.sh"], input = tokenized_string, universal_newlines=True)
    conll = [l.split('\t') for l in output.split('\n')]

    # 3 = lemma
    # 10 = misc

    for i in range(0, len(words)):
        conll[i][2] = lemmas[i]
        conll[i][9] = "{}|{}".format(senses[i],concepts[i])

    # clean up       
    sp.close_session(sid);

    return (conll, concepts)

def load(f,suf,sumod,glosd):
    with open(f, 'r',encoding='ISO-8859-1') as sumo:
        for line in sumo:
            line = line.strip()
            if line:
                if (line.find(";") == 0):
                    continue
                cols = line.split('|')
        
                synset = cols[0].strip().split()[0]
                m = re.search("(.*)&%(.+)$", cols[1].strip())
                sumo = "?"
                glos = ""
                if m:
                    glos = m.group(1).strip()
                    sumo = m.group(2).strip()
                else:
                    glos = cols[1].strip()
                sid = "{}-{}".format(synset,suf)
                sumod[sid] = sumo
                glosd[sid] = glos

def fix_sentence(s):
    s = s.strip()
    if (s[-1]==','):
        return "{}.".format(s[:-1])
    if (s[-1]!='.'):
        return "{}.".format(s)
    return s

sumo = {}
glos = {}

load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-adj.txt','a', sumo, glos)
load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-adv.txt','r', sumo, glos)
load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-noun.txt','n', sumo, glos)
load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-verb.txt','v', sumo, glos)

with open('SICK.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader,None)

    for row in reader:
        (pair_ID,sentence_A,sentence_B,entailment_label,relatedness_score,entailment_AB,entailment_BA,sentence_A_original,sentence_B_original,sentence_A_dataset,sentence_B_dataset,SemEval_set) = (row)
        (sentence_A, sentence_B) = (fix_sentence(sentence_A), fix_sentence(sentence_B))
        with open("{}.txt".format(pair_ID), 'w') as o:
            o.write("sentence A = {}\n".format(sentence_A))
            o.write("sentence B = {}\n".format(sentence_B))
            o.write("entailm AB = {}.\n".format(entailment_AB))
            o.write("entailm BA = {}.\n".format(entailment_BA))
            o.write("\n")

            (conlla,sensesa) = process(sentence_A, sumo, glos)
            (conllb,sensesb) = process(sentence_B, sumo, glos)

            o.write("CONCEPTS A: {}\n".format(",".join(sensesa)))
            o.write("CONCEPTS B: {}\n".format(",".join(sensesb)))

            o.write("\n")

            o.write("CONLL A:\n\n")
            
            for t in conlla:
                o.write("{}\n".format("\t".join(t)))
            o.write("CONLL B:\n\n")
            for t in conllb:

                o.write("{}\n".format("\t".join(t)))



        
