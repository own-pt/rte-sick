#!/usr/bin/python3

import sys
import csv
import subprocess
import re
import hashlib

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

def fix_conll(raw_conll, lemmas, senses, sumo,pos):
    conll = [l.split('\t') for l in raw_conll.split('\n')]
    assert (len(conll) == len(lemmas) == len(senses) == len(sumo)), "{} {} {} {}".format(len(conll), len(lemmas), len(senses), len(sumo))
    for i in range(0, len(lemmas)):
        conll[i][2] = lemmas[i]
        conll[i][9] = "{}|{}|{}".format(pos[i],senses[i],sumo[i])
    return conll

with open('../numbers.sentences', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader,None)

    i = 0
    for row in reader:
        (sentence,number) = (row)
        sentence = fix_sentence(sentence)

        id = hashlib.sha1(sentence.encode('utf-8')).hexdigest()

        senses_a = read_file('{}.senses'.format(id))[0].split(',')
        sumo_a = read_file('{}.sumo'.format(id))[0].split(',')
        pos_a = read_file('{}.tag'.format(id))[0].split(',')
        lemmas_a = read_file('{}.lemmas'.format(id))[0].split('+')

        conll_a = read_conll('sentences-parsey.conllu')

        (conlla) = fix_conll(conll_a[i], lemmas_a, senses_a, sumo_a, pos_a)

        i = i + 1
        with open("{}.conll".format(id), 'w') as o:
            o.write("# text = {}\n".format(sentence));
            for t in conlla:
                o.write("{}\n".format("\t".join(t)))
            o.write('\n')
