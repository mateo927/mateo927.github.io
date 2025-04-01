
def C(i: int, j: int) -> int:
    if j>i:
        return 0
    elif i==j or j==0:
        return 1
    else:
        return C(i-1,j-1)+C(i-1,j)


def pascal(n: int) -> list[list[int]]:
    return [[C(i,j) for j in range(i+1)] for i in range(n)]


def  P(n: int) -> int:
    resltat=1
    for i in range(n+1):
        resltat= resltat*C(n,i)
    return resltat


def Q(n: int) -> float:
     return P(n-1)*P(n+1)/P(n)**2
