import random

choices = ['rock', 'paper', 'scissors']

index = random.randint(0, 2)
computers_choice = choices[index]

while True:
    your_choice = input('enter your choice ')
    if your_choice in choices:
        print(your_choice + ' is good')
        break
    else:
        print(your_choice + ' is not valid')

print('you=' + your_choice)
print('computer=' + computers_choice)

if your_choice == computers_choice:
    print("It's a draw")
elif your_choice == 'rock' and computers_choice == 'scissors':
    print("You win")
elif your_choice == 'scissors' and computers_choice == 'paper':
    print("You win")
elif your_choice == 'paper' and computers_choice == 'rock':
    print("You win")
else:
    print("You lose")


