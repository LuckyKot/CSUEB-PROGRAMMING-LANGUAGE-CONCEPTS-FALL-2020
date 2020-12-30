#lang racket
(define (binomial N k)
(if (= k 0)
1
(if (= k N)
1
(+ (binomial (- N 1) k) (binomial (- N 1) (- k 1))))))