import os 
import time
import random
import climage

os.system('cls')

def battle(): 
    gojo_hp = 150 
    sukuna_hp = 150 

    # loop to make sure the game continues as long as both are alive
    while gojo_hp > 0 and sukuna_hp > 0: 
        print("\n=============================")
        print(f"Gojo HP: {gojo_hp} | Sukuna HP: {sukuna_hp}")
        print("=============================")
        print("Choose your move (enter the number):")
        print("1. Cursed Technique Red")
        print("2. Cursed Technique Blue (80% to hit)")
        print("3. Hollow Purple (30% to hit)")
        print("4. Reverse Cursed Technique (heals you)")

        choice = input("> ").title()

        # Player Moves
        # Red
        if choice == "1":
            print(f"\nGojo points his fingers at Sukuna...")
            time.sleep(1)
            print("A wave of destructive energy blasts through the skies!")
            damage = random.randint(10, 20)
            sukuna_hp -= damage 
            print(f"Red hits Sukuna for {damage} damage!")

        #Blue 
        elif choice == "2":
            print("\nGravity bends and sucks in everything into a blue ball...")
            time.sleep(1.5)
            # Create a probability check (80%)
            if random.random() < 0.8:
                damage == random.randint(20, 35)
                sukuna_hp -= damage 
                print(f"Blue blasts Sukuna for {damage} damage!")
            else: 
                print("Blue spins out of control and explodes far away!")
                print("You delt 0 damage! ")

        # Hollow Purple 
        elif choice == "3":
            print("\nGojo smashes red and blue into one! Creating his ultimate technique: Hollow Purple!")
            time.sleep(2)
            # Creative a probability check (30%)
            if random.random() < 0.3:
                damage = random.randint(40, 55)
                sukuna_hp -= damage 
                print(f"Hollow Purple tears through Sukuna for {damage} damage! That's gotta hurt...")
            else: 
                print("Hollow Purple exploded half way to Sukuna...")
                print("You delt 0 damage!")

        # Reverse Cursed Technique 
        if choice == "4":
            print("\nGojo activates Reverse Cursed Technique...")
            time.sleep(1.5)
            heal = random.randint(25, 40)
            gojo_hp += heal
            if gojo_hp > 150:
                gojo_hp = 150
            print(f"Gojo heals for {heal} HP! His body surges with cursed energy!")


        # Sukuna's Turn
        if sukuna_hp > 0:
            print("\nSukuna prepares a cursed attack...")
            time.sleep(1)
            damage = random.randint (15, 25)
            gojo_hp -= damage
            print(f"Sukuna attacks! You take {damage} damage!")


    # End of battle
    print("\n=============================")
    if gojo_hp <= 0 and sukuna_hp <= 0:
        print("Both fighters fall... It's a draw!")
    elif sukuna_hp <= 0:
        print("Gojo wins! Sukuna has been defeated!")
        # climage.convert('', is_unicode=True)
    else: 
        print("Sukuna wins! Gojo has fallen...")
    print("=============================")

if __name__ == '__main__':
    battle()