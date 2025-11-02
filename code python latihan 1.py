from random import random

while True:
    try:
        N = int(input("Masukkan nilai N: "))
        if N > 0:
            break
        else:
            print("Masukkan bilangan bulat positif.")
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")

print("---------------------------------")
print(f"Menampilkan {N} bilangan acak (< 0.5):")

for i in range(1, N + 1):
    
    bilangan_acak = random() * 0.5

    print(f"data ke: {i} ==> {bilangan_acak}")

print("Selesai")
