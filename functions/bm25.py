from math import log2
from re import L

W = ["Cloudy", "Sunny", "Rainy"]
D = [[1,1,2], [1,0,1], [1,2,0], [4,2,2], [0,1,0],[0,0,2], [1,1,1], [1,0,2], [0,1,2], [1,2,1]]

def get_Lave(D, N):
    c=0
    for d in D:
        c+=sum(d)
    return c/N

k=1
b=0.75

def BM25(k, b, D, Q):
    N=len(D)
    Lave=get_Lave(D, N)
    bm25=[0] * N

    for q in Q:
        dft=0
        for d in D:
            dft+=0 if d[q]==0 else 1
        for key, d in enumerate(D):
            Ld=sum(d)
            tftd=d[q]
            bm25[key]+=log2(N/dft)*(k+1)*tftd/(k*((1-b)+b*(Ld/Lave))+tftd)
    return bm25

def make_ordered_list(bm25):
    d={}
    for key, value in enumerate(bm25):
        d["d" + str(key+1)]=value
    return list({k: v for k, v in sorted(d.items(), key=lambda item: item[1])}.keys())

print("q1='Sunny Rainy'")
bm25=BM25(k,b, D, Q=[1,2])
print(bm25)
print(make_ordered_list(bm25))

print("\n\n\nq2='Cloudy'")
bm25=BM25(k,b, D, Q=[0])
print(bm25)
print(make_ordered_list(bm25))
