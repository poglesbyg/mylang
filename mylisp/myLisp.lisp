;;; Mylisp is an implementation of McCarthy's Lisp
;;; going to include numbers and strings
;;; by Paul Grant


(defun -eval (expr env)
  (cond
    ((atom expr) (cdr (-assoc expr env)))
    ((atom (car expr))
     (cond
      ((eq 'atom (car expr)) (-atom (-eval (cadr expr) env)))

      ((eq 'quote (car expr)) (-quote expr))

      ((eq 'car (car expr)) (-car (-eval (cadr expr) env)))

      ((eq 'cdr (car expr)) (-cdr (-eval (cadr expr) env)))

      ((eq 'cons (car expr)) (-cons (-eval (cadr expr) env)
				   (-eval (caddr expr) env)))

      ((eq 'eq (car expr)) (-eq (-eval (cadr expr) env)
			       (-eval (caddr expr) env)))

      ((eq '+ (car expr)) (+ (-eval (cadr expr) env)
			     (-eval (caddr expr) env)))

      ((eq '- (car expr)) (- (-eval (cadr expr) env)
			     (-eval (caddr expr) env)))

      ((eq '* (car expr)) (* (-eval (cadr expr) env)
			     (-eval (caddr expr) env)))

      ((eq '/ (car expr)) (/ (-eval (cadr expr) env)
			     (-eval (caddr expr) env)))

      ((eq (car expr) 'cond) (-evcond (car expr) env))

      ('t (-eval (cons (-assoc (car expr) env)
		       (cdr env))
		 env))))
    ((eq 'label (caar expr))
     (-eval (cons (caddar expr) (cdr expr))
	    (cons (list (cadar expr) (car expr)) env)))
    ((eq 'lambda (caar expr))
     (-eval (caddar expr)
	    (-append (-pair (cadar expr) (-evlis (cdr expr) env))
		     env)))))
(defun -evlis (expr1 expr2)
  (cond ((-null expr1) '())
	('t (cons (-eval (car expr1) expr2)
		  (-evlis (cdr expr1) expr2)))))

(defun -evcond (expr env)
  (cond ((-eval (caar expr) env)
	 (-eval (cadar expr) env))
	('t (-evcond (cdr expr) env))))

(defun -atom (expr)
  (atom expr))

(defun -quote (expr)
  (cadr expr))

(defun -car (expr)
  (car expr))

(defun -cdr (expr)
  (cdr expr))

(defun -eq (expr1 expr2)
  (eq expr1 expr2))

(defun -null (expr)
  (-eq expr '()))

(defun -and (expr1 expr2)
  (cond (expr1 (cond (expr2 't) ('t '())))
	('t '())))

(defun -not (expr)
  (cond (expr '())
	('t 't)))

(defun -append (expr1 expr2)
  (cond ((-null expr1) expr2)
	('t (cons (car expr1) (-append (cdr expr1) expr2)))))


(defun -pair (expr1 expr2)
  (cond ((-and (-null expr1) (-null expr2)) '())
	((-and (-not (atom expr1)) (-not (atom expr2)))
	 (cons (list (car expr1) (car expr2))
	       (-pair (cdr expr1) (cdr expr2))))))

(defun -assoc (expr1 expr2)
  (cond ((eq (caar expr2) expr1) (cadr expr2))
	('t (-assoc expr1 (cdr expr2)))))

(defun -cons (expr1 expr2)
  (cons expr1 expr2))


;(print (-eval (read)))



