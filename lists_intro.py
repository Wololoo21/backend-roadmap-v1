# --- LISTS PRACTICE ---

print("--- MY SKILL SET ---")

# 1. Liste Oluşturma (Köşeli parantez [] kullanılır)
# Stringlerden oluşan bir liste tanımlıyoruz.
my_languages = ["Python", "C#", "SQL", "HTML"]

# Listenin tamamını görelim
print(f"All Languages: {my_languages}")

# 2. Belirli Bir Elemana Ulaşma (Indexing)
# İlk elemanı almak için [0] kullanırız.
first_lang = my_languages[0] 
print(f"First learned: {first_lang}")

# Üçüncü elemanı almak için [2] kullanırız (0, 1, 2)
third_lang = my_languages[2]
print(f"Database Skill: {third_lang}")

# 3. Listeye Yeni Eleman Ekleme (Append)
# .append() komutu listenin EN SONUNA ekleme yapar.
print("--- Learning new skill... ---")
my_languages.append("JavaScript")

# Bakalım eklenmiş mi?
print(f"Updated List: {my_languages}")

# 4. Listede kaç eleman var? (Length)
# len() fonksiyonu listenin uzunluğunu verir.
count = len(my_languages)
print(f"Total Skills: {count}")



# my shit from here -------

print("MY SKILL SET")

my_languages = ["python","java","c++","javascript","html","css"]
my_languages_len = len(my_languages)

print(f"here they are: {my_languages}")

print(f"leng is : {my_languages_len}")

input_language = input("select one :")
selected_language = int(input_language)

if selected_language < my_languages_len:
    print(f"selected language is : '{selected_language}' so it is : '{my_languages[selected_language]}'")
    print(f"seçtiğiniz dil: {my_languages[selected_language]}")
else:    
    print("tekrar seç sikerinm")

new_language = input("yeni dil gir : ")
my_languages.append(new_language)

input_language = input("select second :")
selected_language = int(input_language)

print(f"yeni dil bu : {my_languages[6]}")
my_languages_len = len(my_languages)

print(f"here they are: {my_languages}")

print(f"leng is : {my_languages_len}")

if selected_language < my_languages_len:
    print(f"selected language is : '{selected_language}' so it is  : '{my_languages[selected_language]}' ")
    print(f"seçtiğiniz dil: {my_languages[selected_language]}")
else:    
    print("tekrar seç sikerinm")
