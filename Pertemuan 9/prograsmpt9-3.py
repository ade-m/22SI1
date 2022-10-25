#deklarasi
N = int(input("Input Jumlah Deret (N) : "))
i=0
j=1
deretBilanganGenap = [0 for i in range(N)]

#program
#percabangan
while i<N :
    #percabangan cek apakah bil genap
    if j%2==0:
        deretBilanganGenap[i]=j
        i+=1
    j+=1
print(deretBilanganGenap)