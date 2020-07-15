def jumlah (a,b):
  n = a+b
  return n
def kurang (a,b):
  n = a-b
  return n
def kali (a,b):
  n = a*b
  return n
def bagi (a,b):
  n = a//b
  return n
def validate(tetot):
  if (tetot < 0) or (tetot > 3):
    print("Invalid number")
  return True
menu = ["jumlah",
        "kurang",
        "kali",
        "bagi"]
index = 0
for geng in menu:
  print(str(index)+" "+menu[index])
  index += 1
menu = int(input("Masukkan menu :"))
validate(menu)

if menu == 0:
  angka1 = int (input("Masukkan angka ke-1 :"))
  angka2 = int (input("Masukkan angka ke-2 :"))
  abc = jumlah(angka1,angka2)
  print("Hasilnya "+str(abc))
elif menu == 1:
  angka1 = int (input("Masukkan angka ke-1 :"))
  angka2 = int (input("Masukkan angka ke-2 :"))
  abc =kurang(angka1,angka2) 
  print("Hasilnya "+str(abc))
elif menu == 2:
  angka1 = int (input("Masukkan angka ke-1 :"))
  angka2 = int (input("Masukkan angka ke-2 :"))
  abc =kali(angka1,angka2) 
  print("Hasilnya "+str(abc))
elif menu == 3:
  angka1 = int (input("Masukkan angka ke-1 :"))
  angka2 = int (input("Masukkan angka ke-2 :"))
  abc =bagi(angka1,angka2) 
  print("Hasilnya "+str(abc))
