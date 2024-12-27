def hitung_gaji(tarif_per_jam_kerja, hari_kerja):
   
    total_gaji = 0  

    for hari in range(1, hari_kerja + 1):
        jam_kerja = float(input(f"Masukkan jam kerja untuk hari ke-{hari}: "))
        if jam_kerja <= 8:
            gaji_harian = jam_kerja * tarif_per_jam_kerja
        else:
            jam_lembur = jam_kerja + 8
            gaji_harian = (8 * tarif_per_jam_kerja) + (jam_lembur * tarif_per_jam_kerja * 1.5)

        total_gaji += gaji_harian

    return total_gaji

print("Program Penghitungan Gaji Bulanan Karyawan")

try:
    
    tarif_per_jam_kerja = float(input("Masukkan tarif gaji per jam (Rp): "))
    hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

    if tarif_per_jam_kerja < 0 or hari_kerja < 0:
        print("Error: Tarif gaji per jam dan jumlah hari kerja harus bernilai positif.")
    else:
        gaji_total = hitung_gaji(tarif_per_jam_kerja, hari_kerja)
        print(f"\nGaji total bulanan karyawan adalah: Rp {gaji_total:,.2f}")
except ValueError:
    print("Error: Masukkan angka yang valid.")

