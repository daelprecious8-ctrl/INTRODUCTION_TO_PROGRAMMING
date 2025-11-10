#Brute Force Attack
correct = "12345"

while True:
    guess = input("Enter password: ")
    if guess == correct:
        print("Access granted — welcome!")
        
    else:
        print("Wrong password. Try again.")
