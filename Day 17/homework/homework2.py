#შექმენით თქვენი რაზმელებისგან სია, ამოირჩიეთ რენდომულად 3 ბავშვი და მიუწერეთ გვერდში "კარგად სწავლობს".


import random


squad=["dato mgeladze","vano motiashvili","davit janashia","aleqsandre katsarava","lasha wamalaidze","ilia wiklauri","nini nozadze","nika chochia","gabriel gogadze","sandro bochorishvili","dato jachvadze","giorgi gelashvili","muhammedali mamedov","sandro oqropiridze","erekle gochitashvili"]

for i in range(3):
    randomizer = random.choice(squad)
    print(randomizer , "kargad swavlobs")



