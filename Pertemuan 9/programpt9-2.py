Angka = [12,5,7,10,11,5]
print(Angka)
print("Count 5 :", Angka.count(5))
print("Panjang Array : ",len(Angka))
Angka.remove(5)
print("remove 5 :",Angka)
Angka.pop()
print("Pop : ",Angka)
bilGenap = [2,4,6,8,10]
Angka.extend(bilGenap)
print("Extend  dengan bilGenap: ",Angka)
Angka.append(999)
print("Append : ",Angka)
Angka[3]= 777
print("Insert : ",Angka)
Angka.sort()
print(Angka)
Angka.reverse()
print(Angka)


