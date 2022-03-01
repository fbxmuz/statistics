def mean(l):
    return sum(l) / len(l)

def midrange(l):
    return (l[0] + l[-1]) / 2

def median(l):
    if len(l) % 2 == 1:
        return l[ int(len(l) /2)]
    else:
        return  (l[ int(len(l) /2) -1] + l[ int(len(l) /2)]) /2

