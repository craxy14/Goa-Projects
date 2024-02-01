# რა ჩაფორმატდება თუ შევიტანთ - 4 ; 15 ; 8


inp1 = int(input("Enter number1 : "))   #4
inp2 = int(input("Enter number2 : "))   #15
inp3 = int(input("Enter number3 : "))   #8

SUM = 0


if inp1 % 2 == 1:
    SUM += inp1
if inp2 % 2 == 1:
    SUM += inp2 / 2
if inp3 % 2 == 1:
    SUM += inp3

print("The sum of numbers is {}".format(SUM))




#ANSWER = 7.5