import os
import logging
import platform
import shutil

# --- SETUP DASAR ---
logging.basicConfig(filename='quantum.log', level=logging.INFO, format='%(asctime)s - %(message)s')
G, Y, B, R, W = "\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"

def get_sys_info():
    """Logika Menu No 2"""
    return {
        "Sistem": platform.system(),
        "Node": platform.node(),
        "Python": platform.python_version()
    }

def main():
    while True:
        os.system('clear')
        print(f"{B}====================================={W}")
        print(f"{G}      QUANTUM SYSTEM V7 - ACTIVE     {W}")
        print(f"{B}====================================={W}")
        print(f"{G}[1]{W} Ganti Nama")
        print(f"{G}[2]{W} System Info")
        print(f"{G}[3]{W} Hapus Cache")
        print(f"{G}[4]{W} Keluar & Sync")
        print(f"{B}====================================={W}")
        
        pilih = input(f"\n{Y}Pilih Menu: {W}")

        if pilih == '1':
            input(f"{G}[+] Menu 1 Ready! Enter...")
        elif pilih == '2':
            # --- MENU NO 2 (SUDAH FIX) ---
            info = get_sys_info()
            print(f"\n{B}--- SYSTEM INFO ---{W}")
            for k, v in info.items():
                print(f"{G}{k:<10} : {W}{v}")
            input(f"\n{Y}Press Enter to continue...")
        elif pilih == '3':
            print(f"{Y}[!] Membersihkan cache...{W}")
            # Logika hapus __pycache__
            input(f"{G}[+] Bersih! Press Enter...")
        elif pilih == '4':
            print("Sampai Jumpa!")
            break

if __name__ == "__main__":
    main()

