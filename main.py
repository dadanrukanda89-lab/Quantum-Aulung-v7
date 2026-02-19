import os
from modules.database import inisialisasi_db, simpan_master, ambil_master
from modules.engine import get_sys_info

def main():
    while True:
        os.system('clear')
        inisialisasi_db()
        master_saat_ini = ambil_master()
        
        # Variabel Warna
        G, B, Y, R = "\033[92m", "\033[94m", "\033[93m", "\033[0m"
        
        print(f"{B}====================================={R}")
        print(f"{G}   WELCOME BACK, {Y}[{master_saat_ini.upper()}]{R}   ")
        print(f"{B}====================================={R}")
        print(f"{G}[1]{R} Ganti Nama Master")
        print(f"{G}[2]{R} Quantum System Info")
        print(f"{G}[3]{R} Keluar & Auto-Sync GitHub")
        print(f"{B}====================================={R}")
        
        pilih = input(f"\n{Y}Pilih Menu:{R} ")
        
        if pilih == '1':
            nama_baru = input(f"{G}Masukkan Nama Baru:{R} ")
            simpan_master(nama_baru)
            print(f"{G}[+] Nama Master berhasil diupdate!{R}")
            input("Tekan Enter untuk kembali...")
        elif pilih == '2':
            info = get_sys_info()
            print(f"\n{B}--- SYSTEM INFO ---{R}")
            print(f"{G}Model Arsitektur:{R} {info['model']}")
            print(f"{G}Sisa Penyimpanan:{R} {info['storage']}")
            input(f"\n{Y}Tekan Enter untuk kembali...{R}")
        elif pilih == '3':
            print(f"{Y}\n[!] Sedang sinkronisasi data ke GitHub...{R}")
            # Perintah otomatisasi Git
            os.system("git add . && git commit -m 'Auto-sync: Quantum System Updated' && git push origin main")
            print(f"{G}[+] Semua data aman di GitHub. Bye!{R}")
            break
        else:
            print("\033[91m[!] Pilihan salah! \033[0m")
            import time
            time.sleep(1)

if __name__ == "__main__":
    main()

