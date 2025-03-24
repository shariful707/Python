def Fibo(N):
    if N ==1:
        return 0
    elif N == 2:
        return 1
    return Fibo(N-1)+Fibo(N-2)

print(Fibo(21))