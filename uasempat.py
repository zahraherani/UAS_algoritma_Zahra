
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def bagi(a, b):
    if b == 0:
        return a / b

def kali(a, b):
    return a * b


print("Pilih operasi matematika:")
print("1. Tambah")
print("2. Kurang")
print("3. Bagi")
print("4. Kali")


pilihan = input("Masukkan nomor operasi (1/2/3/4): ")


if pilihan in ['1', '2', '3', '4']:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    
    if pilihan == '1':
        print(f"Hasil: {tambah(angka1, angka2)}")
    elif pilihan == '2':
        print(f"Hasil: {kurang(angka1, angka2)}")
    elif pilihan == '3':
        print(f"Hasil: {bagi(angka1, angka2)}")
    elif pilihan == '4':
        print(f"Hasil: {kali(angka1, angka2)}")
else:
    print("Pilihan tidak valid. Silakan coba lagi.")




