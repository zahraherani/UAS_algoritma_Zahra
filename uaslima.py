nama = input ('masukan nama anda:')
print('Selamat datang,', nama, "diweb ini!")

umur = int(input("Masukkan umur Anda: "))

if umur >= 0 and umur <= 5:
    kategori = "Balita"
elif umur >= 6 and umur <= 12:
    kategori = "Anak_anak"
elif umur >= 13 and umur<= 17:
    kategori = "Remaja"
elif umur >= 18 and umur <= 59:
    kategori = "Dewasa"
elif umur >= 60:
    kategori = "Lansia"
else:
    kategori = "Umur tidak valid"
print(f"Berdasarkan umur Anda, Anda termasuk dalam kategori: {kategori}")
