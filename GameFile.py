from time import sleep
import random
import os


class weapon:

    def __init__(self, a1dmin, a1dmax, a1n, a1e, a2dmin, a2dmax, a2n, a2e, name, a1ef, a2ef, size, a1cp, a2cp):

        self.a1dmin = a1dmin
        self.a1dmax = a1dmax
        self.a1n = a1n
        self.a1e = a1e
        self.a2dmin = a2dmin
        self.a2dmax = a2dmax
        self.a2n = a2n
        self.a2e = a2e
        self.name = name
        self.a1ef = a1ef
        self.a2ef = a2ef
        self.size = size
        self.a1cp = a1cp
        self.a2cp = a2cp



class enemy:

    def __init__(self, name, health, maxhealth, dmin, dmax, gold, chest, potion, cb, dif, mag, evasionchance):

        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.dmin = dmin
        self.dmax = dmax
        self.gold = gold
        self.chest = chest
        self.potion = potion
        self.cb = cb
        self.dif = dif
        self.mag = mag
        self.evasionchance = evasionchance



class character:

    def __init__(self, playerclass, strength, health, maxhealth, escapechance, criticalchance, basedamage1min, basedamage1max,
                 basedamage2min, basedamage2max, name, rageeffect, armoramount, magicdefense, magicdamage):

        self.playerclass = playerclass
        self.strength = strength
        self.health = health
        self.maxhealth = maxhealth
        self.escapechance = escapechance
        self.criticalchance = criticalchance
        self.basedamage1min = basedamage1min
        self.basedamage1max = basedamage1max
        self.basedamage2min = basedamage2min
        self.basedamage2max = basedamage2max
        self.name = name
        self.rageeffect = rageeffect
        self.armoramount = armoramount
        self.magicdefense = magicdefense
        self.magicdamage = magicdamage


ironsword = weapon(18, 28, 'Slash', 3, 12, 25, 'Stab', 4, 'Iron Sword', None, 'critical', 3, None, 2)
ironaxe = weapon(16, 34, 'Swing', 3, 10, 19, 'Stun', 4, 'Iron Axe', None, 'stun', 2, None, None)
dagger = weapon(12, 19, 'Stab', 2, 8, 17, 'Slash', 1, 'Dagger', 'critical', None, 2, 2, None)


#NAME = CLASS (NAME, DMIN, DMAX, LOOT, CB, GA, CA, PA, DIF)
goblin = enemy('Goblin', 70, 70, 14, 27, True, False, False, 1, 'basic', False, 1)
bandit = enemy("Bandit", 80, 80, 12, 33, True, False, False, 2, 'basic', False, 1)


playeractiveweapon = ironsword
playeractivearmor = 'Iron Armor'
armorstrength = .4
magicstrength = 0

cycle = False
escape = False
questcycle = False

player = character(None, 3, 200, 200, 3, 1, playeractiveweapon.a1dmin, playeractiveweapon.a1dmax, playeractiveweapon.a2dmin,
                   playeractiveweapon.a2dmax, None, .2, None, None, 0)

playerenergy = 30
playerenergymax = 30
inventory = []
inventorysee = []
playername = None
isplayerpoison = False
playerpoisonturn = 0
isplayerrage = False
playerrageturn = 0
playergold = 500

playeractiveeffects = []
enemyactiveeffects = []

activeenemy = goblin
isenemypoison = False
enemypoisonturn = 0
isenemydeath = False

questlocation = None
activequest = None
activequestname = None

town = True
playerlocation =  'Abandoned Cave'
location = ['Grand Castle', 'Abandoned Cave', 'Village Of Norbury', 'Small Town Of Ironforge']


basicgoldloot = [100, 100, 100, 200, 200, 100, 300, 400,  300, 200, 100, 100, 100]
hardgoldloot = [300, 300, 400, 200, 500, 300, 400, 100, 200, 300]
difficultgoldloot = [600, 700, 700, 800, 1000, 500, 600, 800, 900, 600]
legendarygoldloot = [1000, 1500, 1400, 1300, 900, 1100, 1400, 1200]

