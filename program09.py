nama = input("Masukkan Nama 		: ")
nim = int(input("Masukka NIM 		: "))
a = int(input("Masukkan Bilangan A 	: "))
b = int(input("Masukkan Bilangan B 	: "))
c = int(input("Masukkan Bilangan C 	: "))

angka = [a, b, c]
hasil= max(angka)

print(" ")
print("--------------------------------------")
print(" ")

if a>b and a>c:
	huruf = "A"
elif b>c and b>a:
	huruf = "B"
elif c>a and c>b:
	huruf = "C"
else:
	huruf = "A,B,C"

print("\nNama 					: ",nama)
print("nim 					: ",nim)
print("Bilangan Terbesar Adalah 		: ",huruf)
print("Dengan Nilai 				:",hasil)