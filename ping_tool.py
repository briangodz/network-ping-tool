import os
import platform

def ping(host):
    # Tentukan perintah sesuai sistem operasi
    param = "-n" if platform.system().lower()=="windows" else "-c"
    command = ["ping", param, "4", host]
    return os.system(" ".join(command))

if __name__ == "__main__":
    target = input("Masukkan alamat IP atau domain: ")
    print(f"\nMelakukan ping ke {target}...\n")
    ping(target)
