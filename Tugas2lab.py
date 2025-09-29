barang = ["Buku", "Pensil", "Pulpen"]
harga = [20000, 3000, 5000]
jumlah = [2, 5, 3]

total_barang = jumlah[0] + jumlah[1] + jumlah[2]

total_buku = harga[0] * jumlah[0]
total_pensil = harga[1] * jumlah[1]
total_pulpen = harga[2] * jumlah[2]

total_harga = [total_buku, total_pensil, total_pulpen]

total_belanja = (total_buku + total_pensil + total_pulpen)

hasil = {
    "Buku": total_buku,
    "Pensil": total_pensil,
    "Pulpen": total_pulpen,
    "Total Belanja": total_belanja
}

print(hasil)

print("Buku lebih mahal dari Pulpen:", total_buku > total_pulpen)
print("Total belanja > 50000:", total_belanja > 50000)
print("Jumlah semua barang > 5:", total_barang > 5)