import random

def player(prev_opponent_play, opponent_history=[], play_order2freq={}):

    # Nested helper function with predicts the best next play by analyzing the last n play patterns and seeing which 
    # play is most likely to win
    def predictor (prediction, n):
        # Saves the last n plays and keeps track of the frequency of each play pattern
        play_order2freq[last_n] = play_order2freq.get(last_n, 0) + 1

        # Creating all potential plays
        last_n_minus1 = "".join(opponent_history[-(n-1):])
        potential_plays = [
            last_n_minus1 + "R",
            last_n_minus1 + "P",
            last_n_minus1 + "S",
        ]

        # Creating a dictionary, which only includes the potential plays and their frequency ignoring all other play orders
        potential_play_order2freq = {
            k: play_order2freq[k]
            for k in potential_plays if k in play_order2freq
        }

        # As we might not have seen this play pattern before, the dictionary might be empty.
        # If it is not empty, find the play pattern that the opponent uses most frequently and use that to predict the 
        # opponents next play
        if potential_play_order2freq:
            prediction = max(potential_play_order2freq, key=potential_play_order2freq.get)[-1:]
        
        return prediction
    
    # As we don't have a previous play on the first round, we assume the opponent plays rock.
    # I chose as scissors you fail sometime, whereas with assuming paper you fail almost all the time
    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    # Setting a default prediction, in case we can't determine one based on the data we have.
    # Similarily, we choose Scissors here as it consistently passes with scissors, while rock and papers fails occasionally
    prediction = 'S'

    # Choosing how far back to look in history to determine the prediction. 5 is where the program works the best, 6 is alright but
    # it fails sometimes albeit rarely.
    n = 5
    last_n = "".join(opponent_history[-n:])

    # If we have enough data then use n = 5 to predict, else use n = 2 to predict until we get enough data
    if len(last_n) == n:
        prediction = predictor(prediction,n)
    elif len(last_n) > 1:
        n = 2
        lastn = "".join(opponent_history[-n:])
        prediction = predictor(prediction, n)

    # Use the prediction to determine, how we should respond
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
