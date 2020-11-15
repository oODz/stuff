import random
import time
import sys


def displayIntro() -> str:
    """Sets the stage for our hero. Prints a multiline story string."""
    
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
print()


def chooseCave() -> str:
    """Checks to see if user chose cave 1 or 2. Returns the value of user's
selection and assigns it to the variable cave which was previously an
empty string."""
    
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave) -> str:
    """Continues story narration. Checks whether or not the cave selected
by the user matches the value of friendlyCave determined by randint."""
    
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Winks at you and says: \'Get outta here!\'')
    else:
        print('Lunges at you and attacks!')


def fightFlight() -> str:
    """Determines whether hero wants to fight or flee. In the case the hero
wants to fight, this func. checks how much damage each hit does to the dragon.
If sufficient damage is dealt, it will pronounce the dragon dead"""
    
    print('Do you want to attack him, or flee?')
    decision = input()
    life = 100
    damage = random.randint(0, 100)
    hp = life - damage

    while hp > 0:

        if decision == 'attack him':
            print('Your attack inflicted', damage, 'damage!')
            if damage == 100:
                print('Your attack defeated the dragon in one shot!')
             
            else:
                print('The dragon still has', hp, 'left! Keep going!')
                damage = random.randint(0, 100)
                hp = hp - damage
                time.sleep(1)
                if hp <= 0:
                    print('The dragon is dead!')
                    break
                      
        elif decision == 'flee':
            print('You successfully fled!')
            break

            
def main():
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    fightFlight()
    print('Do you want to play again?')
    if input() == 'yes':
        main()
    else:
        sys.exit()
        
#main
if __name__ == '__main__':
    main()


