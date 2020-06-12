
(initialize)

(use-resolution t)

(assert '(exists (?e1 ?e2 ?e3 ?e4 ?e5 ?e6 ?e7 ?x2 ?x3 ?x4 ?x7 ?u)
	  (and
	   (a ?e1 ?e2)
	   (man ?e2 ?x2 ?u ?u)
	   (be_prog ?e3 ?x3 ?x2 ?e4)
	   (sit ?e4 ?x4 ?x2 ?e5)
	   (in ?e5 ?e4 ?x7)
	   (a ?e6 ?e7)
	   (field ?e7 ?x7 ?u ?u))) :name 'sentence-1)


(assert '(exists (?e1 ?e2 ?e3 ?e4 ?e5 ?e6 ?e7 ?e8 ?x3 ?x4 ?x5 ?x8 ?u)
	  (and
	   (a ?e1 ?e3)
	   (old ?e2 ?x3 ?u)
	   (man ?e3 ?x3 ?u ?u)
	   (be_prog ?e4 ?x4 ?x3 ?e5)
	   (sit ?e5 ?x5 ?x3 ?e6)
	   (in ?e6 ?e5 ?x8)
	   (a ?e7 ?e8)
	   (field ?e8 ?x8 ?u ?u))) :name 'sentence-2)


(prove '(implies
	 (exists (?e1 ?e2 ?e3 ?e4 ?e5 ?e6 ?e7 ?x2 ?x3 ?x4 ?x7 ?u)
	  (and
	   (a ?e1 ?e2)
	   (man ?e2 ?x2 ?u ?u)
	   (be_prog ?e3 ?x3 ?x2 ?e4)
	   (sit ?e4 ?x4 ?x2 ?e5)
	   (in ?e5 ?e4 ?x7)
	   (a ?e6 ?e7)
	   (field ?e7 ?x7 ?u ?u)))
	 (exists (?e1 ?e2 ?e3 ?e4 ?e5 ?e6 ?e7 ?e8 ?x3 ?x4 ?x5 ?x8 ?u)
	  (and
	   (a ?e1 ?e3)
	   (old ?e2 ?x3 ?u)
	   (man ?e3 ?x3 ?u ?u)
	   (be_prog ?e4 ?x4 ?x3 ?e5)
	   (sit ?e5 ?x5 ?x3 ?e6)
	   (in ?e6 ?e5 ?x8)
	   (a ?e7 ?e8)
	   (field ?e8 ?x8 ?u ?u)))))

(prove '(implies
	 (exists (?e1 ?e2 ?e3 ?e4 ?e5 ?e6 ?e7 ?e8 ?x3 ?x4 ?x5 ?x8 ?u)
	  (and
	   (a ?e1 ?e3)
	   (old ?e2 ?x3 ?u)
	   (man ?e3 ?x3 ?u ?u)
	   (be_prog ?e4 ?x4 ?x3 ?e5)
	   (sit ?e5 ?x5 ?x3 ?e6)
	   (in ?e6 ?e5 ?x8)
	   (a ?e7 ?e8)
	   (field ?e8 ?x8 ?u ?u)))
	 (exists (?e1 ?e2 ?e3 ?e4 ?e5 ?e6 ?e7 ?x2 ?x3 ?x4 ?x7 ?u)
	  (and
	   (a ?e1 ?e2)
	   (man ?e2 ?x2 ?u ?u)
	   (be_prog ?e3 ?x3 ?x2 ?e4)
	   (sit ?e4 ?x4 ?x2 ?e5)
	   (in ?e5 ?e4 ?x7)
	   (a ?e6 ?e7)
	   (field ?e7 ?x7 ?u ?u)))))
