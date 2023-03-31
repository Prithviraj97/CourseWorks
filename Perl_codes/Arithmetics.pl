factorial(0,X):- X=1.
factorial(Z,X):- Z1 is Z-1,
    factorial(Z1,X1),
    X is X1* Z.
factorial(Z):-
    factorial(Z,X),
    write(X),!.

guess(Y):- Y= 9 ->write("Correct!"); /* Use guess(number). to print whether thee guessed number is right.*/
Y > 9 -> write("Higher!");
write("Low!").
