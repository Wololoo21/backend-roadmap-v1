import sqlite3

# 1. Bağlan
connection = sqlite3.connect("sirket.db")
cursor = connection.cursor()

print("--- PERSONEL LİSTESİ ---")

# 2. Sorguyu Hazırla ve Çalıştır
# "personeller tablosundaki TÜM sütunları (*) getir"
cursor.execute("SELECT * FROM personeller")

# 3. Verileri Çek (Fetch)
# fetchall() komutu, sonuçları bir Python Listesi olarak getirir.
tum_veriler = cursor.fetchall()

# 4. Listeyi Döngüyle Yazdır (Python Level 2 bilgimizi kullanıyoruz!)
# Gelen her satır bir demet (tuple) şeklindedir: (1, 'Fatih', 'Yazılım', 50000)
for personel in tum_veriler:
    print(f"ID: {personel[0]} | İsim: {personel[1]} | Bölüm: {personel[2]} | Maaş: {personel[3]} TL")

print("\n--- FİLTRELEME ÖRNEĞİ (WHERE) ---")
# Sadece Maaşı 40.000'den büyük olanları getirelim
cursor.execute("SELECT * FROM personeller WHERE maas > 40000")
zenginler = cursor.fetchall()

for zengin in zenginler:
    print(f"Yüksek Maaşlı: {zengin[1]} - {zengin[3]} TL")

connection.close()