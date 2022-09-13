from math import log2
import numpy as np


W = ["Cloudy", "Sunny", "Rainy"]
D = [[1,1,2], [1,0,1], [1,2,0], [4,2,2], [0,1,0],[0,0,2], [1,1,1], [1,0,2], [0,1,2], [1,2,1]]

def get_boolean(D):
    B=[]
    for key, d in enumerate(D):
        B.append([(0 if a==0 else 1) for a in d])
    return np.array(B)

def get_tf(D):
    B=[]
    for key, d in enumerate(D):
        B.append([(0 if a==0 else 1+log2(a)) for a in d])
    return np.array(B)

def get_idf(D):
    return np.array([0 if sum(x)==0 else log2(len(D)/sum(x)) for x in zip(*get_boolean(D))])

def get_tf_idf(D):
    return get_tf(D)*get_idf(D)

def print_matrix(W, D):
    W_maxlen = max(map(len, W))
    W=['{{:{}}}'.format(W_maxlen).format(row) for row in W]  
    print("\n" + " "*(W_maxlen+2) + " ".join(str("d" + str(j)) for j in range(10)))
    for i in range(len(W)):
        print(str(W[i]) + ":  " + "  ".join(str(D[j][i]) for j in range(10)))

print(np.array(D))
print(get_tf(D))
print(get_idf(D))
print(get_tf_idf(D))



