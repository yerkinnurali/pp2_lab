import random
def guess():
 name=input("Hello! What is your name?")
 print(f"Well,{name}, I am thinking of a number between 1 and 20.")
 rand=random.randint(1,20)
 i=0
 while True:
  try:
    number = int(input("Take a guess."))
    if rand>number:
     print("Your guess is too low.")
     i=i+1
    elif rand<number:
     print("Your guess is too high.")
     i=i+1
    elif rand==number:
        print(f"Good job,{name}! You guessed my number in {i+1} guesses!")
        break
  except:print("Input int please")


guess()