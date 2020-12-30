#lang racket
(define (mod N M)
(define k(quotient N M))
(define l(* M k))
(- N l))

(define (binaryToDecimal b)
(if (= b 0)
0
(+ (mod b 10) (* 2 (binaryToDecimal (quotient b 10))))))

(define (addBinary binaryList)
(if (null? binaryList)
0
(+ (binaryToDecimal (car binaryList)) (addBinary (cdr binaryList)))))