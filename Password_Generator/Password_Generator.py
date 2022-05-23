import random

word = "chicken" "turkey" "pig" "rice" "lettuce" "demon" "slayer" "youtube" "bug" "insect" "flame" "water" "sound" "beast" "lightning"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "@#$%^&*"

all = word + lower + upper + number + symbol

length = 22

password = "".join(random.sample(all,length))



print("Hello! Welcome to Bill's Super Awesome password generator 1.0.")
print("Whats you name so i can get you started with your brand new super secure password!")

name = input()

print("Hi " + " " + name + " " + " Don't worry if you can't remeber it ! Just come on back and i'll make you a new one!")


print("Your one-time generated password is : " + password)



