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
                if ss[0][0] in sumo:
                    concepts.append(sumo[ss[0][0]])
                else:
                    concepts.append("?")
                senses.append(ss[0][0])
            else:
                concepts.append("?")
                senses.append("?")

    tokenized_string = (" ".join(words))

    # clean up       
    sp.close_session(sid);

    return (tokenized_string,lemmas,senses,concepts)

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

sumo_dic = {}
glos_dic = {}

load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-adj.txt','a', sumo_dic, glos_dic)
load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-adv.txt','r', sumo_dic, glos_dic)
load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-noun.txt','n', sumo_dic, glos_dic)
load('/home/fcbr/repos/sumo/KBs/WordNetMappings/WordNetMappings30-verb.txt','v', sumo_dic, glos_dic)

with open('SICK.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader,None)

    for row in reader:
        (pair_ID,sentence_A,sentence_B,entailment_label,relatedness_score,entailment_AB,entailment_BA,sentence_A_original,sentence_B_original,sentence_A_dataset,sentence_B_dataset,SemEval_set) = (row)
        (sentence_A, sentence_B) = (fix_sentence(sentence_A), fix_sentence(sentence_B))
        
        (txt,lemmas,senses,sumo) = process(sentence_A,sumo_dic,glos_dic)
        with open('{}-a.tokens'.format(pair_ID),'w') as o:
            o.write("{}\n".format(txt))
        with open('{}-a.lemmas'.format(pair_ID),'w') as o:
            o.write("{}\n".format("+".join(lemmas)))
        with open('{}-a.senses'.format(pair_ID),'w') as o:
            o.write("{}\n".format(",".join(senses)))
        with open('{}-a.sumo'.format(pair_ID),'w') as o:
            o.write("{}\n".format(",".join(sumo)))

        (txt,lemmas,senses,sumo) = process(sentence_B,sumo_dic,glos_dic)
        with open('{}-b.tokens'.format(pair_ID),'w') as o:
            o.write("{}\n".format(txt))
        with open('{}-b.lemmas'.format(pair_ID),'w') as o:
            o.write("{}\n".format("+".join(lemmas)))
        with open('{}-b.senses'.format(pair_ID),'w') as o:
            o.write("{}\n".format(",".join(senses)))
        with open('{}-b.sumo'.format(pair_ID),'w') as o:
            o.write("{}\n".format(",".join(sumo)))
