(ql:quickload :cl-conllu)

(defpackage :sick
  (:use :cl :cl-conllu))

(in-package :sick)

(defun neg? (token)
  (string= "neg" (token-deprel token)))

(defun find-token (id tokens)
  (car (remove-if-not (lambda (x) (= id (token-id x))) tokens)))

(defun neg-distribution (sentences)
  (dolist (s sentences)
    (let* ((tokens (sentence-tokens s))
           (negs (remove-if-not #'neg? tokens)))
      (let ((heads (mapcar (lambda (x) (find-token (token-head x) tokens)) negs)))
        (dolist (h heads)
          (format t "~a~%" (token-upostag h)))))))

;; (neg-distribution (read-conllu #p "conll/sentences.conllu"))

(neg-distribution (read-conllu #p "conll/sentences-parsey.conllu"))

