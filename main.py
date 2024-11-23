import random as rnd

def createFile():
  with open('CoinFlip.csv', 'w+') as file:
    file.write('Mode,Strategy,Human Choice,Computer Choice,Coin,Outcome\n')

createFile()

def coin_flip():
  return rnd.choice(['Heads', 'Tails'])

mode = input('Enter \'1\' for single player, \'2\' for multiplayer, \'3\' for simulation & anaylytics: ')
  
if mode == '1': #singleplayer
    
  guess = input('Guess the coin flip - Heads or Tails: ')
  
  result = coin_flip()
  
  print(f'The coin flip result is: {result}')
  
  if guess.lower() == result.lower():
    print('Congratulations! You win!')
    
  else:
    print('Sorry, you lost.')
    
elif mode == '2': #multiplayer
    
  p1 = input('Player 1, enter your name: ')
  p2 = input('Player 2, enter your name: ')
  
  guess1 = input(f'{p1}, guess the coin flip - Heads or Tails: ')
  guess2 = input(f'{p2}, guess the coin flip - Heads or Tails: ')
  
  result = coin_flip()
  print(f'The coin flip result is: {result}')
  
  if guess1.lower() == result.lower() and guess2.lower() != result.lower():
     print(f'Congratulations, {p1}! You win!')
    
  elif guess1.lower() != result.lower() and guess2.lower() == result.lower():
    print(f'Congratulations, {p2}! You win!')
    
  else:
    print('It is a tie!')

elif mode == '3': #simulation and anyalitics
    
  coinFlip = ['heads','tails']
  for i in range(100):
    human = 'tails'
    computer = rnd.choice(coinFlip)
    Coin = rnd.choice(coinFlip)

    if human == Coin and computer == Coin:
      outcome = 'Draw'
    elif human == Coin and computer != Coin:
      outcome = 'Win'
    else:
      outcome = 'Lose'
    
    with open('CoinFlip.csv', 'a+') as file:
      file.write('Simulation,Tails,'+human+','+computer+','+Coin+','+outcome+'\n')

  for i in range(100):
    human = coin_flip()
    computer = coin_flip()
    Coin = coin_flip()

    if human == Coin and computer == Coin:
      outcome = 'Draw'
    elif human == Coin and computer != Coin:
      outcome = 'Win'
    else:
      outcome = 'Lose'
      
    with open('CoinFlip.csv', 'a+') as file:
      file.write('Simulation,Random,'+human+','+computer+','+Coin+','+outcome+'\n')
  
  import pandas as pd 
  
  data_frame = pd.read_csv('CoinFlip.csv')
  print(data_frame['Strategy'])
  random_data = data_frame.loc[data_frame['Strategy'] == 'Random']
  tails_data = data_frame.loc[data_frame['Strategy'] == 'Tails']

  print('Random')
  print(random_data.value_counts('Outcome'))
  print()
  print('Tails')
  print(tails_data.value_counts('Outcome'))

  import matplotlib.pyplot as plt
  while True:
    plt.bar(random_data.value_counts('Outcome').index, random_data.value_counts('Outcome'))
    plt.title('Random Strategy')
    plt.show(block = False)
    plt.pause(20)
    plt.clf()
    plt.bar(tails_data.value_counts('Outcome').index, tails_data.value_counts('Outcome'))
    plt.title('Tails Strategy')
    plt.show(block = False)
    plt.pause(20)
    plt.clf()