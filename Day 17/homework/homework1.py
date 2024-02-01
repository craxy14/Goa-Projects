#კოდი გადააკეთეთ ისე, რომ ერთმა ბავშვმა რამოდენიმეჯერ ვეღარ მოიგოს

import random 

crew_leaders = ['kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze']


choice1 = random.choice(crew_leaders)

choice2 = random.choice(crew_leaders)

choice3 = random.choice(crew_leaders)

while choice1 == choice2 or choice1 == choice3 or choice3 == choice2:
    choice1 = random.choice(crew_leaders)
    choice2 = random.choice(crew_leaders)
    choice3 = random.choice(crew_leaders)

print('winner N1 :' , choice1)
print('winner N2 :' , choice2)
print('winner N3 :' , choice3)