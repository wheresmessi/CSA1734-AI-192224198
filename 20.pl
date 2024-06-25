parent(john,mary).
parent(john,tom).
parent(mary,anna).
parent(tom,james).

grandparent(X,Y):- parent(X,Z),parent(Z,Y).
sibling(X,Y):- parent(Z,X),parent(Z,Y),X\=Y.
