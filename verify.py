"""Exact period and coefficient certificate for A247729."""
from fractions import Fraction as F
from itertools import combinations,product
from math import lcm
import numpy as np

PATTERNS=((1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
FORMS=[(0,)*i + p + (0,)*(2-i) for i in range(3) for p in PATTERNS]

def solve(rows,rhs):
    n=len(rows)
    a=[[F(x) for x in row]+[F(b)] for row,b in zip(rows,rhs)]
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None:
            return None
        a[k],a[j]=a[j],a[k]
        a[j]=[x/a[j][j] for x in a[j]]
        for k in range(n):
            if k!=j and a[k][j]:
                c=a[k][j]
                a[k]=[x-c*y for x,y in zip(a[k],a[j])]
    return tuple(row[-1] for row in a)

def period():
    den=set()
    verts=set()
    for d in range(6):
        for h in combinations(FORMS,d):
            for free in combinations(range(6),d):
                fixed=tuple(i for i in range(6) if i not in free)
                A=[[e[i] for i in free] for e in h]
                for tail in product((0,1),repeat=len(fixed)-1):
                    vals=(0,)+tail  # All equations are invariant under cube reflection.
                    B=[-sum(e[i]*x for i,x in zip(fixed,vals)) for e in h]
                    p=solve(A,B)
                    if p is not None and all(0<=x<=1 for x in p):
                        den.update(x.denominator for x in p)
                        v=[F(0)]*6
                        for i,x in zip(fixed,vals):
                            v[i]=F(x)
                        for i,x in zip(free,p):
                            v[i]=x
                        verts.add(tuple(v))
                        verts.add(tuple(1-x for x in v))
    return sorted(den),lcm(*den),len(verts)

def count(n):
    # int64 is exact here, since counts never exceed (83+1)^6 < 2^40.
    i,j,k=np.ogrid[:n+1,:n+1,:n+1]
    a=np.ones((n+1,)*3,dtype=np.int64)
    exceptions=(i+j-k,i+k-j,j+k-i)
    for _ in range(3):
        b=np.broadcast_to(a.sum(axis=0)[:,:,None],a.shape).copy()
        for index,x in enumerate(exceptions):
            mask=(0<=x)&(x<=n)
            for earlier in exceptions[:index]:
                mask &= (x != earlier)
            b-=np.where(mask,a[np.clip(x,0,n),i,j],0)
        a=b
    return int(a.sum())

def quasi(n):
    c=(-90,207,-42,207,-90,255,-90,207,-42,207,-90,255)
    d=(0,-223,-140,-351,128,-599,108,-223,-248,-351,236,-599)
    j=n%12
    num=54*n**6+387*n**4-203*n**3+(210 if j%2 else 372)*n*n+c[j]*n+d[j]
    assert num%54==0
    return num//54

def gf_coefficients(limit):
    # R. J. Mathar's proposed rational form, OEIS A247729.
    num=[0]+[4*x for x in (2,39,224,786,1816,3236,4421,4943,4379,3196,1787,795,235,61)]
    den=[1]
    for f in [(1,0,1)]+[(1,1,1)]*2+[(1,1)]*3+[(1,-1)]*7:
        new=[0]*(len(den)+len(f)-1)
        for i,a in enumerate(den):
            for j,b in enumerate(f):
                new[i+j]+=a*b
        den=new
    assert den==[1,-2,-1,2,2,2,-5,-2,0,2,5,-2,-2,-2,1,2,-1]
    out=[]
    for n in range(limit+1):
        out.append((num[n] if n<len(num) else 0) -
                   sum(den[j]*out[n-j] for j in range(1,min(n+1,len(den)))))
    return out

if __name__=="__main__":
    bound=period()
    assert bound==([1,2,3,4],12,160),bound
    want=gf_coefficients(83)
    for n,v in enumerate(want):
        actual=count(n)
        assert actual==quasi(n)==v,(n,actual,v)
    print("A247729: 160 cube-arrangement vertices; period bound 12; 84 exact matches.")
