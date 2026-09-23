def play_game(player_hit, boss_hit, boss_damage, boss_armour, player_damage=0, player_armour=0):
    while player_hit > 0 and boss_hit > 0:
        if player_damage > boss_armour:
            boss_hit -= player_damage - boss_armour
        else:
            boss_hit -= 1
        if boss_hit <= 0:
            continue
        if boss_damage > player_armour:
            player_hit -= boss_damage - player_armour
        else:
            player_hit -= 1
    if boss_hit <= 0:
        return "player"
    else:
        return "boss"


def main():
    player_hit = 100
    boss_hit = 100
    boss_damage = 8
    boss_armour = 2
    min_cost = 1000
    max_cost = 0
    weapons = {"Dagger": {"Cost": 8, "Damage": 4, "Armor": 0
                          },
               "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0
                              },
               "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0
                             },
               "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0
                             },
               "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0
                            }}
    armor = {"None": {"Cost": 0, "Damage": 0, "Armor": 0
                      },
             "Leather": {"Cost": 13, "Damage": 0, "Armor": 1
                         },
             "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2
                           },
             "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3
                            },
             "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4
                            },
             "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5
                           }}
    rings = {"None": {"Cost": 0, "Damage": 0, "Armor": 0
                      },
             "None2": {"Cost": 0, "Damage": 0, "Armor": 0
                       },
             "Defence +1": {"Cost": 20, "Damage": 0, "Armor": 1
                            },
             "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0
                           },
             "Defence +2": {"Cost": 40, "Damage": 0, "Armor": 2
                            },
             "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0
                           },
             "Defence +3": {"Cost": 80, "Damage": 0, "Armor": 3
                            },
             "Damage + 3": {"Cost": 100, "Damage": 3, "Armor": 0
                            }}

    for i in weapons.keys():
        for j in armor.keys():
            for k in rings.keys():
                rest = rings.copy()
                rest.pop(k)
                for x in rest:

                    cost = weapons[i]["Cost"] + armor[j]["Cost"] + rings[k]["Cost"] + rings[x]["Cost"]

                    player_damage = weapons[i]["Damage"] + rings[k]["Damage"] + rings[x]["Damage"]
                    player_armour = armor[j]["Armor"] + rings[k]["Armor"] + rings[x]["Armor"]

                    winner = play_game(player_hit, boss_hit, boss_damage, boss_armour, player_damage, player_armour)
                    if winner == "player":
                        if cost < min_cost:
                            min_cost = cost
                    if winner == "boss":
                        if cost > max_cost:
                            max_cost = cost
    print(min_cost)
    print(max_cost)


if __name__ == "__main__":
    main()
