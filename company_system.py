import sqlite3
import time # Programa biraz 'bekleme' efekti eklemek için

# --- VERİTABANI AYARLARI ---
connection = sqlite3.connect("sirket.db")
cursor = connection.cursor()

# Tablo yoksa oluştur (Garanti olsun)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personeller (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT,
        departman TEXT,
        maas INTEGER
    )
""")
connection.commit()

# --- FONKSİYONLAR (İŞ YAPAN ROBOTLAR) ---

def personelleri_goster():
    print("\n--- PERSONEL LİSTESİ ---")
    cursor.execute("SELECT * FROM personeller")
    liste = cursor.fetchall()
    
    if len(liste) == 0:
        print("Sistemde kayıtlı personel yok.")
    else:
        for kisi in liste:
            print(f"ID: {kisi[0]} | İsim: {kisi[1]} | Dept: {kisi[2]} | Maaş: {kisi[3]}")
    print("------------------------\n")

def personel_ekle():
    print("\n--- YENİ PERSONEL EKLE ---")
    ad = input("İsim Soyisim: ")
    dept = input("Departman: ")
    maas = int(input("Maaş: "))
    
    cursor.execute("INSERT INTO personeller (isim, departman, maas) VALUES (?, ?, ?)", (ad, dept, maas))
    connection.commit()
    print("✅ Personel başarıyla eklendi!")

def maas_guncelle():
    print("\n--- MAAŞ GÜNCELLEME ---")
    personelleri_goster() # Önce listeyi görsün ki ID seçebilsin
    
    secilen_id = int(input("Maaşı değişecek personelin ID'si: "))
    yeni_maas = int(input("Yeni Maaş Miktarı: "))
    
    cursor.execute("UPDATE personeller SET maas = ? WHERE id = ?", (yeni_maas, secilen_id))
    connection.commit()
    print("✅ Maaş güncellendi!")

def personel_sil():
    print("\n--- PERSONEL SİLME ---")
    personelleri_goster()
    
    secilen_id = int(input("Silinecek personelin ID'si: "))
    
    cursor.execute("DELETE FROM personeller WHERE id = ?", (secilen_id,))
    connection.commit()
    print("🗑️ Personel silindi.")

# --- ANA PROGRAM DÖNGÜSÜ (MAIN LOOP) ---

print("***********************************")
print("* ŞİRKET OTOMASYONUNA HOŞGELDİNİZ  *")
print("***********************************")

while True:
    print("İŞLEMLER:")
    print("1. Personelleri Göster")
    print("2. Yeni Personel Ekle")
    print("3. Maaş Güncelle")
    print("4. Personel Sil")
    print("5. Çıkış")
    
    secim = input("Seçiminiz (1-5): ")
    
    if secim == '1':
        personelleri_goster()
    elif secim == '2':
        personel_ekle()
    elif secim == '3':
        maas_guncelle()
    elif secim == '4':
        personel_sil()
    elif secim == '5':
        print("Sistemden çıkılıyor...")
        time.sleep(1) # 1 saniye bekle
        print("Güle güle!")
        break # Döngüyü kırar ve programı kapatır
    else:
        print("❌ Hatalı seçim, tekrar deneyin.")
        
# Bağlantıyı kapatmayı unutmayalım
connection.close()