potionlist = ['health potion', 'health flask', 'max health potion', 'energy flask', 'energy potion', 'max energy potion',
               'strength flask', 'strength potion', 'rage flask', 'rage potion']


override = False

travelenemies = [goblin, bandit]

#FUNCTIONS

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def chest():
    pass


def loot():

    global playergold


    if activeenemy.gold is True:

        if activeenemy.dif == 'basic':
            rangold = random.choice(basicgoldloot)
            print("The %s dropped %s Gold! " % (activeenemy.name, rangold))
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            playergold += rangold
            return



        if activeenemy.dif == 'hard':
            pass

        if activeenemy.dif == 'lethal':
            pass

        if activeenemy.dif == 'legendary':
            pass


    if activeenemy.chest is True:

        if activeenemy.dif == 'basic':
            ranchest = random.randrange(1, 11)

            if ranchest in [1, 2]:
                print("%s dropped a loot chest! ")
                chest()

            else:
                pass

        if activeenemy.dif == 'hard':
            pass

        if activeenemy.dif == 'difficult':
            pass

        if activeenemy.dif == 'legendary':
            pass


    if activeenemy.potion is True:

        if activeenemy.dif == 'basic':
            pass

        if activeenemy.dif == 'hard':
            pass

        if activeenemy.dif == 'legendary':
            pass

    return


def classbonus():

    global playeractiveweapon

    if playerclass == 'warrior':
        pass

    if playerclass == 'knight':
        pass

    if playerclass == 'mage':
        pass

    if playerclass == 'hunter':
        pass

    if playerclass == 'rogue':
        pass


def checkenemyhealth(activeenemy):

    if activeenemy.health <= 0:

        print("You have defeated the %s! " % activeenemy.name)
        while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
        return

    if activeenemy.health > 0:
        return


def poison(player):

    global isplayerpoison
    global isenemypoison
    global enemypoisonturn
    global playerpoisonturn

    if isplayerpoison is True:

        if playerpoisonturn > 0:

            poisoneffect = int(player.health * .10)
            player.health -= poisoneffect
            print("You took %s damage from poison" % poisoneffect)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            playerpoisonturn -= 1

        if playerpoisonturn <= 0:
            print("Poison has worn off! ")
            isplayerpoison = False
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            return

    if isenemypoison is True:

        if enemypoisonturn > 0:

            poisoneffect = int(activeenemy.health * .10)
            activeenemy.health -= poisoneffect
            print("Poison dealt %s damage to the %s! It's Health is now at %s" %
                  (poisoneffect, activeenemy.name, activeenemy.health))
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            enemypoisonturn -= 1
            return


        if enemypoisonturn <= 0:
            print("Poison has worn off on the %s! " % activeenemy.name)
            isenemypoison = False
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            return


def rage(player):

    global playeractiveweapon
    global isplayerrage
    global playerrageturn

    oa1min = playeractiveweapon.a1dmin
    oa1max = playeractiveweapon.a1dmax
    oa2min = playeractiveweapon.a2dmin
    oa2max = playeractiveweapon.a2dmax

    if isplayerrage is True:

        print("Your damage increased by %s percent! " % int((player.rageeffect * 100)))
        isplayerrage = False
        player.criticalchance -= 1

        a1dminp = int(playeractiveweapon.a1dmin * player.rageeffect)
        playeractiveweapon.a1dmin = playeractiveweapon.a1dmin + a1dminp

        a1dmaxp = int(playeractiveweapon.a1dmax * player.rageeffect)
        playeractiveweapon.a1dmax = playeractiveweapon.a1dmax + a1dmaxp

        a2dminp = int(playeractiveweapon.a2dmin * player.rageeffect)
        playeractiveweapon.a2dmin = playeractiveweapon.a2dmin + a2dminp

        a2dmaxp = int(playeractiveweapon.a2dmax * player.rageeffect)
        playeractiveweapon.a2dmax = playeractiveweapon.a2dmax + a2dmaxp


    if playerrageturn <= 0:
        print("Rage has worn off! ")
        playeractiveweapon.a1dmin = oa1min
        playeractiveweapon.a1dmax = oa1max
        playeractiveweapon.a2dmin = oa2min
        playeractiveweapon.a2dmax = oa2max
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        return

    playerrageturn -= 1

    return


