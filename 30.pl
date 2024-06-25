flies(eagle).
flies(sparrow).

lays_eggs(eagle).
lays_eggs(sparrow).
lays_eggs(penguin).
bird(X) :- flies(X), lays_eggs(X).






