"""
 Chapter 2 - Probability

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



"""
The probability of a single event, E, is 0 <= P(E) <= 1
The sample space S are all the possible outcomes of a trial
   is P(S) == 1
   
P(E) and it's complement P(~E),  P(E) + P(~E) == 1
A corollary, P(~E) == 1 - P(E)
"""
def isAProbability(n):
    return n >= 0 and n <= 1

def complement(PE):
    if isAProbability(PE):
        return 1 - PE
    else:
        return ValueError("0 <= P(E) <= 1")

def excusive_union(PE, PF) :
    # pf. 32
    """P (E ∪ F) = P(E) + P(F)"""
    if isAProbability(PE + PF):
        return PE + PF
    else:
        raise ValueError("0 <= P(E) + P(F) <= 1")


def non_exclusive_union(PE, PF):
    """P(E ∪ F) = P(E) + P(F) − P(E ∩ F)"""
    if isAProbability(PE + PF):
        return PE + PF - excusive_union(PE, PF)
    else:
        raise ValueError("0 <= P(E) + P(F) <= 1")

def intersection_independent(PE, PF):
    if isAProbability(PE) and isAProbability(PF):
        return PE * PF
    else:
        raise ValueError("PE and PF must be between 0 and 1")

def intersection(PE, PF):
    if isAProbability(PE) and isAProbability(PF):
        return PE * PF
    else:
        raise ValueError("PE and PF must be between 0 and 1")

def draw(number_of_matches, number_of_cards):
    return number_of_matches/number_of_cards
# draw clubs from a card deck
clubs = draw(26,52)
print(clubs)
# draw clubs twice
clubs_twice = draw(25,51)

print(intersection(clubs, clubs_twice))

