#deklarasi
A = [1,5,3,7]
i = 0
cari = 10
ketemu = False

for i in range(0,len(A)) :
    if( A[i]==cari ):
        ketemu = True
        print(cari, " ketemu pada indeks ke",i)
        break
    else :
        i+=1
#jika tidak ketemu
if(not ketemu) :
    print(cari, " tidak ditemukan pada ",A)