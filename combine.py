#!/usr/bin/python3

import sys
import csv
import subprocess
import re

def fix_sentence(s):
    s = s.strip()
    if (s[-1]==','):
        return "{}.".format(s[:-1])
    if (s[-1]!='.'):
        return "{}.".format(s)
    return s

def read_file(s):
    l = []
    with open(s,'r') as i:
        for f in i:
            l.append(f.strip())
    return l

def read_conll(s):
    with open(s,'r') as i:
        return i.read().split('\n\n')

def fix_conll(raw_conll, lemmas, senses, sumo):
    conll = [l.split('\t') for l in raw_conll.split('\n')]
    assert (len(conll) == len(lemmas) == len(senses) == len(sumo)), "{} {} {} {}".format(len(conll), len(lemmas), len(senses), len(sumo))
    for i in range(0, len(lemmas)):
        conll[i][2] = lemmas[i]
        conll[i][9] = "{}|{}".format(senses[i],sumo[i])
    return conll

with open('SICK.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader,None)

    i = 0
    for row in reader:
        (pair_ID,sentence_A,sentence_B,entailment_label,relatedness_score,entailment_AB,entailment_BA,sentence_A_original,sentence_B_original,sentence_A_dataset,sentence_B_dataset,SemEval_set) = (row)
        (sentence_A, sentence_B) = (fix_sentence(sentence_A), fix_sentence(sentence_B))

        senses_a = read_file('{}-a.senses'.format(pair_ID))[0].split(',')
        sumo_a = read_file('{}-a.sumo'.format(pair_ID))[0].split(',')
        lemmas_a = read_file('{}-a.lemmas'.format(pair_ID))[0].split('+')
        senses_b = read_file('{}-b.senses'.format(pair_ID))[0].split(',')
        sumo_b = read_file('{}-b.sumo'.format(pair_ID))[0].split(',')
        lemmas_b = read_file('{}-b.lemmas'.format(pair_ID))[0].split('+')

        conll_a = read_conll('sentences-a.conll')
        conll_b = read_conll('sentences-b.conll')

        (conlla) = fix_conll(conll_a[i], lemmas_a, senses_a, sumo_a)
        (conllb) = fix_conll(conll_b[i], lemmas_b, senses_b, sumo_b)

        i = i +1
        with open("{}-a.conll".format(pair_ID), 'w') as o:
            o.write("# sent_id = {}a\n".format(pair_ID));
            o.write("# text = {}\n".format(sentence_A));
            for t in conlla:
                o.write("{}\n".format("\t".join(t)))
            o.write('\n')

        with open("{}-b.conll".format(pair_ID), 'w') as o:
            o.write("# sent_id = {}b\n".format(pair_ID));
            o.write("# text = {}\n".format(sentence_B));
            for t in conllb:
                o.write("{}\n".format("\t".join(t)))
            o.write('\n')

        with open("{}.txt".format(pair_ID), 'w') as o:
            o.write("sentence A = {}\n".format(sentence_A))
            o.write("sentence B = {}\n".format(sentence_B))
            o.write("entailm AB = {}.\n".format(entailment_AB))
            o.write("entailm BA = {}.\n".format(entailment_BA))
            o.write("\n")

            o.write("CONCEPTS A: {}\n".format(",".join([x for x in sumo_a if x != '?'])))
            o.write("CONCEPTS B: {}\n".format(",".join([x for x in sumo_b if x != '?'])))

            o.write("\n")

            o.write("CONLL A:\n\n")
            
            for t in conlla:
                o.write("{}\n".format("\t".join(t)))

            o.write("\n\nCONLL B:\n\n")
            for t in conllb:
                o.write("{}\n".format("\t".join(t)))
