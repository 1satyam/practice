# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import Counter


def player(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history)<3:
      return random.choice(['R','P','S'])
    
    counter_move={'R':'P','P':'S','S':'R'}
    
    RANDOM_RATE = 0.12

    chosen_move = None
    used_pattern = False

    ## pattern 
    last_moves=opponent_history[-3:]
    next_moves =[]
   
    for i in range(len(opponent_history) - 4):
      if opponent_history[i : i+3] == last_moves:
          next_moves.append(opponent_history[i+3])
    
    if len(next_moves): #>= 2:
      counts=Counter(next_moves)
      most_common_move = max(counts, key=counts.get)

      #if counts[most_common_move] > (len(next_moves) -counts[most_common_move] ):
      predicted_move = most_common_move
      chosen_move=counter_move[predicted_move]
      used_pattern = True

    
      
    #probability
    if chosen_move==None:
      freq_counts = Counter(opponent_history)
      most_likely_move = max(freq_counts, key=freq_counts.get)
      
      chosen_move=counter_move[most_likely_move]
    

    
    if not used_pattern and random.random() < RANDOM_RATE:
        return random.choice(['R', 'P', 'S'])

    return chosen_move




    

    
