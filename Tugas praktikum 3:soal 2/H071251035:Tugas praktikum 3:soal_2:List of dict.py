data = [
    {"nama": "Alya", "nilai": 88},
    {"nama": "Budi", "nilai": 67},
    {"nama": "Citra", "nilai": 74}
]

# Alya 
if data[0]["nilai"] >= 70:
    status0 = "Lulus"
else:
    status0 = "Gagal"

if data[0]["nilai"] >= 85:
    kategori0 = "A"
elif data[0]["nilai"] >= 70:
    kategori0 = "B"
elif data[0]["nilai"] >= 50:
    kategori0 = "C"
else:
    kategori0 = "D"

# Budi
if data[1]["nilai"] >= 70:
    status1 = "Lulus"
else:
    status1 = "Gagal"

if data[1]["nilai"] >= 85:
    kategori1 = "A"
elif data[1]["nilai"] >= 70:
    kategori1 = "B"
elif data[1]["nilai"] >= 50:
    kategori1 = "C"
else:
    kategori1 = "D"

# Citra
if data[2]["nilai"] >= 70:
    status2 = "Lulus"
else:
    status2 = "Gagal"

if data[2]["nilai"] >= 85:
    kategori2 = "A"
elif data[2]["nilai"] >= 70:
    kategori2 = "B"
elif data[2]["nilai"] >= 50:
    kategori2 = "C"
else:
    kategori2 = "D"


jumlah = data[0]["nilai"] + data[1]["nilai"] + data[2]["nilai"]
rata = jumlah / 3
rata_dua_angka = int(rata * 100) / 100   


tinggi = data[0]
rendah = data[0]

if data[1]["nilai"] > tinggi["nilai"]:
    tinggi = data[1]
if data[2]["nilai"] > tinggi["nilai"]:
    tinggi = data[2]

if data[1]["nilai"] < rendah["nilai"]:
    rendah = data[1]
if data[2]["nilai"] < rendah["nilai"]:
    rendah = data[2]


print(f"{data[0]['nama']} : {data[0]['nilai']} -> {status0} ({kategori0})")
print(f"{data[1]['nama']} : {data[1]['nilai']} -> {status1} ({kategori1})")
print(f"{data[2]['nama']} : {data[2]['nilai']} -> {status2} ({kategori2})")
print("Rata-rata kelas:", rata_dua_angka)
print("Nilai tertinggi:", tinggi["nilai"], f"({tinggi['nama']})")
print("Nilai terendah:", rendah["nilai"], f"({rendah['nama']})")