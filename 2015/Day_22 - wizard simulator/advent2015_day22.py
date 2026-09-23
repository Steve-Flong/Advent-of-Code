import random

def play_game():
    spells = {
        "Magic Missile": {"cost": 53, "damage": 4, "count": 0, "heal": 0, "armor": 0, "recharge": 0, "effect": False,
                          "current": False},
        "Drain": {"cost": 73, "damage": 2, "count": 0, "heal": 2, "armor": 0, "recharge": 0, "effect": False,
                  "current": False},
        "Shield": {"cost": 113, "damage": 0, "count": 6, "heal": 0, "armor": 7, "recharge": 0, "effect": True,
                   "current": False},
        "Poison": {"cost": 173, "damage": 3, "count": 6, "heal": 0, "armor": 0, "recharge": 0, "effect": True,
                   "current": False},
        "Recharge": {"cost": 229, "damage": 0, "count": 5, "heal": 0, "armor": 0, "recharge": 101, "effect": True,
                     "current": False}}
    player = {"hit points": 50, "armor": 0, "mana": 500, "total_spend": 0}
    boss = {"hit points": 71, "damage": 10}

    def check_current_spells():
        for i in spells:
            if spells[i]["current"]:
                if i == "Shield":
                    spells[i]["count"] -= 1
                    #print(spells_update(i, spells[i]["count"]))
                    if spells[i]["count"] > 0:
                        player["armor"] = 7
                    else:
                        #print(spells_finished(i))
                        spells[i]["current"] = False
                        spells[i]["count"] = 6
                        player["armor"] = 0
                else:
                    boss["hit points"] -= spells[i]["damage"]
                    player["mana"] += spells[i]["recharge"]
                    spells[i]["count"] -= 1
                    #print(spells_update(i, spells[i]["count"]))
                    if spells[i]["count"] == 0:
                        spells[i]["current"] = False
                        if i == "Poison":
                            spells[i]["count"] = 6
                        if i == "Recharge":
                            spells[i]["count"] = 5
                        #print(spells_finished(i))

    def spells_update(spell, timer):
        update = {"Shield": "Shield's timer is now {}.".format(timer),
                  "Poison": "Poison deals 3 damage; its timer is now {}.".format(timer),
                  "Recharge": "Recharge provides 101 mana; its timer is now {}.".format(timer)}
        return update[spell]

    def spells_finished(spell):
        finish = {"Shield": "Shield wears off, decreasing armor by 7.",
                  "Poison": "Poison wears off.",
                  "Recharge": "Recharge wears off."}
        return finish[spell]

    def spells_cast(spell):
        cast = {"Shield": "Player casts Shield, increasing armor by 7.",
                "Poison": "Player casts Poison",
                "Magic Missile": "Player casts Magic Missile, dealing 4 damage.",
                "Recharge": "Player casts Recharge.",
                "Drain": "Player casts Drain, dealing 2 damage, and healing 2 hit points."}
        return cast[spell]

    def cast_spell():
        avail_spells = [spell for spell in spells if
                        spells[spell]["current"] is False and spells[spell]["cost"] < player["mana"]]
        #print("Available spells are ....", list(avail_spells))
        # answer = input("Do you want to pick? y/n")
        # if answer =="n":
        #     x = random.randint(0, len(avail_spells)-1)
        #     spell_to_cast = avail_spells[x]
        # else:
        #     select = input("Select number relative to list")
        #     spell_to_cast = avail_spells[int(select)]
        if len(avail_spells) > 1:
            x = random.randint(0, len(avail_spells) - 1)
        elif len(avail_spells) == 1:
            x = 0
        elif len(avail_spells) == 0:
            return
        spell_to_cast = avail_spells[x]
        list_of_spells.append(spell_to_cast)
        player["mana"] -= spells[spell_to_cast]["cost"]
        player["total_spend"] += spells[spell_to_cast]["cost"]
        #print(spells_cast(spell_to_cast))
        if spells[spell_to_cast]["effect"]:
            spells[spell_to_cast]["current"] = True
            if spell_to_cast == "Shield":
                player["armor"] = 7
        else:
            boss["hit points"] -= spells[spell_to_cast]["damage"]
            player["hit points"] += spells[spell_to_cast]["heal"]

    def check_points():
        if player["mana"] < 53:
            #print("You have run out of mana, Boss wins!!!")
            return "Boss"
        elif player["hit points"] <= 0:
            #print("You have died, Boss wins!!")
            return "Boss"
        elif boss["hit points"] <= 0:
            #print("The Boss is dead, you win!!")
            return "Player"
        else:
            return None
    def boss_attack():
        if player["armor"] == 0:
            damage = boss["damage"]
            player["hit points"] -= boss["damage"]
        else:
            damage = 3
            player["hit points"] -= 3
        #print("Boss attacks for {} damage".format(damage))


    while player["hit points"] > 0 and boss["hit points"] > 0:
        # print("\n-- Player turn --")
        # print("- Player has {} hit points, {} armor, {} mana, {} total spent".format(player["hit points"],
        #                                                              player["armor"], player["mana"],
        #                                                                              player["total_spend"]))
        # print("- Boss has {} hit points".format(boss["hit points"]))
        player["hit points"] -= 1
        if player["hit points"] == 0:
            return "Boss", player["total_spend"]
        check_current_spells()
        x = check_points()
        if x is not None:
            return x, player["total_spend"]
        cast_spell()
        if player["hit points"] <= 0:
            #print("You have died, Boss wins!!")
            return "Boss", player["total_spend"]
        elif boss["hit points"] <= 0:
            #print("The Boss is dead, you win!!")
            return "Player", player["total_spend"]
        # print("\n-- Boss turn --")
        # print("- Player has {} hit points, {} armor, {} mana, {} total spent".format(player["hit points"],
        #                                                                              player["armor"], player["mana"],
        #                                                                              player["total_spend"]))
        # print("- Boss has {} hit points".format(boss["hit points"]))
        player["hit points"] -= 1
        if player["hit points"] == 0:
            return "Boss", player["total_spend"]
        check_current_spells()
        if player["hit points"] <= 0:
            #print("You have died, Boss wins!!")
            return "Boss", player["total_spend"]
        elif boss["hit points"] <= 0:
            #print("The Boss is dead, you win!!")
            return "Player", player["total_spend"]
        boss_attack()
        if player["hit points"] <= 0:
            #print("You have died, Boss wins!!")
            return "Boss", player["total_spend"]

#play_game()
min_spend = 100000
x = ""
while x != "Player":
    list_of_spells = []
    x, y = play_game()
    if x == "Player":
        print(y)
        break
        #print(list_of_spells)
        #break
        #min_spend = y
#print(min_spend)