def enemyattack(activeenemy):

    if activeenemy.mag is True:
        enemydamagepre = random.randrange(activeenemy.dmin, activeenemy.dmax)
        edreduction = enemydamagepre * magicstrength
        enemydamage = int(round(enemydamagepre - edreduction))

        print("%s attacks with magic, dealing %s damage! " % (activeenemy.name, enemydamage))
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        player.health -= enemydamage
        if player.health <= 0:
            print("You have died! ")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            exit(0)
        return

    else:
        enemydamagepre = random.randrange(activeenemy.dmin, activeenemy.dmax)
        edreduction = enemydamagepre * armorstrength
        enemydamage = int(round(enemydamagepre - edreduction))

        print("%s attacks, dealing %s damage! " % (activeenemy.name, enemydamage))
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        player.health -= enemydamage
        if player.health <= 0:
            print("You have died! ")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            exit(0)
        return


def useitem(player):

    global playerenergy
    global playerenergymax

    while True:

        print(inventorysee)
        itemuse = str.lower(input("Use which item? "))

        if itemuse not in inventory:
            print("You don't have that item! ")
            continue

        elif itemuse is 'health flask':

            if player.health == player.maxhealth:
                print("Your health is already at max! ")
                continue
            player.health += 30
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print("Your health is now at %s" % player.health)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break

        elif itemuse is 'health potion':

            if player.health == player.maxhealth:
                print("Your health is already at max! ")
                continue
            player.health += 60
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print("Your health is now at %s" % player.health)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            continue

        elif itemuse is 'max health potion':
            if player.health == player.maxhealth:
                print("You are already at max")
                continue
            player.health = player.maxhealth
            print("Your health is now at %s" % player.health)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            continue

        elif itemuse is 'rage flask':
            print("You are now filled with rage")
            isplayerrage = True
            playerrageturn = 1
            continue

        elif itemuse is 'rage potion':
            print("You are now filled with rage")
            isplayerrage = True
            playerrageturn = 3

        elif itemuse is 'energy flask':
            if playerenergy == playerenergymax:
                print("Your energy is already at max! ")
                continue
            playerenergy += 10
            if playerenergy > playerenergymax:
                playerenergy = playerenergymax
            print("Your energy is now at %s" % playerenergy)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            continue

        elif itemuse is 'energy potion':
            if playerenergy == playerenergymax:
                print("Your energy is already at max! ")
                continue
            playerenergy += 20
            playerenergy = playerenergymax
            print("Your energy is now at %s " % playerenergy)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            continue

        elif itemuse is 'max energy potion':
            if playerenergy == playerenergymax:
                print("Your energy is already at max! ")
                continue
            playerenergy = playerenergymax
            print("Your energy is now at %s" % playerenergy)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            continue

        elif itemuse is 'strength flask':
            player.strength += 1
            print("Your strength has increased by 1! ")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            print("Your strenth is now at %s" % player.strength)
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            continue

        elif itemuse is 'strength potion':
            player.strength += 2
            print("Your strength has incresed by 2! ")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            print("Your strength is now at %s" % player.strength)

        elif itemuse is 'exit':
            return


