"""
File name: Menu.py
Author : Jamal Hamid (c3508783)
Imported Files :
Imported libraries:
Date Modifed : 26/3/2026
Date Created : 26/3/2026

Desciption : The menu for the program
"""
# TODO create the menu for the main program

def Menu ():
    print("__________________________________________\n\n")
    print(" 1 | Load data / Import file")
    print(" 2 | Save data / Output file")
    print(" 3 | Select DES00")
    print(" 4 | Select DES01")
    print(" 5 | Select DES02")
    print(" 6 | Select DES03")
    print(" 7 | Analysing data")
    print(" 8 | Testing mode")
    print(" 9 | Display current data mode")
    print(" 10 | Exit ...\n")

    print("__________________________________________\n")
    
    option = input("Please select an option \n").lower()
    match option:
        case "1" | "one":
            print("Load data\n")
        case "2" | "two":
            print("Saving data\n")
        case "3" | "three":
            print("Selected DES00\n")
        case "4" | "four":
            print("Selected DES01\n")
        case "5" | "five":
            print("Selected DES02\n")
        case "6" | "six":
            print("Selected DES03\n")
        case "7" | "seven":
            print("Analysing data\n")
        case "8" | "eight":
            print("Testing mode\n")
        case "9" | "nine":
            print("Display current data / mode\n")
        case "10" | "eight":
            print("Exit ...\n")
            
def AnalysisMenu():
    print("__________________________________________\n\n")
    print(" 1 | Avalanche analysis")
    print(" 2 | Bit analysis")
    print(" 3 | Data comparison")
    print(" 4 | Exit ...\n")

    print("__________________________________________\n")
    
    option = input("Please select an option \n").lower()
    
    match option:
        case "1" | "one":
            print("Avalanche method analysing ...\n")
        case "2" | "two":
            print("Bit comparison analysing ...\n")
        case "3" | "three":
            print("Data comparison showing ...\n")
        case "4" | "four":
            print("Exit ...\n")

AnalysisMenu()