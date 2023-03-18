import random

number_to_guess = []
for i in range(0, 6):
    n = random.randrange(1, 1000)
    number_to_guess.append(n)
    print(number_to_guess)

user_guess = []
correct_guess = []
while len(user_guess) < 6:
    user_input = input(f"Guess Next number or Enter Q to quit: ").lower()
    if user_input == "q":
        print("You just Quit the lottery")
        break

    if int(user_input) in user_guess:
        print(f"Sorry a user can not repeat a guess more than once {user_input} already existing")
        user_guess.append(int(user_input))
        user_guess.pop()
        print(user_guess)
    else:
        user_guess.append(int(user_input))
        print(user_guess)

    if int(user_input) in number_to_guess:
        correct_guess.append(int(user_input))

t = 0
for each_number in user_guess:
    if each_number in number_to_guess:
        t += 1

if t == 1:
    print(f'''
         "Sorry you have one leg {correct_guess}"
         users Guess    = {user_guess}
         Expected Guess = {number_to_guess} 
        ''')
elif t == 2:
    print(f'''
    Congratulation!!! You got 2 correctly {correct_guess} 
     users Guess = {user_guess}
      Expected Guess = {number_to_guess}
    ''')
elif t == 3:
    print(f'''
        Congratulation!!! You got 3 strikes correctly {correct_guess} 
         users Guess = {user_guess}
          Expected Guess = {number_to_guess}
        ''')
elif t == 4:
    print(f'''
            Congratulation!!! You got 4 strikes correctly {correct_guess} 
             users Guess = {user_guess}
              Expected Guess = {number_to_guess}
            ''')
elif t == 5:
    print(f'''
            Congratulation!!! You got 5 strikes correctly {correct_guess} 
             users Guess = {user_guess}
              Expected Guess = {number_to_guess}
            ''')
elif t == 6:
    print(f'''
            Congratulation JACKPOT !!! You got 6 strikes correctly {correct_guess} 
             users Guess = {user_guess}
              Expected Guess = {number_to_guess}
            ''')
