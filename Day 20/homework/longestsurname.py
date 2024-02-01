#3) თქვენი რაზმელების სიიდან, ტოპ 2 ყველაზე გრძელგვარიანი შეაგდეთ ახალ სიაში და დაპრინტეთ

squad=["dato mgeladze","vano motiashvili","davit janashia","aleqsandre katsarava","lasha wamalaidze","ilia wiklauri","nini nozadze","nika chochia","gabriel gogadze","sandro bochorishvili","dato jachvadze","giorgi gelashvili","muhammedali mamedov","sandro oqropiridze","erekle gochitashvili"]

squad2 = []

max_len = 0
for element in squad:
    if len(element) > max_len:
        max_len = len(element)
        res = element

squad2.append(res)
squad.remove(res)

max_len = 0
for element in squad:
    if len(element) > max_len:
        max_len = len(element)
        res = element

squad2.append(res)
print(squad2)

