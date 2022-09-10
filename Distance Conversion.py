# This script allows users to convert units of distance

import time

def inchToCent():
    inch = input("Enter value in inches\n")
    centimetre = float(inch) * 2.54
    print(str(inch) + "in is " + str(centimetre) + " centimetres")
    messageDelay()
    exit()

def feetToMetre():
    feet = input("Enter value in feet\n")
    metre = float(feet) * 0.3048
    print(str(feet) + "ft is " + str(metre) + " metre")
    messageDelay()
    exit()    

def mileToKilometre():
    mile = input("Enter value in miles\n")
    kilometre = float(mile) * 1.609344
    print(str(mile) + "mi is " + str(kilometre) + " kilometres")
    messageDelay()
    exit() 

def fahrToCelsius():
    fahrenheit = input("Enter value in fahrenheit\n")
    celsius = (float(fahrenheit) - 32) * (5/9)
    print(str(fahrenheit) + "°f is " + str(celsius) + " °c")
    messageDelay()
    exit() 

def poundToKilogram():
    pound = input("Enter value in pounds\n")
    kilogram = float(pound) * 0.4535924
    print(str(pound) + "lb is " + str(kilogram) + " kilograms")
    messageDelay()
    exit()

def impToMet():
    print("1. Inches to Centimetres \n2. Feet to Metres \n3. Miles to Kilometres \n4. Fahrenheit to Celsius \n5. Pounds to Kilograms")
    answer = input()
    if answer == "1":
        inchToCent()
    if answer == "2":
        feetToMetre()
    if answer == "3":
        mileToKilometre()
    if answer == "4":
        fahrToCelsius()
    if answer == "5":
        poundToKilogram()

##############################
def centToInch():
    centimetre = input("Enter value in centimetres\n")
    inch = float(centimetre) * 0.39370
    print(str(centimetre) + "cm is " + str(inch) + '"')
    messageDelay()
    exit()  

def metreToFeet():
    metre = input("Enter value in metres\n")
    feet = float(metre) * 3.28
    print(str(metre) + "m is " + str(feet) + "'")
    messageDelay()
    exit()

def kilometreToMile():
    kilometre = input("Enter value in kilometres\n")
    mile = float(kilometre) * 0.6213712
    print(str(kilometre) + "km is " + str(mile) + " miles")
    messageDelay()
    exit()

def celsiusToFahr():
    celsius = input("Enter value in celsius\n")
    fahrenheit = float(celsius) * (9/5) + 32
    print(str(celsius) + "°c is " + str(fahrenheit) + "°f")
    messageDelay()
    exit()    

def kilogramToPound():
    kilogram = input("Enter value in kilograms\n")
    pound = float(kilogram) * 2.204623
    print(str(kilogram) + "kg is " + str(pound) + " pounds")
    messageDelay()
    exit() 

def metToImp():
    print("1. Centimetres to Inches \n2. Metres to Feet \n3. Kilometres to Miles \n4. Celsius to Fahrenheit \n5. Kilograms to Pounds")
    answer = input()
    if answer == "1":
        centToInch()
    if answer == "2":
        metreToFeet()
    if answer == "3":
        kilometreToMile()
    if answer == "4":
        celsiusToFahr()
    if answer == "5":
        kilogramToPound()
    
def messageDelay():
    time.sleep(60)
    return

def main():
    answer = input("1.Metric to Imperial\n2.Imperial to Metric\n")
    if answer == "1":
        metToImp()
    if answer == "2":
        impToMet()
    else:
        exit()

main()