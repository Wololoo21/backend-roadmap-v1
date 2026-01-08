# --- INPUT & CASTING PRACTICE ---

print("--- Simple Calculator ---")

# Kullanıcıdan iki sayı isteyelim
# input() takes everything as String!
num1_input = input("First Number: ") 
num2_input = input("Second Number: ")

# İŞLEM 1: Dönüşüm yapmadan toplarsak ne olur?
result_wrong = num1_input + num2_input
print(f"Wrong Result (String): {result_wrong}")

# --- FIXING THE BUG (HATA DÜZELTME) ---

# Şimdi o stringleri Sayıya (Integer) çevirelim
# int() function converts string to integer.
num1 = int(num1_input)
num2 = int(num2_input)

# İŞLEM 2: Şimdi toplayalım
result_correct = num1 + num2
print(f"Correct Result (Integer): {result_correct}")