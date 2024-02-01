#2)თქვენი რაზმის წევრებიდან ვისი სახელი და გვარის სიგრძე ნაკლებია 16 სიმბოლოზე, გაუდიდდეს სახელი და გვარი და დაიპრინტოს გადიდებულად.


squad=["dato mgeladze","vano motiashvili","davit janashia","aleqsandre katsarava","lasha wamalaidze","ilia wiklauri","nini nozadze","nika chochia","gabriel gogadze","sandro bochorishvili","dato jachvadze","giorgi gelashvili","muhammedali mamedov","sandro oqropiridze","erekle gochitashvili"]

for element in squad:
    if len(element) < 16:
        print(element.upper()) 