:- discontiguous male/1, female/1, married/2, parentOf/2, family/2, childOf/2, siblings/2.

/* 1. male  */

male(tiger).
male(yuvi).
male(navi).
male(pitaji).
male(baba).
male(ram).
male(sam).
male(ross).

/* 2. Female */

female(maa).
female(dadi).
female(fuwa).
female(chachi).

/* 3. married */

married(pitaji,maa).
married(maa, pitaji).
married(baba,dadi).
married(dadi,baba).
married(ram,chachi).
married(chachi,ram).

/*  4. parentof(child, parent) */

parentOf(tiger,pitaji).
parentOf(tiger,maa).
parentOf(yuvi,pitaji).
parentOf(yuvi,maa).
parentOf(navi,pitaji).
parentOf(navi,maa).
parentOf(pitaji,baba).
parentOf(pitaji,dadi).
parentOf(ram,baba).
parentOf(ram,dadi).
parentOf(fuwa,baba).
parentOf(fuwa,dadi).
parentOf(sam,ram).
parentOf(sam,chachi).
parentOf(ross,ram).
parentOf(ross,chachi).

/* 5. childOf(parent,chlid)*/

childOf(pitaji,tiger).
childOf(pitaji,yuvi).
childOf(pitaji,navi).
childOf(maa,tiger).
childOf(maa,yuvi).
childOf(maa,navi).
childOf(baba,pitaji).
childOf(dadi,pitaji).
childOf(baba,ram).
childOf(dadi,ram).
childOf(baba,fuwa).
childOf(dadi,fuwa).
childOf(ram,sam).
childOf(chachi,sam).
childOf(ram,ross).
childOf(chachi,ross).

/* 6. siblings */

siblings(tiger,yuvi).
siblings(yuvi,tiger).
siblings(tiger,navi).
siblings(navi,tiger).
siblings(pitaji,ram).
siblings(ram,pitaji).
siblings(sam,ross).
siblings(ross,sam).
siblings(pitaji,fuwa).
siblings(fuwa,pitaji).
siblings(ram, fuwa).
siblings(fuwa,ram).
siblings(yuvi,navi).
siblings(navi,yuvi).

/* iii) Relations */
brotherOf(X,Y) :-  male(X),siblings(X,Y).
sisterOf(X,Y) :- female(X),siblings(X,Y).
grandParentOf(X,Y) :- parentOf(Z,X),parentOf(Y,Z).
auntOf(X,Y) :- sisterOf(X,Z),parentOf(Y,Z).
uncleOf(X,Y) :- brotherOf(Z,X),parentOf(Y,Z).

showFamily():- write("My Family members are: "),
		male(X), write(X), write(','),
		female(Y), write(Y), write(',').

showFamily1():- write("My family members are:"),
		Z=pitaji, male(X), write(X), write(','),X=Z,!,
		W=maa, female(Y), write(Y), write(','),Y=W,!. /* Use the showFamily1 to print out whole family*/



