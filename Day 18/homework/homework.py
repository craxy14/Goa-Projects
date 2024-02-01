# 1)შეიქმნას რაზმის წევრების სია, ვისს სახელ და გვარში 2-ზე მეტი "ი" არის,გაუდიდდეს პირველი ასო და შევიდეს ახალ სიაში "supersia"


squad=['alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']

i_count = 0
supersia = []


for element in squad:
    i_count = 0
    for char in element:
        if char == "i":
            i_count += 1

    if i_count > 2:
        supersia.append(element.capitalize())


print(supersia)

