# #ვისი სახელიც "ი"-ზე მთავრდება, დაუპრინტეთ გვერდით "cool"

import random

squad=["dato mgeladze","vano motiashvili","davit janashia","aleqsandre katsarava","lasha wamalaidze","ilia wiklauri","nini nozadze","nika chochia","gabriel gogadze","sandro bochorishvili","dato jachvadze","giorgi gelashvili","muhammedali mamedov","sandro oqropiridze","erekle gochitashvili"]

choice1 = random.choice(squad)
choice2 = random.choice(squad)
choice3 = random.choice(squad)
        
if choice1[-1] == "i":
    print(choice1 , "cool")
else:
    print(choice1)

if choice2[-1] == "i":
    print(choice2 , "cool")
else:
    print(choice2)

if choice3[-1] == "i":
    print(choice3 , "cool")
else:
    print(choice3)



    


    
