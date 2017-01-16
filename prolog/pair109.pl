%% -*- prolog -*-

%% sentence
nlp_sentence(s109b).
nlp_sentence(s109a).

%% idx
nlp_index(s109b,i9,9).
nlp_index(s109b,i8,8).
nlp_index(s109b,i7,7).
nlp_index(s109b,i6,6).
nlp_index(s109b,i5,5).
nlp_index(s109b,i4,4).
nlp_index(s109b,i3,3).
nlp_index(s109b,i2,2).
nlp_index(s109b,i1,1).
nlp_index(s109a,i8,8).
nlp_index(s109a,i7,7).
nlp_index(s109a,i6,6).
nlp_index(s109a,i5,5).
nlp_index(s109a,i4,4).
nlp_index(s109a,i3,3).
nlp_index(s109a,i2,2).
nlp_index(s109a,i1,1).

%% form
nlp_form(s109b,i9,'.').
nlp_form(s109b,i8,'match').
nlp_form(s109b,i7,'football').
nlp_form(s109b,i6,'a').
nlp_form(s109b,i5,'in').
nlp_form(s109b,i4,'competing').
nlp_form(s109b,i3,'are').
nlp_form(s109b,i2,'teams').
nlp_form(s109b,i1,'Two').
nlp_form(s109a,i8,'.').
nlp_form(s109a,i7,'football').
nlp_form(s109a,i6,'playing').
nlp_form(s109a,i5,'are').
nlp_form(s109a,i4,'people').
nlp_form(s109a,i3,'of').
nlp_form(s109a,i2,'groups').
nlp_form(s109a,i1,'Two').

%% lemma
nlp_lemma(s109b,i9,'.').
nlp_lemma(s109b,i8,'match').
nlp_lemma(s109b,i7,'football').
nlp_lemma(s109b,i6,'a').
nlp_lemma(s109b,i5,'in').
nlp_lemma(s109b,i4,'compete').
nlp_lemma(s109b,i3,'be').
nlp_lemma(s109b,i2,'team').
nlp_lemma(s109b,i1,'2').
nlp_lemma(s109a,i8,'.').
nlp_lemma(s109a,i7,'football').
nlp_lemma(s109a,i6,'play').
nlp_lemma(s109a,i5,'be').
nlp_lemma(s109a,i4,'people').
nlp_lemma(s109a,i3,'of').
nlp_lemma(s109a,i2,'group').
nlp_lemma(s109a,i1,'2').

%% pos
nlp_pos(s109b,i9,'.').
nlp_pos(s109b,i8,'NOUN').
nlp_pos(s109b,i7,'NOUN').
nlp_pos(s109b,i6,'DET').
nlp_pos(s109b,i5,'ADP').
nlp_pos(s109b,i4,'VERB').
nlp_pos(s109b,i3,'VERB').
nlp_pos(s109b,i2,'NOUN').
nlp_pos(s109b,i1,'NUM').
nlp_pos(s109a,i8,'.').
nlp_pos(s109a,i7,'NOUN').
nlp_pos(s109a,i6,'VERB').
nlp_pos(s109a,i5,'VERB').
nlp_pos(s109a,i4,'NOUN').
nlp_pos(s109a,i3,'ADP').
nlp_pos(s109a,i2,'NOUN').
nlp_pos(s109a,i1,'NUM').

%% num
nlp_num(s109b,i1,i2).
nlp_num(s109a,i1,i2).

%% nsubj
nlp_nsubj(s109b,i2,i4).
nlp_nsubj(s109a,i2,i6).

%% prep
nlp_prep(s109b,i5,i4).
nlp_prep(s109a,i3,i2).

%% pobj
nlp_pobj(s109b,i8,i5).
nlp_pobj(s109a,i4,i3).

%% aux
nlp_aux(s109b,i3,i4).
nlp_aux(s109a,i5,i6).

%% ROOT
nlp_sent_root(s109b,i4).
nlp_sent_root(s109a,i6).

%% dobj
nlp_dobj(s109a,i7,i6).

%% punct
nlp_punct(s109b,i9,i4).
nlp_punct(s109a,i8,i6).

%% det
nlp_det(s109b,i6,i8).

%% nn
nlp_nn(s109b,i7,i8).
