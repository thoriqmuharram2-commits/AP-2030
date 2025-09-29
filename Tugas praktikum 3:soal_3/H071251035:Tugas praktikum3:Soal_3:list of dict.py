
buku1 = {"id": 1, "judul": "Belajar Python", "stok": 10, "harga": 85000}
buku2 = {"id": 2, "judul": "Algoritma Dasar", "stok": 3, "harga": 120000}
buku3 = {"id": 3, "judul": "Struktur Data", "stok": 2, "harga": 95000}

print("=== Menu Inventori Buku ===")
print("1. Tampilkan semua buku")
print("2. Tambah buku baru")
print("3. Ubah stok buku")
print("4. Buku dengan stok < 5")
print("5. Hitung total nilai inventori")

menu = int(input("Pilih menu: "))

# ini untuk menampilkan semua buku
if menu == 1:
    print(buku1)
    print(buku2)
    print(buku3)

# ini untuk menambah buku baru
elif menu == 2:
    judul_baru = input("Masukkan judul buku: ")
    stok_baru = int(input("Masukkan stok: "))
    harga_baru = int(input("Masukkan harga: "))
    buku4 = {"id": 4, "judul": judul_baru, "stok": stok_baru, "harga": harga_baru}
    print("Data buku baru ditambahkan:", buku4)

#ini untuk mengubah stok buku
elif menu == 3:
    id_edit = int(input("Masukkan ID buku yang stoknya ingin diubah: "))
    stok_baru = int(input("Masukkan stok baru: "))
    if id_edit == 1:
        buku1["stok"] = stok_baru
        print("Stok diperbarui:", buku1)
    elif id_edit == 2:
        buku2["stok"] = stok_baru
        print("Stok diperbarui:", buku2)
    elif id_edit == 3:
        buku3["stok"] = stok_baru
        print("Stok diperbarui:", buku3)
    else:
        print("ID tidak ditemukan!")

# ini untuk menampilkan buku dengan stok < 5
elif menu == 4:
    if buku1["stok"] < 5:
        print(buku1)
    if buku2["stok"] < 5:
        print(buku2)
    if buku3["stok"] < 5:
        print(buku3)

# untuk menghitung total inventori
elif menu == 5:
    total = (buku1["stok"] * buku1["harga"] +
             buku2["stok"] * buku2["harga"] +
             buku3["stok"] * buku3["harga"])
    print("Total nilai inventori:", total)

else:
    print("Menu tidak valid!")