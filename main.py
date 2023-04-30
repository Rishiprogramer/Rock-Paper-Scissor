def computer_choice():
    ops = ["rock", "paper", "scissor"]
    import random
    random_number = random.randint(1, 1000000)
    print(random_number)
    for i in range(random_number):
        ch = "".join(random.choice(ops) )
    return ch

from colr import clor

print(clor.OKBLUE+f"\t\t\t\t\t\t\t\t\t\t\t\tWelcome to rock, paper, scissor  game\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
print(clor.OKBLUE+f"Choose your actor:\n1)Scissor\n2)Paper\n3)Rock")
try:
    ch = str(input(clor.OKBLUE+f"Enter your choice: "))
    ch = ch.lower()
    computer = computer_choice()
except ValueError:
    print(clor.FAIL+f"INVALID VALUE ENTERED")
    exit()
if ch != computer:
    if ch == "scissor" and computer == "rock":
        print(clor.FAIL+f"You lost \ncomputer choice:{computer} \nyour choice: {ch}")
    elif ch == "rock" and computer == "scissor":
        print(clor.OKGREEN+f"You win \ncomputer choice:{computer} \nyour choice: {ch}")
    elif ch == "paper" and computer == "rock":
        print(clor.OKGREEN+f"you win \ncomputer choice:{computer} \nyour choice: {ch}")
    elif ch == "scissor" and computer == "paper":
        print(clor.OKGREEN+f"You win \ncomputer choice:{computer} \nyour choice: {ch}")
    elif ch == "rock" and computer == "paper":
        print(clor.FAIL+f"you lost \ncomputer choice:{computer} \nyour choice: {ch}")
    elif ch == "paper" and computer == "scissor":
        print(clor.FAIL+f"You lost \ncomputer choice:{computer} \nyour choice: {ch}")
else:
    print(clor.OKBLUE+f"Tie \ncomputer choice:{computer} \nyour choice: {ch}")




