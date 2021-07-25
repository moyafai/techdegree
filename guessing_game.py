import random
secret_number = random.randrange(45)
tries = 1
welcome = ("Welcome to the game, the game of the geniuses people ")
print (welcome)
correct = " congratulation, you got the correct answer.See you soon with another challenge"
attemps = 1
guess=""
try:
    while guess != secret_number:
        guess = input("What do you think it is the right number? ")
        guess = int(guess)

        if guess > secret_number:
                print("it is lower, you treid {} times.".format(attemps))
                attemps += 1
        elif guess < secret_number:
                print ("it is higher, you tried {} times.".format(attemps))
                attemps += 1
except ValueError:
        print("invalid data entered, numbers only please!")
              
else:
                print( correct)
                
