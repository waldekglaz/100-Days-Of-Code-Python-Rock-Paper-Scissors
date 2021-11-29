import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

available_moves = [rock, paper, scissors]

cpu_move_index = random.randint(0, 2)
cpu_move = available_moves[cpu_move_index]

player_move_index = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

player_move = 0
if player_move_index >= 3 or player_move_index < 0:
    print("Invalid number. GAME OVER")
else:
    player_move = available_moves[player_move_index]

    if player_move_index == cpu_move_index:
        print(player_move)
        print("Computer chose:")
        print(cpu_move)
        print("Its a draw")
    elif player_move_index == 1 and cpu_move_index == 0:
        print(player_move)
        print("Computer chose:")
        print(cpu_move)
        print("You win")
    elif player_move_index == 0 and cpu_move_index == 2:
        print(player_move)
        print("Computer chose:")
        print(cpu_move)
        print("You win")
    elif player_move_index == 2 and cpu_move_index == 1:
        print(player_move)
        print("Computer chose:")
        print(cpu_move)
        print("You win")
    else:
        print(player_move)
        print("Computer chose:")
        print(cpu_move)
        print("You lose")