def playerattack(player):

    global playerenergy
    global inventory
    global inventorysee
    global cycle
    global escape
    global playeractiveeffects
    global enemyactiveeffects
    global isplayerpoison
    global isenemypoison
    global enemypoisonturn
    global override

    while True:

        if isplayerpoison is True:
            playeractiveeffects.append("Poison, %s turn(s)" % playerpoisonturn)

        if isplayerrage is True:
            playeractiveeffects.append("Rage, %s turn(s)" % playerrageturn)

        if isplayerpoison is False and isplayerrage is False:
            playeractiveeffects.append("None")

        if isenemypoison is True:
            enemyactiveeffects.append("Poison, %s turn(s)" % enemypoisonturn)

        else:
            enemyactiveeffects.append("None")

        print("Player: ")
        print("\n" * 0)
        print("Health: %s" % player.health)
        print("Energy: %s" % playerenergy)
        print("Effects: %s" % playeractiveeffects)
        print("\n" * 0)
        print("%s: " % activeenemy.name)
        print("\n" * 0)
        print("Health: %s" % activeenemy.health)
        print("Effects: %s" % enemyactiveeffects)
        print("Difficulty: %s " % str.capitalize(activeenemy.dif))
        print("\n" * 0)
        sleep(.7)

        playeractiveeffects = []
        enemyactiveeffects = []

        attack = str.lower(input("Attack, Use Item, or Escape? (Attack, Item, Escape) "))
        clear_screen()
        sleep(.5)

        if attack == 'attack':

            print("Player: ")
            print("\n" * 0)
            print("Health: %s" % player.health)
            print("Energy: %s" % playerenergy)
            print("Effects: %s" % playeractiveeffects)
            print("\n" * 0)
            print("%s: " % activeenemy.name)
            print("\n" * 0)
            print("Health: %s" % activeenemy.health)
            print("Effects: %s" % enemyactiveeffects)
            print("Difficulty: %s" % activeenemy.dif)
            print("\n" * 0)
            sleep(.4)

            attackchoice = str.capitalize(input("Which attack? %s, %s ('attack' + info for more information) " %
                                                (playeractiveweapon.a1n, playeractiveweapon.a2n)))
            clear_screen()
            sleep(.5)

            if activeenemy.dif is "basic":
                enemyinvasionchance = random.randrange(activeenemy.evasionchance, 11)

                if enemyinvasionchance in [1, 2, 3]:
                    print("The %s evaded your attack! " % activeenemy.name)
                    while True:
                        a = input("Press enter to continue...")
                        if a == '':
                            clear_screen()
                            sleep(.5)
                            break
                    return

                else:

                    if attackchoice == playeractiveweapon.a1n:

                        if playerenergy - playeractiveweapon.a1e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a1e
                            attackamount = random.randrange(playeractiveweapon.a1dmin, playeractiveweapon.a1dmax)

                            if playeractiveweapon.a1ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                            if playeractiveweapon.a1ef == 'critical':
                                player.criticalchance += playeractiveweapon.a1cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                            if playeractiveweapon.a1ef == 'poison':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a2n:

                        if playerenergy - playeractiveweapon.a2e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a2e
                            attackamount = random.randrange(playeractiveweapon.a2dmin, playeractiveweapon.a2dmax)

                            if playeractiveweapon.a2ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                            if playeractiveweapon.a2ef == 'critical':
                                player.criticalchance += playeractiveweapon.a2cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                            if playeractiveweapon.a2ef == 'posion':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a1n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (playeractiveweapon.a1n, playeractiveweapon.a1dmin,
                                                                             playeractiveweapon.a1dmax, playeractiveweapon.a1e,
                                                                             playeractiveweapon.a1ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break


                    elif attackchoice == playeractiveweapon.a2n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (playeractiveweapon.a2n, playeractiveweapon.a2dmin,
                                                                             playeractiveweapon.a2dmax, playeractiveweapon.a2e,
                                                                             playeractiveweapon.a2ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break

                    else:
                        continue

            elif activeenemy.dif is "hard":
                enemyinvasionchance = random.randrange(activeenemy.evasionchance, 11)

                if enemyinvasionchance in [1, 2, 3, 4]:
                    print("The %s evaded your attack! " % activeenemy.name)
                    while True:
                        a = input("Press enter to continue...")
                        if a == '':
                            clear_screen()
                            sleep(.5)
                            break
                    return

                else:

                    if attackchoice == playeractiveweapon.a1n:

                        if playerenergy - playeractiveweapon.a1e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a1e
                            attackamount = random.randrange(playeractiveweapon.a1dmin, playeractiveweapon.a1dmax)

                            if playeractiveweapon.a1ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a1ef == 'critical':
                                player.criticalchance += playeractiveweapon.a1cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a1ef == 'poison':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a2n:

                        if playerenergy - playeractiveweapon.a2e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a2e
                            attackamount = random.randrange(playeractiveweapon.a2dmin, playeractiveweapon.a2dmax)

                            if playeractiveweapon.a2ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a2ef == 'critical':
                                player.criticalchance += playeractiveweapon.a2cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a2ef == 'posion':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a1n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (
                        playeractiveweapon.a1n, playeractiveweapon.a1dmin,
                        playeractiveweapon.a1dmax, playeractiveweapon.a1e,
                        playeractiveweapon.a1ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break


                    elif attackchoice == playeractiveweapon.a2n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (
                        playeractiveweapon.a2n, playeractiveweapon.a2dmin,
                        playeractiveweapon.a2dmax, playeractiveweapon.a2e,
                        playeractiveweapon.a2ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break

                    else:
                        continue

            elif activeenemy.dif is "difficult":
                enemyinvasionchance = random.randrange(activeenemy.evasionchance, 11)

                if enemyinvasionchance in [1, 2, 3, 4, 5]:
                    print("The %s evaded your attack! " % activeenemy.name)
                    while True:
                        a = input("Press enter to continue...")
                        if a == '':
                            clear_screen()
                            sleep(.5)
                            break
                    return

                else:

                    if attackchoice == playeractiveweapon.a1n:

                        if playerenergy - playeractiveweapon.a1e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a1e
                            attackamount = random.randrange(playeractiveweapon.a1dmin, playeractiveweapon.a1dmax)

                            if playeractiveweapon.a1ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a1ef == 'critical':
                                player.criticalchance += playeractiveweapon.a1cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a1ef == 'poison':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a2n:

                        if playerenergy - playeractiveweapon.a2e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a2e
                            attackamount = random.randrange(playeractiveweapon.a2dmin, playeractiveweapon.a2dmax)

                            if playeractiveweapon.a2ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a2ef == 'critical':
                                player.criticalchance += playeractiveweapon.a2cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a2ef == 'posion':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a1n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (
                        playeractiveweapon.a1n, playeractiveweapon.a1dmin,
                        playeractiveweapon.a1dmax, playeractiveweapon.a1e,
                        playeractiveweapon.a1ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break


                    elif attackchoice == playeractiveweapon.a2n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (
                        playeractiveweapon.a2n, playeractiveweapon.a2dmin,
                        playeractiveweapon.a2dmax, playeractiveweapon.a2e,
                        playeractiveweapon.a2ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break

                    else:
                        continue

            elif activeenemy.dif is "legendary":
                enemyinvasionchance = random.randrange(activeenemy.evasionchance, 11)

                if enemyinvasionchance in [1, 2, 3, 4, 5, 6]:
                    print("The %s evaded your attack! " % activeenemy.name)
                    while True:
                        a = input("Press enter to continue...")
                        if a == '':
                            clear_screen()
                            sleep(.5)
                            break
                    return

                else:

                    if attackchoice == playeractiveweapon.a1n:

                        if playerenergy - playeractiveweapon.a1e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a1e
                            attackamount = random.randrange(playeractiveweapon.a1dmin, playeractiveweapon.a1dmax)

                            if playeractiveweapon.a1ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a1ef == 'critical':
                                player.criticalchance += playeractiveweapon.a1cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a1ef == 'poison':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a2n:

                        if playerenergy - playeractiveweapon.a2e < 0:

                            print("You don't have enough energy for that attack! ")
                            continue

                        else:

                            playerenergy -= playeractiveweapon.a2e
                            attackamount = random.randrange(playeractiveweapon.a2dmin, playeractiveweapon.a2dmax)

                            if playeractiveweapon.a2ef is None:

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a2ef == 'critical':
                                player.criticalchance += playeractiveweapon.a2cp

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                    criticalattack, activeenemy.name))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return

                            if playeractiveweapon.a2ef == 'posion':

                                criticalattackchance = random.randrange(player.criticalchance, 11)

                                if criticalattackchance in [1, 2, 3, 4, 5, 6, 7]:
                                    print("You attacked the %s, dealing %s damage! " % (activeenemy.name, attackamount))
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    activeenemy.health -= attackamount
                                    return

                                if criticalattackchance in [8, 9, 10]:
                                    criticalattack = attackamount * 2
                                    print("You dealt a critical attack, dealing %s damage to %s! " % (
                                        criticalattack, activeenemy.name))
                                    print("You inflicted poison on the %s! " % activeenemy.name)
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    isenemypoison = True
                                    enemypoisonturn = 3
                                    while True:
                                        a = input("Press enter to continue...")
                                        if a == '':
                                            clear_screen()
                                            sleep(.5)
                                            break
                                    activeenemy.health -= criticalattack
                                    return


                    elif attackchoice == playeractiveweapon.a1n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (
                        playeractiveweapon.a1n, playeractiveweapon.a1dmin,
                        playeractiveweapon.a1dmax, playeractiveweapon.a1e,
                        playeractiveweapon.a1ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break


                    elif attackchoice == playeractiveweapon.a2n + 'info':
                        print("%s, %s - %s damage, %s energy, %s effect " % (
                        playeractiveweapon.a2n, playeractiveweapon.a2dmin,
                        playeractiveweapon.a2dmax, playeractiveweapon.a2e,
                        playeractiveweapon.a2ef))
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break

                    else:
                        continue


        elif attack == 'item':
            seeinventory()
            if cycle is True:
                cycle = False
                continue
            if cycle is False:
                useitem(player)


        elif attack == 'escape':
            escapechance = random.randrange(player.escapechance, 11)


            if escapechance in [1, 2, 3, 4, 5, 6, 7]:
                print("Your escape chance failed! ")
                while True:
                    a = input("Press enter to continue...")
                    if a == '':
                        clear_screen()
                        sleep(.5)
                        break
                return

            if escapechance in [8, 9, 10]:
                print("You have escaped from the battle! ")
                while True:
                    a = input("Press enter to continue...")
                    if a == '':
                        clear_screen()
                        sleep(.5)
                        break
                escape = True
                return


        elif attack == 'override':
            override = True
            return


def seeinventory():

    global inventory
    global inventorysee
    global cycle

    loopnum = len(inventory)
    if loopnum is 0:
        print("Your inventory is empty!")
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        cycle = True
        return

    i = 0
    while True:

        itemcount = inventory.count(inventory[i])

        if (("%s " + "%s ") % (itemcount, inventory[i])) in inventorysee:
            i += 1
            if i == loopnum:
                break
            else:
                continue

        inventorysee.append(("%s " + "%s ") % (itemcount, inventory[i]))
        i += 1
        if i == loopnum:
            break
        else:
            continue

    print(inventorysee)
    return


def battle():

    global isenemydeath
    global escape

    print("A %s has entered the battle! " % activeenemy.name)
    while True:
        a = input("Press enter to continue...")
        if a == '':
            clear_screen()
            sleep(.5)
            break

    while True:

        if isplayerpoison is True:
            poison(player)


        if isplayerrage is True:
            rage(player)


        playerattack(player)

        if override is True:
            return

        elif override is False:
            pass

        if escape is True:
            return
        if escape is False:
            pass

        checkenemyhealth(activeenemy)

        if activeenemy.health <= 0:
            activeenemy.health = activeenemy.maxhealth
            loot()
            return

        if activeenemy.health > 0:
            enemyattack(activeenemy)
            continue


def menu():

    global playerlocation
    global activequest
    global playergold

    if town is True:

        while True:
            clear_screen()
            sleep(.5)
            print("Current location: %s" % playerlocation)
            print("\n" * 0)
            print("Health: %s" % player.health)
            print("\n" * 0)
            print("Equipped Weapon: %s" % playeractiveweapon.name)
            print("\n" * 0)
            print("Equipped Armor: %s" % playeractivearmor)
            print("\n" * 0)
            print("Active Quest: %s" % activequestname)
            print("\n" * 0)
            print("Gold: %s" % playergold)
            print("\n" * 1)

            menuchoice = str.lower(input("Travel, Shop, Quests or Change Equipment? "))

            if menuchoice == 'travel':

                while True:
                    clear_screen()
                    sleep(.5)
                    i = 0
                    while True:
                        if i == len(location):
                            break
                        print(location[i])
                        i += 1
                    locationfind = location.index(playerlocation)

                    print("\n" * 0)

                    movechoice = str.title(input("Travel to which location? (%s, %s)" % (location[locationfind + 1],
                                                                                       location[locationfind - 1])))

                    if movechoice == location[locationfind + 1]:
                        playerlocation = movechoice
                        clear_screen()
                        sleep(.5)
                        print("You are traveling to %s..." % playerlocation)
                        sleep(2)

                        travelattack = random.randrange(1, 11)

                        if travelattack in [1, 2, 3, 4, 5]:

                            randomenemyselection = random.choice(travelenemies)
                            clear_screen()
                            sleep(.5)
                            print("You were unlucky on your journey, and ran into a %s! " % randomenemyselection.name)
                            while True:
                                a = input("Press enter to continue...")
                                if a == '':
                                    clear_screen()
                                    sleep(.5)
                                    break
                            activeenemy = randomenemyselection
                            battle()
                            return


                        if travelattack in [6, 7, 8, 9, 10]:
                            clear_screen()
                            sleep(.5)
                            return

                    elif movechoice == location[locationfind - 1]:
                        playerlocation = movechoice
                        clear_screen()
                        sleep(.5)
                        print("You are traveling to %s..." % playerlocation)
                        sleep(2)

                        travelattack = random.randrange(1, 11)

                        if travelattack in [1, 2, 3, 4, 5]:

                            randomenemyselection = random.choice(travelenemies)
                            clear_screen()
                            sleep(.5)
                            print("You were unlucky on your journey, and ran into a %s! " % randomenemyselection.name)
                            while True:
                                a = input("Press enter to continue...")
                                if a == '':
                                    clear_screen()
                                    sleep(.5)
                                    break
                            activeenemy = randomenemyselection
                            battle()
                            return


                        if travelattack in [6, 7, 8, 9, 10]:
                            clear_screen()
                            sleep(.5)
                            return

                    elif movechoice in location:
                        clear_screen()
                        sleep(.5)
                        print("You can't reach %s from here! " % movechoice)
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break
                        continue

                    else:
                        clear_screen()
                        sleep(.5)
                        print("That place does not exist! ")
                        while True:
                            a = input("Press enter to continue...")
                            if a == '':
                                clear_screen()
                                sleep(.5)
                                break
                        continue

            if menuchoice == 'shop':
                pass

            if menuchoice == 'quests':
                clear_screen()
                sleep(.5)
                quest()

            if menuchoice == 'change equipment':
                pass


def q1():

    global playerlocation
    global questlocation
    global activeenemy

    questlocation = "Grand Castle"
    activequest = "q1"

    while True:

        if playerlocation == questlocation:
            print("As you reach the castle, you start to hear yelling from inside the village")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            print("You quickly run inside, only to meet a bandit who is terrorizing the small town")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break
            activeenemy = bandit
            battle()

            print("The defeated bandit falls, leaving the village to cheer you on ")



        if playerlocation != questlocation:
            clear_screen()
            sleep(.5)
            if cycle is False:
                print("For this quest, you need to travel to %s! " % questlocation)
                questcycle = True
                while True:
                    a = input("Press enter to continue...")
                    if a == '':
                        break
                menu()
                continue
            if cycle is True:
                clear_screen()
                sleep(.5)
                menu()


#QUESTS
questlist = []
questsrun = {"Find A Way To The Castle" : q1,
             }

def quest():

    while True:

        print(questlist)
        choice = str.title(input("Which quest? "))

        if choice in questlist:
            activequestname = choice
            questsrun[choice]()

        if choice not in questlist:
            clear_screen()
            sleep(.5)
            print("That's not a quest! ")
            while True:
                a = input("Press enter to continue...")
                if a == '':
                    clear_screen()
                    sleep(.5)
                    break


#START
while True:
    sleep(.5)
    print("Welcome Player! ")
    while True:
        a = input("Press enter to continue...")
        if a == '':
            clear_screen()
            sleep(.5)
            break
    pickname = (input("What is your character's name? "))

    if pickname == '':
        print("Are you sure that's your name? ")
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        continue

    else:
        clear_screen()
        sleep(.4)
        player.name = pickname
        print("Hello, %s! " % player.name)
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
    break

print("As your journey starts, you find your hero awakening in a dark and eerie cave, knowing little to nothing of how"
      "\nthey became there")
while True:
    a = input("Press enter to continue...")
    if a == '':
        clear_screen()
        sleep(.5)
        break

while True:

    print("Knight - Hp: 300, Energy: 25,Carry: 30, Class Bonus: Shields increase defense by 10% more"
          "\nStarts with: Iron Sword, Iron Armor")
    print("\n" * 0)
    print("Warrior - Hp: 400, Energy: 30, Carry: 35, Class Bonus: Rage Potion's affects increase damage by 20% more"
          "\nStarts with: Iron Axe, Leather Armor,")
    print("\n" * 0)
    print("Mage - Hp: 250, Energy: 45, Carry: 25, Class Bonus: Magic weapons deal 30% more damage"
              "\n Starts with: Mage's Staff, Magic Robe")
    print("\n" * 0)
    print("Hunter - Hp: 250, Energy: 40, Carry: 20, Class Bonus: Long Ranged weapons deal 20% more damage"
              "\n Starts with: Standard Bow, Hunter's Cloak")
    print("\n" * 0)
    print("Rogue - Hp: 250, Energy: 30, Carry: 25, Class Bonus: Evasion chance increased by 40%"
              "\n Starts with: Dagger, Stealth Cloak")
    print("\n" * 1)

    classpick = str.lower(input("What do you remember? (Choose a class)"))

    if classpick == 'knight':
        clear_screen()
        sleep(.5)
        print("You have chosen the Knight class! ")
        playerclass = 'knight'
        inventory.append("Iron Armor")
        inventory.append("Iron Sword")
        armorstrength = .4
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break

        break

    elif classpick == 'warrior':
        clear_screen()
        sleep(.5)
        print("You have chosen the Warrior class! ")
        playerclass = 'warrior'
        player.rageeffect += .2
        inventory.append("Iron Axe")
        inventory.append("Leather Armor")
        armorstrength = .1
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        break

    elif classpick == 'hunter':
        clear_screen()
        sleep(.5)
        print("You have chosen the Hunter class! ")
        playerclass = 'hunter'
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        break

    elif classpick == 'rogue':
        clear_screen()
        sleep(.5)
        print("You have chosen the Rogue class! ")
        playerclass = 'rogue'
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        break

    elif classpick == 'mage':
        clear_screen()
        sleep(.5)
        print("You have chosen the Mage class! ")
        playerclass = 'mage'
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        break

    else:
        clear_screen()
        sleep(.5)
        print("Not a valid input! ")
        while True:
            a = input("Press enter to continue...")
            if a == '':
                clear_screen()
                sleep(.5)
                break
        continue

print("Regaining your strength, you stumble out of the cave, and into the blinding light")
while True:
    a = input("Press enter to continue...")
    if a == '':
        clear_screen()
        sleep(.5)
        break
print("Taking a look around you, you see a stone castle with what looks like a large wall \nand a village inside")
while True:
    a = input("Press enter to continue...")
    if a == '':
        clear_screen()
        sleep(.5)
        break
print("Quest log updated! ")
questlist.append("Find A Way To The Castle")
while True:
    a = input("Press enter to continue...")
    if a == '':
        break
menu()
