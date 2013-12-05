mylang
======

following McCarthy's 1960 essay on implementing lisp as well as some of Graham's essay on the "Roots of Lisp"

two implementations of lisp. first one is the Lisp in Common Lisp. second one is lisp written in python, which is more
likely to be considered a scheme than a lisp.

  -something wrong with lambda(label in lisplisp)
  
  -lambda and define work fine in lispy, though cons is missing

third implementation will be in ruby. have only initialized the file -- no commits yet.

in order to test my implementations of lisp:
1. lisp in lisp
	a. use sbcl (steel bank commmon lisp)
	b. load file and then check -eval
	c. runnable examples:
		>(-eval 'x '((x a) (y b)))
		a

	my functions that are implemented begin with a hyphen, '-', otherwise I'm using the sbcl functions

2. lisp/scheme in python
	a. use 2.X Python
	b. evaluate the python file into a python REPL
	c. use the command evalLoop() to start the repl in order to test my lisp
	d. runable examples:
		> (= 'this 'this)
		T
		> (define foo (lambda (x) (* x x)))
		None --> however in reality you've made the function foo
		> (foo 2)
		4