from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # Veri doğrulama için (C# Class gibi)
import sqlite3

app = FastAPI()

# --- 1. MODEL (SCHEMA) ---
# Kullanıcıdan gelecek verinin kalıbı.
# C#'taki Class/DTO mantığının aynısıdır.
class PersonelModel(BaseModel):
    isim: str
    departman: str
    maas: int

# --- 2. YARDIMCI FONKSİYON ---
# Veritabanına bağlanıp imleç (cursor) veren fonksiyon.
def baglanti_kur():
    conn = sqlite3.connect("sirket.db")
    conn.row_factory = sqlite3.Row # Verileri sözlük (dict) gibi çekmek için
    return conn

# --- 3. ENDPOINTS (UÇ NOKTALAR) ---

# A. LİSTELEME (GET)
@app.get("/personeller")
def personelleri_getir():
    conn = baglanti_kur()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM personeller")
    veriler = cursor.fetchall()
    
    conn.close()
    return veriler

# B. EKLEME (POST)
# Dikkat: Burada 'personel' değişkeni yukarıdaki Model tipindedir.
# FastAPI, gelen JSON verisini otomatik olarak bu modele çevirir.
@app.post("/personel-ekle")
def personel_ekle(personel: PersonelModel):
    conn = baglanti_kur()
    cursor = conn.cursor()
    
    # Modelden verileri alıp SQL'e yazıyoruz
    cursor.execute("INSERT INTO personeller (isim, departman, maas) VALUES (?, ?, ?)", 
                   (personel.isim, personel.departman, personel.maas))
    
    conn.commit()
    conn.close()
    
    return {"mesaj": "Personel başarıyla eklendi", "eklenen": personel}

# C. SİLME (DELETE)
# URL'den ID alıyoruz (Örn: /personel-sil/5)
@app.delete("/personel-sil/{personel_id}")
def personel_sil(personel_id: int):
    conn = baglanti_kur()
    cursor = conn.cursor()
    
    # Önce var mı diye bakalım
    cursor.execute("SELECT * FROM personeller WHERE id = ?", (personel_id,))
    kayit = cursor.fetchone()
    
    if kayit is None:
        # Hata fırlatma (404 Not Found)
        raise HTTPException(status_code=404, detail="Böyle bir personel bulunamadı")
    
    # Varsa sil
    cursor.execute("DELETE FROM personeller WHERE id = ?", (personel_id,))
    conn.commit()
    conn.close()
    
    return {"mesaj": f"{personel_id} numaralı kayıt silindi."}