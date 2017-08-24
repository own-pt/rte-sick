
(ql:quickload :drakma)
(ql:quickload :yason)

(defun credentials (key)
  (with-open-file (in "password.lisp")
    (getf (list :user (read in) :password (read in)) key)))

(defun sentences (filename)
  (with-open-file (in filename)
    (loop for line = (read-line in nil nil)
	  while line
	  collect line)))

(defun submit-request (text user password)
  (let* ((data (with-output-to-string (s)
		 (yason:encode (alexandria:plist-hash-table `("text" ,text "source" "en" "target" "pt"))
			       s)))
	 (stream (drakma:http-request "https://gateway.watsonplatform.net/language-translator/api/v2/translate"
				      :method :post
				      :content data
				      :basic-authorization (list user password)
				      :content-type "application/json"
				      :accept "application/json"
				      :external-format-out :utf-8
				      :want-stream t)))
    (setf (flexi-streams:flexi-stream-external-format stream) :utf-8)
    (let ((obj (yason:parse stream :object-as :plist)))
      (close stream)
      obj)))


(loop for sent in (sentences "sentences-4.txt")
      collect (list sent (submit-request sent (credentials :user) (credentials :password))))
