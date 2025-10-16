import os 
import time
import random
import climage

os.system('cls')

def battle(): 
    gojo_hp = 150 
    sukuna_hp = 200 
    gojo_sanity = 100 
    sukuna_sanity = 100

    sukuna_stun_turns = 0
    fuga_burn_turns = 0 
    domain_turns = 0 
    gojo_domain_active = 0
    sukuna_domain_active = 0 




    # loop to make sure the game continues as long as both are alive
    while gojo_hp > 0 and sukuna_hp > 0 and gojo_sanity > 0 and sukuna_sanity > 0: 
        print("\n===================================")
        print(f"Gojo HP: {gojo_hp} | Gojo Sanity: {gojo_sanity} \nSukuna HP: {sukuna_hp} | Sukuna Sanity: {sukuna_sanity}")
        print("===================================")
        print("Choose your move (enter the number):")
        print("1. Cursed Technique Red\n   -10 Sanity")
        print("2. Cursed Technique Blue\n   -15 Sanity | 80% to hit")
        print("3. Hollow Purple\n   -30 Sanity | 50% to hit")
        print("4. Reverse Cursed Technique\n   Heals HP | +15 Sanity")
        print("5. Domain Expansion: Infinite Void\n   -25 Sanity | Stuns Sukuna for 2 turns")

        choice = input("> ").title()

        # Function to check if Gojo loses control
        def loses_control():
            if gojo_sanity < 20:
                return random.random() < 0.4 # 40% for Gojo to lose control if his sanity is below 20 

        # Player Moves

        # Red
        if choice == "1":
            if gojo_sanity >= 10:
                print(f"\nGojo points his fingers at Sukuna...")
                time.sleep(1)
                if loses_control():
                    blacklash = random.randint(10, 25)
                    gojo_hp -= blacklash 
                    gojo_sanity -= 5
                    print(f"Gojo loses control! Red backfires, hurting him for {blacklash} HP!")
                else: 
                    damage = random.randint(10, 20)
                    sukuna_hp -= damage 
                    print("A wave of destructive energy blasts through the skies!")
                    print(f"Red hits Sukuna for {damage} damage!")
            else: 
                print("\nGojo's mind is unstable... he can't form Red!")

        #Blue 
        elif choice == "2":
            if gojo_sanity >= 10: 
                print("\nGravity bends and sucks in everything into a blue ball...")
                time.sleep(1.5)
                if loses_control():
                    blacklash = random.randint(20, 30)
                    gojo_hp -= blacklash
                    gojo_sanity -= 5
                    print(f"Gojo loses control! Blue implodes, dealing {blacklash} damage to himself!")
                # Create a probability check (80%)
                elif random.random() < 0.8:
                    damage == random.randint(20, 35)
                    sukuna_hp -= damage 
                    print(f"Blue blasts Sukuna for {damage} damage!")
                else: 
                    print("Blue spins out of control and explodes far away!")
            else: 
                print("\nGojo's mind is unstabke... Blue fizzles out!")


        # Hollow Purple 
        elif choice == "3":
            if gojo_sanity >= 30:
                print("\nGojo smashes red and blue into one! Creating his ultimate technique: Hollow Purple!")
                time.sleep(2)
                if loses_control():
                    blacklash = random.randint(25, 40)
                    gojo_hp -= blacklash
                    gojo_sanity -= 10 
                    print(f"Hollow Purple collapses inward! Gojo takes {blacklash} damage form his own power!")
                # Creative a probability check (30%)
                else:
                    random.random() < 0.3
                    damage = random.randint(40, 55)
                    sukuna_hp -= damage 
                    print(f"Hollow Purple tears through Sukuna for {damage} damage! That's gotta hurt...")
            else: 
                print("\nGojo doesn't have enough sanity to use Hollow")

        # Reverse Cursed Technique 
        elif choice == "4":
            print("\nGojo activates Reverse Cursed Technique...")
            time.sleep(1.5)
            heal = random.randint(25, 40)
            sanity_gain = 15
            gojo_hp = min(100, gojo_hp + heal)
            gojo_sanity = min(100, gojo_sanity + sanity_gain)
            print(f"Gojo heals for {heal} HP and regains {sanity_gain} sanity!")
        
        # Domain Expansion: Infinite Void
        elif choice == "5":
            if gojo_sanity >= 25:
                print("\nGojo activates Domain Expansion: Infinite Void!")
                time.sleep(2)
                print("Space distorts... Sukuna is trapped in endless knowledge!")
                sukuna_stun_turns = 2
                gojo_domain_active = 2
                gojo_sanity -= 25
            else:
                print("\nGojo's sanity is too low to expand his domain!")
        else:
            print("\nGojo hesitates, losing his focus!")


        # Sukuna's Moveset
        if sukuna_hp > 0:
            if sukuna_stun_turns > 0:
                print("\nSukuna is trapped in the Infinite Void! He can't move this turn!")
                sukuna_stun_turns -= 1 # Reduces stun duration
            else: 
                # List of possible moves that can be done if sanity is enough 
                move = random.choice(["cleave", "dismantle", "fuga", "domain"])
                # Cleave
                if move == "cleave" and sukuna_sanity >= 10:
                    print("\nSukuna slashes with Cleave!")
                    damage = random.randint(10, 20)
                    gojo_hp -= damage 
                    sukuna_sanity -= 10
                    print(f"Cleave deals {damage} damage!")
                # Dismantle
                elif move == "dismantle" and sukuna_sanity >= 15:
                    print("\nSukuna swings with Dismantle!")
                    damage = random.randint(20, 30)
                    gojo_hp -= damage 
                    sukuna_sanity -= 15
                    print(f"Dismantle rips Gojo for {damage} damage!")
                # Fuga
                elif move == "fuga" and sukuna_sanity >= 25:
                    print("\nThe air increases in heat as a mysterious fire arrow summons in the hands of Sukuna!")
                    damage = random.randint(30, 45)
                    gojo_hp -= damage 
                    sukuna_sanity -= 25
                    print(f"Fuga deals {damage} damage and burns Gojo for 3 turns!")

                # Sukuna Domain Expansion
                elif move == "domain" and sukuna_sanity >= 30:
                    print("\nSukuna attempts Domain Expansion!")
                    if gojo_domain_active > 0:
                        print("DOMAIN CLASH! Both domains collide violently!")
                        clash_damage_gojo = random.randint(5, 15)
                        clash_damage_sukuna = random.randint(5, 15)
                        gojo_hp -= clash_damage_gojo
                        sukuna_hp -= clash_damage_sukuna
                        print("Both take damage! Gojo {clash_damage_gojo}, Sukuna {clash_damage_sukuna}")
                    sukuna_domain_active = 5
                    sukuna_sanity -= 30 
                    print("\nSukuna's Malevolent Shrine is active for 5 turns!")
                    domain_turns = 5
                    sukuna_sanity -= 30
                    print("The air itself fills with Dismantles and Cleaves, cutting Gojo for 5 turns!")

                else:
                    print("\nSukuna grins sinisterly and recovers his cursed energy...")
                    sukuna_sanity = min(100, sukuna_sanity + 10)
            if fuga_burn_turns > 0:
                burn = 10
                gojo_hp -= burn 
                fuga_burn_turns -= 1 # Reduces burn duration
                print(f"Gojo burns for {burn} damage! ({fuga_burn_turns} turns left)")
            
            if domain_turns > 0:
                domain_damage = 5
                gojo_hp -= domain_damage
                domain_turns -= 1 # Reduces Malevolent Shrine Effect Turns
                print(f"Malevolent Shrine deals {domain_damage} damage! ({domain_turns} turns left)")

            if gojo_domain_active > 0:
                gojo_domain_active -= 1
            
            if sukuna_domain_active > 0: 
                damage = 5 
                gojo_hp -= damage 
                sukuna_domain_active -= 1 # Reduces Sukuna's Domain Duration
                print(f"Malevolent Shrine deals {damage} damage to Gojo! ({sukuna_domain_active} turns left)")

    # End of battle
    print("\n===================================")
    if gojo_hp <= 0 and sukuna_hp <= 0:
        print("Both fighters fall... It's a draw!")
    elif sukuna_hp <= 0:
        print("Gojo wins! Sukuna has been defeated!")
    elif gojo_sanity <= 0:
        print("Gojo's mind collapses under his own power... He loses control!")
    elif sukuna_sanity <= 0:
        print("Sukuna runs out of cursed energy and collapses!")
        print("The Disgraced One has fallen...")
    else: 
        print("Sukuna wins! Gojo has fallen...")
    print("===================================")

if __name__ == '__main__':
    battle()