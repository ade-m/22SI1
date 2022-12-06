
def tampilkanangka(batas,i=1) :
    if(i<=batas):
        print("Angka i =",i)
        tampilkanangka(batas,i+1)

tampilkanangka(10,5)