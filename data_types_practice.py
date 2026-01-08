# --- DATA TYPES PRACTICE ---

# 1. Integer (Tam Sayı)
# Dikkat: Tırnak işareti yok, direkt sayı.
score = 100

# 2. Float (Ondalıklı Sayı)
# Dikkat: Virgül değil NOKTA kullanılır.
health_points = 95.5

# 3. String (Metin)
# Dikkat: Mutlaka tırnak (tek veya çift) içinde olmalı.
character_name = "Warrior"

# 4. Boolean (Mantıksal)
# Dikkat: Tırnak yok ve Baş harfi BÜYÜK olmak zorunda (True/False).
is_alive = True

# --- INSPECTION (İNCELEME) ---

# Şimdi Python'a bu değişkenlerin tiplerini soralım.
print("--- Variable Types ---")

print(score)
print(type(score))  # Çıktı: <class 'int'> olmalı

print(health_points)
print(type(health_points)) # Çıktı: <class 'float'> olmalı

print(character_name)
print(type(character_name)) # Çıktı: <class 'str'> olmalı

print(is_alive)
print(type(is_alive)) # Çıktı: <class 'bool'> olmalı