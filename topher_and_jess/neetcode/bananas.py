"""

"""

from math import ceil
import math
def minEatingSpe(piles, h):
    res = max(piles)
    l,r = 1,max(piles)
    while l < r:
        m = (l + r) // 2
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas /m)

        if hours <= h:
            res = min(res,m)
            r = m -1
        else:
            l = m +1

    return res

print(minEatingSpe(piles = [1,4,3,2], h = 9))