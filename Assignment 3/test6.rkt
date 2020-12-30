#lang racket
(define (myRemove atm list)
(if (null? list)
'()
(let ((x (car list)))
((if (eqv? atm x)
(lambda (y) y)
(lambda (y) (cons x y)))
(myRemove atm (cdr list))))))
