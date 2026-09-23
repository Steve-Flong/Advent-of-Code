align = False
t = 0
while True:
    disc1_pos = ((t+1+1) % 17)
    if disc1_pos == 17:
        disc1_pos = 0
    disc2_pos = ((t+2) % 7)
    if disc2_pos == 7:
        disc1_pos = 0
    disc3_pos = ((t+3+2) % 19)
    if disc3_pos == 19:
        disc1_pos = 0
    disc4_pos = ((t+4) % 5)
    if disc4_pos == 5:
        disc1_pos = 0
    disc5_pos = ((t+5) % 3)
    if disc5_pos == 3:
        disc1_pos = 0
    disc6_pos = ((t+6+5) % 13)
    if disc6_pos == 13:
        disc1_pos = 0
    disc7_pos = ((t+7) % 11)
    if disc7_pos == 11:
        disc7_pos = 0
    if disc1_pos == disc2_pos == disc3_pos == disc4_pos == disc5_pos == disc6_pos == disc7_pos == 0:
        break
    t += 1
print(t)
