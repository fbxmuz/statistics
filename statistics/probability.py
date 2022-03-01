"""
 Chapter 3 - Inferential Statistics

"""
def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n-1)



def permutation(n,k):
    """
    nPk

    :param n: the size of the set
    :param k: the number drawn
    :return: the number of permutations ( order does not matters )
    """
    if n > k:
        return  int(factorial(n) / factorial(n - k))
    else:
        raise ValueError("n may not be less than k")



def combination(n,k):
    """
    nCk

    :param n: the size of the set
    :param k: the number drawn
    :return: the number of combinations ( order matters )
    """
    if n > k:
        return int(permutation(n,k) / factorial(k))
    else:
        raise ValueError("n may not be less than k")

print(permutation(n=8,k=2))

print(combination(n=8, k=2))

"""
The probability of a single event, E, is 0 <= P(E) <= 1
The sample space S are all the possible outcomes of a trial
   is P(S) == 1
   
P(E) and it's complement P(~E),  P(E) + P(~E) == 1
A corollary, P(~E) == 1 - P(E)
"""

def complement(PE):
    if PE >= 0 and PE <= 1:
        return 1 - PE
    else:
        return ValueError("0 <= P(E) <= 1")

def excusive_union(PE, PF) :
    """P (E ∪ F) = P(E) + P(F)"""
    if PE + PF >=0 and PE +PF <= 1:
        return PE + PF
    else:
        raise ValueError("0 <= P(E) + P(F) <= 1")


def non_exclusive_union(PE, PF):
    """P(E ∪ F) = P(E) + P(F) − P(E ∩ F)"""
    if PE + PF >= 0 and PE + PF <= 1:
        return PE + PF - excusive_union(PE, PF)
    else:
        raise ValueError("0 <= P(E) + P(F) <= 1")

# intersection