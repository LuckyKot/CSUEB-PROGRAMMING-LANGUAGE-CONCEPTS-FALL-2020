#lang racket
(define (min list)
(if (= (length list) 0) (display "no list")
(cond ((null? (cdr list)) (car list))
((< (car list) (min (cdr list))) (car list))
(else (min (cdr list))))))
