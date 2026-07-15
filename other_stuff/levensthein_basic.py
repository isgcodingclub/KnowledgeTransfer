# install with pip install python-Levenshtein
from Levenshtein import distance

s = "cat"
s1 = "rat"

distance = distance(s, s1, weights=(1, 1, 1))
print(distance)
