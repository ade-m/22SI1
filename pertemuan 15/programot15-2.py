def ffaktorial(i):
    if i>=1 :
        return i*ffaktorial(i-1)
    else:
        return 1

N=10
faktorial = 1
for i in range(N,0,-1):
    faktorial *= i

print(faktorial)

print(ffaktorial(N))