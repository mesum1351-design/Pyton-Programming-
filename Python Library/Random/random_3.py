import random
#%%
def result():
  return random.randint(0, 2)
#%%
def game():
  a = result()
  b = result()
  # 0 represents Rock, 1 represents Paper, 2 represents Scissor
  if a == b:
    print("Tie")
  elif a == 0 and b == 2:
    print("A is Rock and B is Scissor, A Won")
  elif a == 2 and b == 0:
    print("A is Scissor and B is Rock, B Won")
  elif a == 0 and b == 1:
    print("A is Rock and B is Paper, B Won")
  elif a == 1 and b == 0:
    print("A is Paper and B is Rock, A Won")
  elif a == 1 and b == 2:
    print("A is Paper and B is Scissor, B Won")
  else:
    print("A is Scissor and B is Paper, A Won")