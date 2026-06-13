import random

print("=== JEU BONJOUR2025 ===")
print("Devine le nombre entre 1 et 50 !")

nombre_secret = random.randint(1, 50)
essais = 0

while True:
    essais += 1
    guess = int(input("Ton essai: "))
    
    if guess < nombre_secret:
        print("Trop petit ! ⬆️")
    elif guess > nombre_secret:
        print("Trop grand ! ⬇️")
    else:
        print(f"Bravo ! Trouvé en {essais} essais 🎉")
        break
