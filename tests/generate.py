#!/usr/bin/env python3
import os, random; random.seed(46)
def w(name, n, m, arr):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(f"{n} {m}\\n" + " ".join(map(str,arr))+"\\n")
    T=[0]*(n*m)
    for i in range(n):
        for j in range(m):
            T[j*n + i] = arr[i*m + j]
    with open(f"tests/output_{name}.txt","w") as f:
        for i in range(m):
            f.write(" ".join(map(str,T[i*n:(i+1)*n]))+"\\n")
def main():
    w("min",1,1,[7])
    n,m=1000,1000; arr=list(range(1,n*m+1)); w("max",n,m,arr)
    n,m=7,11; arr=[random.randint(-50,50) for _ in range(n*m)]; w("rnd",n,m,arr)
if __name__=="__main__": main()
