::::::::::::::::::::::: University of Trento - Italy ::::::::::::::::::::::::::::::::

:::::::::::: SICK (Sentences Involving Compositional Knowledge) data set ::::::::::::

:::::::::::::::::::::http://clic.cimec.unitn.it/composes/sick/ ::::::::::::::::::::::


The SICK data set consists of 10,000 English sentence pairs, built starting from two existing 
paraphrase sets: the 8K ImageFlickr data set (http://nlp.cs.illinois.edu/HockenmaierGroup/data.html) 
and the SEMEVAL-2012 Semantic Textual Similarity Video Descriptions data set 
(http://www.cs.york.ac.uk/semeval-2012/task6/index.php?id=data). Each sentence pair is annotated 
for relatedness in meaning and for the entailment relation between the two elements.



The SICK data set is released under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 
Unported License (http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US)

When using SICK in published research, please cite:
M. Marelli, S. Menini, M. Baroni, L. Bentivogli, R. Bernardi and R. Zamparelli. 2014. A SICK cure 
for the evaluation of compositional distributional semantic models. Proceedings of LREC 2014, 
Reykjavik (Iceland): ELRA. 



The SICK data set is used in SemEval 2014 - Task 1: Evaluation of compositional distributional 
semantic models on full sentences through semantic relatedness and textual entailment



This file includes indexes specifying, for each sentence pair, whether it was included in the each
of the subsets described and analyzed in:
Bentivogli et al. (under review). SICK Through the SemEval Glasses. Lesson learned from the evaluation 
of compositional distributional semantic models on full sentences through semantic relatedness and 
textual entailment

 

File Structure: tab-separated text file

Fields:

- pair_ID: sentence pair ID

- balanced: inclusion in the balanced subset (1= included pair)

- ENT_lowvariance: inclusion in the low-variance subset based of the entailment task (1= included pair)

- REL_lowvariance: inclusion in the low-variance subset based of the relatedness task (1= included pair)

- ENT_difficult: inclusion in the difficult subset for the entailment task (1= included pair)

- REL_difficult: inclusion in the difficult subset for the relatedness task (1= included pair)

