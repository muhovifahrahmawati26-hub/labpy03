# Praktikum3

## Latihan 1

Tujuan pemerograman:

1. Menampilkan n bilangan acak yang lebih kecil dari 0.5.
2. Nilai n dimasukkan pada saat runtime (eksekusi).
3. Menggunakan fungsi random() yang diimpor terlebih dahulu.
4. Menggunakan kombinasi while atau for.

## penjelasan code Python

1. from random import random: Ini mengimpor hanya fungsi random() dari modul random. Fungsi ini menghasilkan bilangan floating-point acak dalam rentang [0.0, 1.0).

2. Input  N  (while True...): Bagian ini meminta pengguna memasukkan nilai integer positif untuk  N . Loop while True dan blok try-except digunakan untuk memastikan input yang dimasukkan adalah bilangan bulat positif yang valid (error handling).

3. Loop for (for i in range(1, N + 1):): Loop ini memastikan bahwa proses pembuatan dan tampilan bilangan acak diulang tepat  N  kali. Variabel i digunakan untuk menghitung "data ke-" ke berapa.

4. Menghasilkan Bilangan Acak (bilangan_acak = random() * 0.5):Fungsi random() menghasilkan nilai antara  0.0  dan  1.0 .Mengalikan hasilnya dengan  0.5  akan membatasi rentang nilai acak menjadi  [0.0, 0.5) , sehingga memenuhi syarat soal yaitu "lebih kecil dari 0.5".

5. print(...): Baris ini menampilkan hasilnya sesuai format yang diminta di contoh keluaran pada gambar.
## Otput
<img width="1920" height="383" alt="hasil output 1" src="https://github.com/user-attachments/assets/49d8114b-ae20-4bc0-8e2d-6974f374e516" />

## Latihan 2
menghitung total keuntungan selama 8 bulan investasi
## Penjelasan Code
A. Struktur Perhitungan
- Program harus melakukan perhitungan secara berulang (iteratif) dari bulan 1 hingga bulan 8. Logika yang digunakan adalah:
    - $$\text{Laba Bulanan} = \text{Modal Awal} \times \text{Persentase Laba Bulan Terkait}$$
- Setiap laba bulanan kemudian diakumulasikan (dijumlahkan) untuk mendapatkan total laba.

B. Skema Persentase Laba
Persentase laba ditentukan oleh bulan keberapa perhitungan dilakukan:
1. Bulan ke-1 dan ke-2: Laba adalah 0%.
2. Bulan ke-3 dan ke-4: Laba adalah 1% dari modal awal.
3. Bulan ke-5, ke-6, dan ke-7: Laba adalah 5% dari modal awal.
4. Bulan ke-8: Laba adalah 3% dari modal awal (berdasarkan teks, laba bulan sebelumnya (5%) dikurangi 2%, menjadi 3%).

C. Kebutuhan Pemrograman
Untuk menyelesaikan latihan ini, program harus menggunakan dua elemen kontrol utama:
1. Loop (Perulangan): Digunakan untuk mengulang proses perhitungan laba dari bulan 1 hingga 8.
2. Kondisional: Digunakan untuk memeriksa nilai bulan (misalnya, if bulan == 1 atau elif bulan <= 4) untuk menerapkan persentase laba yang benar pada perhitungan.

D. Hasil Akhir yang Diharapkan
Output program harus menampilkan laba yang diperoleh untuk setiap bulan secara terpisah, dan diakhiri dengan tampilan total laba akumulasi setelah semua 8 bulan selesai dihitung.
  - Contoh Perhitungan Laba:
      - Laba Bulan 4 (1%): $100.000.000 \times 0.01 = \text{Rp } 1.000.000$
      - Laba Bulan 6 (5%): $100.000.000 \times 0.05 = \text{Rp } 5.000.000$
  - Catatan: Jika mengikuti semua persentase yang disebutkan (termasuk 3% di bulan 8), Total Laba seharusnya adalah Rp 20.000.000.
## Otput
<img width="1920" height="387" alt="hasil output 2" src="https://github.com/user-attachments/assets/72a22076-4ea4-4e9c-b86d-9f87e8999335" />

# Latihan 3
Tujuan pemerograman ini untuk membuat Simulasi Mesin ATM Sederhana (atau Simple ATM Machine Simulation)
## Penjelasan Code
1. Inisialisasi Saldo Awal
  Variabel saldo diatur ke nilai awal 1000000 (Rp 1.000.000) sesuai dengan instruksi.

2. Perulangan Utama (while True)
  Program menggunakan perulangan tak terbatas (while True) untuk menampilkan menu dan memproses transaksi secara berulang. Ini akan terus berjalan sampai secara eksplisit   dihentikan.

3. Tampilan Menu
  Di awal setiap perulangan, program memanggil fungsi tampilkan_menu() yang menampilkan saldo saat ini dan dua pilihan menu:

  - Tarik Uang

  - Keluar

4. Pemilihan Menu
  Pengguna diminta untuk memasukkan pilihan (1 atau 2).

5. Logika Pilihan (if/elif/else)

  - A. Jika Pilih '1' (Tarik Uang):
    - Input Jumlah: Pengguna diminta memasukkan jumlah uang yang ingin ditarik.

    - Validasi Input: Program mencoba mengonversi input menjadi angka bulat (int). Jika gagal (misalnya, pengguna mengetik huruf), akan ada pesan error.

    - Cek Saldo:

        - Jika jumlah_tarik lebih besar dari saldo, program menampilkan pesan "Saldo tidak mencukupi!".

        - Jika jumlah_tarik kurang dari atau sama dengan nol, program menampilkan pesan error.

    - Penarikan Berhasil:

       - Jika semua validasi lolos, saldo diperbarui dengan operasi pengurangan (saldo -= jumlah_tarik).

       - Program menampilkan pesan "Penarikan berhasil!".

    -  Program kembali ke awal perulangan untuk menampilkan menu yang diperbarui.

  - B. Jika Pilih '2' (Keluar):
    - Program menampilkan pesan "Terima kasih telah menggunakan ATM!".

    - Perintah break dijalankan, yang menghentikan perulangan while True dan mengakhiri program.

  - C. Pilihan Lain:
    - Jika pengguna memasukkan input selain 1 atau 2, program menampilkan pesan "Pilihan tidak valid..." dan kembali ke awal perulangan.

6. Penanganan Error
 - Kode menggunakan blok try...except untuk mengantisipasi kesalahan input yang mungkin terjadi, seperti pengguna memasukkan teks saat program mengharapkan angka (saat     penarikan uang), sehingga program tidak langsung crash.
## Otput
<img width="1920" height="550" alt="hasil output 3" src="https://github.com/user-attachments/assets/3b2a1465-fc6d-4402-8fa8-56d075431583" />
