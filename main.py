import os
import time

def salam():
    os.system('clear')
    print("=====================================")
    print("     PROJECT QUANTUM AULUNG V7       ")
    print("=====================================")
    print(" Status: Berhasil Sinkron ke GitHub! ")
    print(" User  : dadanrukanda89-lab          ")
    print("=====================================")
    
    nama = input("\nMasukkan nama lo, Bro: ")
    print(f"\n[+] Halo {nama}, kodingan lo siap beraksi!")
    time.sleep(2)

if __name__ == "__main__":
    salam()

