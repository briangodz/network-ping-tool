import subprocess
import platform
import sys
from datetime import datetime

def ping(target, count=4):
    """
    Fungsi untuk melakukan ping ke target IP/domain.
    Mengembalikan hasil sebagai string dan statistik singkat.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), target]

    try:
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        result = output.stdout

        # Ambil ringkasan paket jika Linux/Mac
        summary = ""
        if platform.system().lower() != "windows":
            for line in result.splitlines():
                if "packet loss" in line or "rtt min/avg/max/mdev" in line:
                    summary += line + "\n"
        else:
            # Windows summary
            for line in result.splitlines():
                if "Packets:" in line or "Minimum" in line:
                    summary += line + "\n"

        return result, summary

    except subprocess.CalledProcessError as e:
        return "", f"Gagal melakukan ping ke {target}. Error:\n{e.stderr}"
    except Exception as e:
        return "", f"Terjadi error: {e}"

def main():
    print("=== Advanced Network Ping Tool ===\n")
    targets_input = input("Masukkan IP/domain (pisahkan dengan koma): ").strip()
    if not targets_input:
        print("Error: Target tidak boleh kosong!")
        sys.exit(1)

    targets = [t.strip() for t in targets_input.split(",")]
    count = input("Jumlah paket ping per host (default 4): ").strip()
    count = int(count) if count.isdigit() else 4

    # Buat file log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"ping_results_{timestamp}.txt"
    with open(log_file, "w") as f:
        f.write(f"=== Hasil Ping {timestamp} ===\n\n")
        for target in targets:
            print(f"\n>>> Pinging {target} ...")
            result, summary = ping(target, count)
            print(result)
            print(summary)
            f.write(f"Target: {target}\n")
            f.write(result + "\n")
            f.write(summary + "\n")
    print(f"\nSemua hasil telah disimpan di {log_file}")

if __name__ == "__main__":
    main()
