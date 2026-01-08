soyulacak_patates = 10
patates_cuvali = soyulacak_patates
soyulan_patates = 0

print("Patates soyma işlemine başlandı.")

while soyulan_patates < soyulacak_patates:
    soyulan_patates += 1
    patates_cuvali -= 1
    print(f"{soyulan_patates} patates soyuldu, {patates_cuvali} patates kaldı.")

print("--- BİTTİ: Tüm patatesler soyuldu! ---")