import sqlite3 # Python'un kendi kütüphanesi

print("--- DATABASE SYSTEM STARTED ---")

# 1. BAĞLANTI (CONNECTION)
# 'sirket.db' adında bir dosya oluşturur ve ona bağlanır.
connection = sqlite3.connect("sirket.db")

# 2. İMLEÇ (CURSOR)
# Veritabanı üzerinde işlem yapmak için yetkili bir 'el' oluşturuyoruz.
cursor = connection.cursor()

# 3. TABLO OLUŞTURMA (CREATE TABLE)
# SQL Dili burada başlıyor. Tırnak içi SQL komutudur.
# IF NOT EXISTS: Hata almamak için "Yoksa oluştur" diyoruz.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personeller (
        id INTEGER PRIMARY KEY,
        isim TEXT,
        departman TEXT,
        maas INTEGER
    )
""")
print("Tablo başarıyla oluşturuldu (veya zaten vardı).")

# 4. VERİ EKLEME (INSERT)
# Tabloya bir personel ekleyelim.
cursor.execute("""
    INSERT INTO personeller (isim, departman, maas)
    VALUES ('Fatih Coşkun', 'Yazılım', 50000)
""")

cursor.execute("""
    INSERT INTO personeller (isim, departman, maas)
    VALUES ('Ahmet Yılmaz', 'İnsan Kaynakları', 35000)
""")

# 5. KAYDETME (COMMIT)
# Bu çok önemli! Bunu yazmazsan veriler hafızada kalır, dosyaya işlenmez.
connection.commit()
print("Veriler kaydedildi.")

# 6. BAĞLANTIYI KAPAT
connection.close()