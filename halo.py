# halo.py - program Python dengan tambahan colorama
from colorama import init, Fore, Style

# Inisialisasi colorama (agar berfungsi dengan baik di Windows)
init(autoreset=True)

# Sapaan utama
nama = input(Fore.CYAN + "Masukkan nama Anda: " + Style.RESET_ALL)
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")
print(Fore.YELLOW + "Semoga Anda menikmati belajar Python!")

# Input umur
umur = int(input(Fore.CYAN + "Masukkan umur Anda: " + Style.RESET_ALL))
print(Fore.MAGENTA + f"Tahun depan umur Anda {umur + 1} tahun.")

# Fitur hobi
hobi = input(Fore.CYAN + "Masukkan hobi Anda: " + Style.RESET_ALL)
print(Fore.GREEN + f"Wah, keren sekali! Hobi Anda adalah {hobi}.")
print(Fore.BLUE + Style.BRIGHT + "\nTerima kasih telah menjalankan program ini!")