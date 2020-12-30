#lang racket
(define (selectionSort list) 
(cond ( (null? list) '() )
( else (cons (min list (car list)) 
(selectionSort (myRemove list (min list (car list))))))))

(define (myRemove x y)
(cond ( (null? x) '() )           
( (= (car x) y) (cdr x)) 
(else (cons (car x)(myRemove (cdr x) y)))))

(define (min x y)
(cond ( (null? x) y)
( (< (car x) y) (min (cdr x)(car x)))
(else (min (cdr x) y ))))