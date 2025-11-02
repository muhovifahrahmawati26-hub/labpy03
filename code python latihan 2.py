MODAL_AWAL = 100_000_000.0  # 100 Juta
total_laba = 0.0

for bulan in range(1, 9):
    if bulan <= 2:
        # Bulan 1 dan 2: Laba 0%
        persentase_laba = 0.0
    elif bulan <= 4:
        # Bulan 3 dan 4: Laba 1%
        persentase_laba = 0.01  # 1%
    elif bulan <= 7:
        # Bulan 5, 6, dan 7: Laba meningkat 5%
        persentase_laba = 0.05  # 5%
    else:  # bulan == 8
        # Bulan 8: Penurunan 2% (sehingga laba menjadi 3%)
        persentase_laba = 0.03  # 3%

    laba_bulan_ini = MODAL_AWAL * persentase_laba

    total_laba += laba_bulan_ini

    print(f"laba bulan ke- {bulan} sebesar: {laba_bulan_ini}")

print(f"Total laba adalah: {total_laba}")