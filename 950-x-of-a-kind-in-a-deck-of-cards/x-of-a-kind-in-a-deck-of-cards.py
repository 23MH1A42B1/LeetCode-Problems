from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        count = Counter(deck)
        return reduce(gcd, count.values()) >= 2
