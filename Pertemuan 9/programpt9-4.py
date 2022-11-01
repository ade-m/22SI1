#deklarasi
N = int(input("Input Jumlah Deret (N) : "))
i=1
j=1
deretBilanganPrima = [1]

#program
#percabangan
while i<N :
    #cek apakah bil prima
    if j==2:
        deretBilanganPrima.append(j)
        i+=1
    for x in range(2,j):   
        if j%x==0:
            break
        elif x==j-1:
            deretBilanganPrima.append(j)
            i+=1
    j+=1
if(N>0) :
    print(deretBilanganPrima)