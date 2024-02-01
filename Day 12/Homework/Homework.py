#შევქმათ სია ჩვენი სახელი და გვარისგან და დაპრინტეთ ხმოვნების რაოდენობა

full_name = "Vano Motiashvili"

vowel_count = 0

for i in range(len(full_name)):
    char = (full_name[i])
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vowel_count += 1      #vowel_count = vowel_count + 1 

print(vowel_count)