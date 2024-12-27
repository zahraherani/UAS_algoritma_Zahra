def cetak_pola(baris):
    for i in range(1, baris + 1):
        print('*' * i)

print("Program Mencetak Pola Segitiga")
try:
    jumlah_baris = int(input("Masukkan jumlah baris untuk pola segitiga: "))
    if jumlah_baris > 0:
        print("\nPola segitiga:")
        cetak_pola(jumlah_baris)
    else:
        print("Error: Jumlah baris harus lebih dari 0.")
except ValueError:
    print("Error: Masukkan angka yang valid.")
