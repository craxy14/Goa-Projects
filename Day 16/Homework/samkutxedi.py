#შექმენით ფუნქცია რომელსაც გადაეცემა სამკუთხედის სამი გვერდი, და დაპრინტავს მის პერიმეტრს
 
# gverdi1 = int(input("gverdi 1 : "))
# gverdi2 = int(input("gverdi 2 : "))
# gverdi3 = int(input("gverdi 3 : "))

# def samkutxedi(gverdi1 , gverdi2 , gverdi3):
#     print("samkutxedis perimetria :" , gverdi1 + gverdi2 + gverdi3)

# samkutxedi(gverdi1 , gverdi2 , gverdi3)    


side1 = int(input("side 1 : "))
side2 = int(input("side 2 : "))
side3 = int(input("side 3 : "))

def triangle(any_side1 , any_side2 , any_side3):
    print("perimeter of a triangle = " , any_side1 + any_side2 + any_side3)

triangle(side1 , side2 , side3)