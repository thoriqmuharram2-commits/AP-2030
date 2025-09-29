#Program Hitung Bilangan Kuadrat
angka = int(input("masukkan sebuah bilangan: "))
if angka == 0:
        print(f"kuadrat dari {angka} adalah 1")
elif angka >= 0:
            print(f"kuadrat dari {angka} adalah {angka ** 2}")
else:
            print("Error : bilangan tidak boleh negatif!")
