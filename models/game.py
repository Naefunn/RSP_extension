import random

class Game:
    def __init__(self, _player):
        self.player = _player

    def play_game(self, player):

        possible_choices = ["Rock", "Paper", "Scissors"]
        computer = random.choice(possible_choices)
        
        winner = "Computer"
        
        if player == computer:
            winner = "no one"
        if player == "Rock" and computer == "Scissors":
            winner = "player 1"
        if player == "Scissors" and computer == "Paper":
            winner = "player 1"
        if player == "Paper" and computer == "Rock":
            winner = "player 1"
        
        return winner