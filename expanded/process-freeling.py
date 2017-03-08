#!/usr/bin/python3

import sys
import freeling
import csv
import subprocess
import re
import hashlib
import os

## Modify this line to be your FreeLing installation directory
FREELINGDIR = "/home/fcbr/bin/freeling-4.0";
SUMODIR="/home/fcbr/repos/sumo/KBs";

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
    ls = sp.split(sid,l,True);

    ls = mf.analyze(ls);
    ls = tg.analyze(ls);
    ls = sen.analyze(ls);
    ls = ukb.analyze(ls)

    words = []
    lemmas = []
    senses = []
    concepts = []
    pos = []

    ## output results
    for s in ls :
        ws = s.get_words();
        for w in ws:
            words.append(w.get_form())
            lemmas.append(w.get_lemma())
            # see https://github.com/TALP-UPC/FreeLing/issues/33
            # pos.append(w.get_tag()+"|"+bin(w.get_analyzed_by()))
            pos.append(w.get_tag())
            ss = w.get_senses()
            if (ss): 
                local_senses = []
                local_concepts = []

                for (sense,score) in ss:
                    if sense in sumo:
                        local_concepts.append(sumo[sense])
                    else:
                        local_concepts.append('?')
                    local_senses.append(sense)
                concepts.append(local_concepts)
                senses.append(local_senses)
            else:
                concepts.append('?')
                senses.append('?')

    tokenized_string = (" ".join(words))

    # clean up       
    sp.close_session(sid);

    return (tokenized_string,lemmas,senses,concepts,pos)

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

sumo_dic = {}
glos_dic = {}

load(SUMODIR+'/WordNetMappings/WordNetMappings30-adj.txt','a', sumo_dic, glos_dic)
load(SUMODIR+'/WordNetMappings/WordNetMappings30-adv.txt','r', sumo_dic, glos_dic)
load(SUMODIR+'/WordNetMappings/WordNetMappings30-noun.txt','n', sumo_dic, glos_dic)
load(SUMODIR+'/WordNetMappings/WordNetMappings30-verb.txt','v', sumo_dic, glos_dic)

sentences = []
with open('../SICK.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader,None)

    for row in reader:
        (pair_ID,sentence_A,sentence_B,entailment_label,relatedness_score,entailment_AB,entailment_BA,sentence_A_original,sentence_B_original,sentence_A_dataset,sentence_B_dataset,SemEval_set) = (row)
        sentences.append(sentence_A.strip())
        sentences.append(sentence_B.strip())

sentences = list(set(sentences))

with open('sentences.txt', 'w') as o:
    for sentence in sentences:
        o.write("{}\n".format(sentence))

with open('sentences.tokens', 'w') as senf:
    for sentence in sentences:

        id = hashlib.sha1(sentence.encode('utf-8')).hexdigest()

        # if (os.path.exists('{}.tokens'.format(id))):
        #     print ("Collision!")
        #     sys.exit(1)

        (txt,lemmas,senses,sumo,tag) = process(sentence,sumo_dic,glos_dic)
            
        senf.write("{}\n".format(txt))

        with open('{}.tokens'.format(id),'w') as o:
            o.write("{}\n".format(txt))
        with open('{}.lemmas'.format(id),'w') as o:
            o.write("{}\n".format("+".join(lemmas)))
        with open('{}.senses'.format(id),'w') as o:
            o.write("{}\n".format(",".join([".".join(x) for x in senses])))
        with open('{}.sumo'.format(id),'w') as o:
            o.write("{}\n".format(",".join([".".join(x) for x in sumo])))
        with open('{}.tag'.format(id),'w') as o:
            o.write("{}\n".format(",".join(tag)))
