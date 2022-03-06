

# least squares method
x = [  1,  2,   3,   4,   5,    6,    7]
y = [ 1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16]

def listMuliply(list1, list2):
    return [ i * j  for  i,j in zip(list1, list2)  ]

def slope(x,y):
    sum_x = sum(x)
    sum_y = sum(y)
    xy = listMuliply(x,y)
    sum_xy = sum(xy)
    xx = listMuliply(x, x)
    sum_xx = sum(xx)
    n = len(x)
    return (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)

def x_intercept(slope, x,y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    return (sum_y - slope * sum_x) / n


def mean(x):
    return sum(x)/ len(x)




m = round(slope(x,y),7)
b = round(x_intercept(m, x,y),7)

print(f"y = {m}x + {b}")
