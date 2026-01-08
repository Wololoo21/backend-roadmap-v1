import sqlite3

connection = sqlite3.connect("sirket.db")
cursor = connection.cursor()

print("--- OPERASYON ÖNCESİ DURUM ---")
# Hızlıca mevcut listeyi görelim
cursor.execute("SELECT * FROM personeller")
for kisi in cursor.fetchall():
    print(kisi)

# --- İŞLEM 1: UPDATE (GÜNCELLEME) ---
# Senaryo: Fatih Coşkun (ID: 1) çok çalıştı, maaşına zam yapalım.
print("\n... Zam Yapılıyor ...")

# MANTIK: personeller tablosunu GÜNCELLE, maas'ı 75000 YAP, AMA sadece ismi 'Fatih Coşkun' OLANIN.
cursor.execute("""
    UPDATE personeller 
    SET maas = 75000 
    WHERE isim = 'Fatih Coşkun'
""")

# --- İŞLEM 2: DELETE (SİLME) ---
# Senaryo: İnsan Kaynakları bölümü kapatıldı. Ahmet Yılmaz (veya İK'daki herkes) çıkarılacak.
print("... İşten Çıkarma Yapılıyor ...")

# MANTIK: personeller tablosundan SİL, AMA sadece departmanı 'İnsan Kaynakları' OLANLARI.
cursor.execute("""
    DELETE FROM personeller 
    WHERE departman = 'İnsan Kaynakları'
""")

# Değişiklikleri kaydet (Bunu unutursan her şey geri alınır)
connection.commit()

print("\n--- OPERASYON SONRASI DURUM ---")
cursor.execute("SELECT * FROM personeller")
for kisi in cursor.fetchall():
    print(kisi)

connection.close()