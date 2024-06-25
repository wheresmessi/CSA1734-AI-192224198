if(bird, flies).
if(mammal, walks).
if(wings, bird).
if(fur, mammal).
if(penguin, wings).
if(bat, fur).

% Forward Chaining
fc(Fact) :-
    assertz(known(Fact)),
    forward_chain(Fact).

forward_chain(Fact) :-
    if(Fact, Conclusion),
    \+ known(Conclusion),  % Ensure we only assert new conclusions
    assertz(known(Conclusion)),
    forward_chain(Conclusion).
forward_chain(_).
