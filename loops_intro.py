# --- FOR LOOP PRACTICE ---

# Senin listen
my_languages = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]

print("--- Manuel Yöntem (Amelelik) ---")
print(my_languages[0])
print(my_languages[1])
# ... 100 tane olsa ölürdük.

print("\n\n--- FOR Döngüsü (Mühendislik) ---")

# MANTIK: 
# 'lang' burada geçici bir değişkendir (takma ad).
# Döngü her döndüğünde, listedeki sıradaki elemanı 'lang' değişkenine koyar.
for lang in my_languages:
    # Her bir dil için ne yapmak istiyorsan buraya yaz
    print(f"Bildiğim Dil: {lang}")
    print("---") 

print("Listeleme Bitti!")