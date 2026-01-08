# --- SERVER TEMPERATURE CONTROL SYSTEM ---

print("--- SYSTEM STATUS CHECK ---")

# Kullanıcıdan sıcaklık verisini alalım
temp_input = input("Current Server Temperature (°C): ")
temperature = int(temp_input) # Sayıya çevirmeyi unutmuyoruz!

# --- DECISION LOGIC ---

# SENARYO 1: Tehlikeli Sıcaklık
# Eğer sıcaklık 80'den büyükse...
if temperature > 80:
    # Burası "Indentation" (Girinti) alanıdır.
    print("CRITICAL ALERT: Overheating!")
    print("Action: Shutting down the server immediately.")

# SENARYO 2: Yüksek Sıcaklık (Ama acil değil)
# 80 değil ama 60'tan büyük mü?
elif temperature > 60:
    print("WARNING: High temperature detected.")
    print("Action: Starting backup fans (Speed: Max).")

# SENARYO 3: Normal Sıcaklık
else:
    print("STATUS: Temperature is normal.")
    print("Action: System running in eco-mode.")

print("--- CHECK COMPLETE ---")