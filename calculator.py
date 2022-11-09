import math

def tangent(degree):
    if degree == 90 or degree == 270 or degree == -90 or degree == -270:
        tangent = "Undefined"
    elif degree == 45 or degree == 225:
        tangent = 1.0
    elif degree == -45 or degree == -225:
        tangent = -1.0
    else:
        tangent = math.tan(math.radians(degree))
    return tangent

def cotangent(degree):
    if degree == 0 or degree == 180 or degree == 360 or degree == -180 or degree == 90 or degree == 270 or degree == -90 or degree == -270:
        cotangent = "Undefined"
    else:
        cotangent = 1 / tangent(degree)
    return cotangent

def sinus(degree):
    if degree == 0 or degree == 180 or degree == -180:
        sinus = 0.0
    else:
        sinus = math.sin(math.radians(degree))
    return sinus

def cosine(degree):
    if degree == 90 or degree == 270 or degree == -90 or degree == -270:
        cosine = 0.0
    else:
        cosine = math.cos(math.radians(degree))
    return cosine

def faktorial(number):
    if number < 0:
        return "Number cannot be less than zero!"
    else:
        faktorial = 1
        for i in range(2, (number+1)):
            faktorial *= i
        return faktorial

def percent(number, percent_number):
    if percent_number < 0:
        result = "Percent number cannot be less than zero!"
    else:
        result = number*percent_number/100
    return result

process_list = ["Look At The Menu", "Exit the Program", "Tangent", "Cotangent", "Sinus", "Cosine", "Cosecant", "Secant", "Logarithm", "Exponentiation", "Rooting", "Addition", "Subtraction", "Multiplication", "Dividing", "Mod", "Factorial", "Percent"]

menu = "*****************************************\n"
menu += "Select a Process;\n"
for i in range((len(process_list))):
    menu += "{} = {}\n".format((i-1), process_list[i])
menu += "******************************************\n"
print(menu)

while True:
    process = input("Proccess (-1 = Look at the menu again):")
    if process == "0": #Exit the Program
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[1]))
        break
    elif process == "1": #Tangent
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[2]))
        try:
            degree = float(input("Enter a degree:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("tan({}) = {}\n".format(degree, tangent(degree)))
    elif process == "2": #Cotangent
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[3]))
        try:
            degree = float(input("Enter a degree:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("cot({}) = {}\n".format(degree, cotangent(degree)))
    elif process == "3": #Sinus
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[4]))
        try:
            degree = float(input("Enter a degree:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("sin({}) = {}\n".format(degree, sinus(degree)))
    elif process == "4": #Cosine
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[5]))
        try:
            degree = float(input("Enter a degree:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("cos({}) = {}\n".format(degree, cosine(degree)))
    elif process == "5": #Cosecant
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[6]))
        try:
            degree = float(input("Enter a degree:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("cosec({}) = {}\n".format(degree, (1/sinus(degree))))
    elif process == "6": #Secant
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[7]))
        try:
            degree = float(input("Enter a degree:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("sec({}) = {}\n".format(degree, (1 / cosine(degree))))
    elif process == "7": #Logarithm
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[8]))
        try:
            base = int(input("Enter base:"))
            number = float(input("Enter number:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("log({}){} = {}\n".format(number, base, math.log(number, base)))
    elif process == "8": #Exponentiation
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[9]))
        try:
            number = float(input("Enter number:"))
            power = float(input("Enter power:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("{}^{} = {}\n".format(number, power, number**power))
    elif process == "9": #Rooting
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[10]))
        try:
            number = float(input("Enter number:"))
            root = int(input("Enter root:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("{}√{} = {}\n".format(root, number, number**(1/root)))
    elif process == "10": #Addition
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[11]))
        try:
            number_of_numbers = int(input("How many numbers will you enter?:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            addition = 0
            for i in range(1, (number_of_numbers+1)):
                try:
                    addition += float(input("Enter number {}:".format(i)))
                except ValueError:
                    print("This is not a number!\n")
                else:
                    if(i == number_of_numbers):
                        print("total value =", addition, "\n")
    elif process == "11": #Subtraction
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[12]))
        try:
            number1 = float(input("Enter number 1:"))
            number2 = float(input("Enter number 2:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("{} - {} = {}\n".format(number1, number2, number1-number2))
    elif process == "12": #Multiplication
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[13]))
        try:
            number_of_numbers = int(input("How many numbers will you enter?:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            multiplication = 1
            for i in range(1, (number_of_numbers + 1)):
                try:
                    multiplication *= float(input("Enter number {}:".format(i)))
                except ValueError:
                    print("This is not a number!\n")
                else:
                    if (i == number_of_numbers):
                        print("total value =",multiplication,"\n")
    elif process == "13": #Dividing
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[14]))
        try:
            number1 = float(input("Enter number 1:"))
            number2 = float(input("Enter number 2:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("{} / {} = {}\n".format(number1, number2, number1/number2))
    elif process == "14": #Mod
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[15]))
        try:
            number = float(input("Enter number:"))
            mod_number = float(input("Enter mod number:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("{} % {} = {}\n".format(number, mod_number, number % mod_number))
    elif process == "15": #Factorial
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[16]))
        try:
            number = int(input("Enter a number:"))
        except ValueError:
            print("This is not a number!\n")
        else:
            print("{}! = {}\n".format(number, faktorial(number)))
    elif process == "16": #Percent
        print("""
*****************************************
{}
*****************************************
        """.format(process_list[17]))
        try:
            number = float(input("Enter a number:"))
            percent_number = float(input("Enter percent number:"))
        except:
            print("This is not a number!\n")
        else:
            print("{}% of {} is {}".format(percent_number, number, percent(number, percent_number)))

    elif process == "-1": #Look At The Menu
        print(menu)
    else: #no key
        print("""
*****************************************
There Is No Such Key!
*****************************************
            """)