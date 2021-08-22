#9.2 - Ostanek
choice = int(input("Choose a number between 1-100 "))

for num in range (1, choice+1):
    
    if num % 3 == 0 and num % 5 == 0:
        print("Deljivo s 3 in 5")
    elif num % 3 == 0:
        print("Deljivo s 3")
    elif num % 5 == 0:
        print("Deljivo s 5")
    else:
        print(num)


#9.3 - Make string lowercase
string1 = input("Please enter a string: ")
string2 = input("Please add another string: ")
x = (f"{string1} {string2}").lower()
print(x)

