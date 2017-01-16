%% -*- prolog -*-

%% sentence
nlp_sentence(s3885b).
nlp_sentence(s3885a).

%% idx
nlp_index(s3885b,i5,5).
nlp_index(s3885b,i4,4).
nlp_index(s3885b,i3,3).
nlp_index(s3885b,i2,2).
nlp_index(s3885b,i1,1).
nlp_index(s3885a,i5,5).
nlp_index(s3885a,i4,4).
nlp_index(s3885a,i3,3).
nlp_index(s3885a,i2,2).
nlp_index(s3885a,i1,1).

%% form
nlp_form(s3885b,i5,'.').
nlp_form(s3885b,i4,'dancing').
nlp_form(s3885b,i3,'is').
nlp_form(s3885b,i2,'male').
nlp_form(s3885b,i1,'A').
nlp_form(s3885a,i5,'.').
nlp_form(s3885a,i4,'dancing').
nlp_form(s3885a,i3,'is').
nlp_form(s3885a,i2,'man').
nlp_form(s3885a,i1,'A').

%% lemma
nlp_lemma(s3885b,i5,'.').
nlp_lemma(s3885b,i4,'dance').
nlp_lemma(s3885b,i3,'be').
nlp_lemma(s3885b,i2,'male').
nlp_lemma(s3885b,i1,'a').
nlp_lemma(s3885a,i5,'.').
nlp_lemma(s3885a,i4,'dance').
nlp_lemma(s3885a,i3,'be').
nlp_lemma(s3885a,i2,'man').
nlp_lemma(s3885a,i1,'a').

%% pos
nlp_pos(s3885b,i5,'.').
nlp_pos(s3885b,i4,'VERB').
nlp_pos(s3885b,i3,'VERB').
nlp_pos(s3885b,i2,'NOUN').
nlp_pos(s3885b,i1,'DET').
nlp_pos(s3885a,i5,'.').
nlp_pos(s3885a,i4,'VERB').
nlp_pos(s3885a,i3,'VERB').
nlp_pos(s3885a,i2,'NOUN').
nlp_pos(s3885a,i1,'DET').

%% det
nlp_det(s3885b,i1,i2).
nlp_det(s3885a,i1,i2).

%% nsubj
nlp_nsubj(s3885b,i2,i4).
nlp_nsubj(s3885a,i2,i4).

%% aux
nlp_aux(s3885b,i3,i4).
nlp_aux(s3885a,i3,i4).

%% ROOT
nlp_sent_root(s3885b,i4).
nlp_sent_root(s3885a,i4).

%% punct
nlp_punct(s3885b,i5,i4).
nlp_punct(s3885a,i5,i4).

intransitive_action(S, A, X) :-
        nlp_sent_root(S,T),
        nlp_pos(S,T,'VERB'),
        nlp_lemma(S,T,A),
        nlp_aux(S,BE,T),
        nlp_lemma(S,BE,'be'),
        nlp_nsubj(S,X1,T),
        nlp_lemma(S,X1,X).

dance(A) :-
        intransitive_action(_, 'dance', A).

entails('dance', 'dance').
entails('man', 'male').
entails('male','man').

entails(S1, S2) :-
        intransitive_action(S1, A1, T1),
        intransitive_action(S2, A2, T2),
        entails(A1, A2),
        entails(T1, T2).
