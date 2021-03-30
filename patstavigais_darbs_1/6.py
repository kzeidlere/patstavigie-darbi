dalderi = int(input("Dālderi: "))
grasi = int(input("Graši: "))
santimi = int(input("Santīmi: "))

grasi += dalderi * 37
santimi += grasi * 162

new_dalderi = santimi // 100
new_santimi = santimi % 100

print("Jaunie dālderi:", new_dalderi)
print("Jaunie santīmi:", new_santimi)

print('Izmaiņas')
