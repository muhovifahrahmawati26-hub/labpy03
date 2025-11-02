# Praktikum3

## Latihan 1

Tujuan pemerograman:

1. Menampilkan n bilangan acak yang lebih kecil dari 0.5.
2. Nilai n dimasukkan pada saat runtime (eksekusi).
3. Menggunakan fungsi random() yang diimpor terlebih dahulu.
4. Menggunakan kombinasi while atau for.

## penjelasan code Python

```python
1. from random import random: Ini mengimpor hanya fungsi random() dari modul random. Fungsi ini menghasilkan bilangan floating-point acak dalam rentang [0.0, 1.0).

2. Input  N  (while True...): Bagian ini meminta pengguna memasukkan nilai integer positif untuk  N . Loop while True dan blok try-except digunakan untuk memastikan input yang dimasukkan adalah bilangan bulat positif yang valid (error handling).

3. Loop for (for i in range(1, N + 1):): Loop ini memastikan bahwa proses pembuatan dan tampilan bilangan acak diulang tepat  N  kali. Variabel i digunakan untuk menghitung "data ke-" ke berapa.

4. Menghasilkan Bilangan Acak (bilangan_acak = random() * 0.5):Fungsi random() menghasilkan nilai antara  0.0  dan  1.0 .Mengalikan hasilnya dengan  0.5  akan membatasi rentang nilai acak menjadi  [0.0, 0.5) , sehingga memenuhi syarat soal yaitu "lebih kecil dari 0.5".

5. print(...): Baris ini menampilkan hasilnya sesuai format yang diminta di contoh keluaran pada gambar.
```
## Otput
<img width="1920" height="383" alt="hasil output 1" src="https://github.com/user-attachments/assets/49d8114b-ae20-4bc0-8e2d-6974f374e516" />
