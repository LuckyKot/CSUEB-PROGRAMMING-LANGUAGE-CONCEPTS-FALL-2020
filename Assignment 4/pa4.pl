use_module(library(random)).

male(andrew).
male(pavel).
male(alexander).
male(nikita).
male(yuri).
male(igor).
male(michael).

female(ana).
female(kathy).
female(christine).
female(valerie).
female(claire).

father(michael, igor).
father(yuri, christine).
father(yuri, nikita).
father(nikita,alexander).

mother(claire,ana).
mother(kathy, igor).
mother(valerie, christine).
mother(valerie, nikita).
mother(ana,alexander).


sibling(X,Y) :-
    father(Z,X),
    father(Z,Y),
    mother(A,X),
    mother(A,Y).

sister(X,Y) :-
    father(Z,X),
    father(Z,Y),
    mother(A,X),
    mother(A,Y),
    female(X),
    Y\=X.

%alexander gs yuri,
%alexander gs claire

grandson(X,Y) :-
	mother(D,X),
    mother(Y,D),
    male(X).

grandson(X,Y) :-
   father(D,X),
   father(Y,D),
   male(X).

descendant(X,Y) :-
    father(Y,X).

descendant(X,Y) :-
    mother(Y,X).

descendant(X,Y) :-
	father(D,X),
	father(Y,D).

descendant(X,Y) :-
    mother(D,X),
    mother(Y,D).

remove(E,[E|L],L).
remove(E,[A|L],[A|R]) :-remove(E,L,R).

subsequence(L1,L2):- 
   subset(L1,L2).

%How many different proofs are there for each of the following queries?
% 1,1,3,4 
% 1 - a,d only once in the program
% 1 - b,a only once in the program
% 3 - it basically should take every pair, b,a a,d d,a
% 4 - S is only one symbol, so it will go through each single symbol and of course it will match

add_list(X,Y):-
     append(X,Y,Z),
     sort(Z,A),
	 write(A).

%simply writes out every item of the list 1 by 1
write_list([]).
write_list([Head|Tail]) :-
    write(Head), nl,
    write_list(Tail).







