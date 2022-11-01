#  12  24  56
#  12  78  55
#  1   2   3

#  1   2   3           13  26  59
#  99  90  5           111 168  60
#  88  8   0           89   10  3

#deklarasi
A = [ [12,24,56], [12,78,55], [1,2,3] ]
B = [ [1,2,3], [99,90,5], [88,8,0]]
C = [ [0,0,0], [0,0,0], [0,0,0]]
#print(len(A),len(A[2]))
#print(A)
# C = A+B
#kalkulasi C
#perulangan baris#
for i in range(0,len(A)):
    #perulangan kolom
    for j in range(0,len(A[0])):
        C[i][j] = A[i][j] + B[i][j]
    
#cetak C
#perulangan baris#
for i in range(0,len(A)):
    #perulangan kolom
    for j in range(0,len(A[0])):
        print(C[i][j],end='\t')
    print("")