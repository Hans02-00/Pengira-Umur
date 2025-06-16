from datetime import date

# Minta input tahun lahir pengguna
tahun_lahir = int(input("Masukkan tahun lahir anda: "))

# Dapatkan tahun semasa
tahun_sekarang = date.today().year

# Kira umur
umur = tahun_sekarang - tahun_lahir

# Papar keputusan
print(f"Umur anda sekarang ialah: {umur} tahun")

# BY-Hanisah
