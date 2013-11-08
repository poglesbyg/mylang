;;; mylisp is an implementation of McCarthy's Lisp
;;; going to include numbers and strings
;;; by Paul Grant

(defun -eval (expr env)
  (cond
    ((atom expr) (cdr (assoc expr env)))
    ((eq 'atom (car expr)) (-atom (-eval (cadr expr) env)))
    ((eq 'quote (car expr)) (-quote expr))
    ((eq 'car (car expr)) (-car (-eval (cadr expr) env)))
    ((eq 'cdr (car expr)) (-cdr (-eval (cadr expr) env)))
    ((eq 'cons (car expr)) (-cons (-eval (cadr expr) env)
				  (-eval (caddr expr) env)))
    ((eq 'eq (car expr)) (-eq (-eval (cadr expr) env)
			      (-eval (caddr expr) env)))
    ((eq 'cond (car expr)) (-cond (cadr expr) env))))

(defun -atom (expr)
  (atom expr))

(defun -quote (expr)
  (cadr expr))

(defun -car (expr)
  (car expr))

(defun -cdr (expr)
  (cdr expr))

(defun -cons (expr1 expr2)
  (cons expr1 expr2))

(defun -eq (expr1 expr2)
  (eq expr1 expr2))

(defun -cond (expr env)
  (cond
    ((null expr) nil)
    ((-eval (caar expr) env) (-eval (cadar expr) env))
    (t (-cond (cdr expr) env))))
