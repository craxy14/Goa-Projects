#შემოატანინეთ მომხმარებელს მისი და მამამისის ასაკი და თუ მამამისის ასაკი ორჯერ მეტია დაპრინტეთ Bingo თუარადა Mouse

user_age = int(input("Enter your age : "))
fathers_age = int(input("Enter your Fathers age : "))

if fathers_age == user_age *2:
    print("Bingo")
else:
    print("Mouse")