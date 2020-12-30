#lang racket
(define (mod N M)
(define k(quotient N M))
(define l(* M k))
(- N l))