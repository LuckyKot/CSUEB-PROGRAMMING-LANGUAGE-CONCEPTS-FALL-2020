#lang racket
(define (mod N M)
(define k(quotient N M))
(define l(* M k))
(- N l))

(define (binaryToDecimal b)
(if (= b 0)     
0
(+ (mod b 10) (* 2 (binaryToDecimal (quotient b 10))))))
