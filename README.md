# projecteuler
problems from projecteuler
test

# quick sort algorithm implement in python

def qsort(L):
    if L: return qsort([x for x in L if x<L[0]]) + [x for x in L if x==L[0]] + qsort([x for x in L if x>L[0]])
    return []
