saldo = 1000000

def tampilkan_menu(current_saldo):
    print("\n" + "="*30)
    print(f"Saldo saat ini: Rp {current_saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    print("="*30)

while True:
    tampilkan_menu(saldo)

    try:
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == '1':
            jumlah_tarik_str = input("Masukkan jumlah penarikan: ")
            
            try:
                jumlah_tarik = int(jumlah_tarik_str)
            except ValueError:
                print("❌ Input tidak valid. Harap masukkan angka.")
                continue # Lanjut ke iterasi berikutnya
                
            if jumlah_tarik > saldo:
                print("⚠️ Saldo tidak mencukupi!")
            elif jumlah_tarik <= 0:
                print("❌ Jumlah penarikan harus lebih dari nol.")
            else:
                saldo -= jumlah_tarik
                print("✅ Penarikan berhasil!")
                
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM!")
            break # Keluar dari perulangan
            
        else:
            print("❌ Pilihan tidak valid. Silakan pilih 1 atau 2.")
            
    except EOFError:
        print("\nProgram dihentikan.")
        break
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        break
