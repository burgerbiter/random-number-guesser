import random
print("welcome to number guesser. you have three tries to do this.")
comp_num = random.randint(1,10)
tries = 3
won = False
play = True
while play == True:
  while won == False:
    while tries > 0:
      print()
      player_num=input("Enter a number between 1 and 10: ")
      player_num=float(player_num)
      if player_num<0 or player_num>10:
        print("bad number")
        break
      else:
        if player_num>comp_num:
          tries-=1
          print("too big. you have "+str(tries)+" tries left")
        elif player_num<comp_num:
          tries-=1
          print("too small. you have "+str(tries)+" tries left")
        else:
          print("You Guessed it!")
          won=True
          break
        