#delarasi
kalimat = input("Masukkan kalimat/kata\t: ")
ikalimat=""
#buat inverse kalimat
for i in range(len(kalimat)-1,-1,-1) :
    ikalimat += kalimat[i]

#bandingkan kalimat dengan inversenya sama atau tidak,
# jika sama palindrom jika tidak bukan palindrom 
if(kalimat==ikalimat):
    print("Palindrom")
else :
    print("Bukan Palindrom")