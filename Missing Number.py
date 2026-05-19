from typing import *

def missingNumber(a : List[int], N : int) -> int:
    N=len(a)+1
    return N*(N+1)//2-sum(a)
