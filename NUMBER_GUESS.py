import random as rm

number = rm.randint(1,100)
active = True
counter = 0
number_attempts = 15

while active and counter < number_attempts:
  try:
    guess = int(input("Enter Value Between 1-100: "))
    counter+=1
    if guess > number:
      attempt = number_attempts-counter
      print(f"guess lower, attempt left {attempt}")
    elif guess < number:
      attempt = number_attempts-counter
      print(f"guess higher, attempt left {attempt}")
    elif guess == number:
      print(f"Correct Guess Congratulation ! The Number is {number} you guessed it on {counter} attempts")
      active = False

  except:
      print("Enter valid number!")

if counter == number_attempts and guess!=number:
      active = False
      print(f"Game Over! The Number is {number} You are Out of Attempts {counter}/{counter}")
