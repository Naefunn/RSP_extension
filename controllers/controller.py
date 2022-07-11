from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game

@app.route('/play')
def index():
    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def game():
    player_choice = request.form["player_choice"]
    player_name = request.form["player_name"]
    player_1 = Player(player_name, player_choice)
    play = Game(player_1.player_choice)
    return render_template("results.html", result=play.play_game(player_1.player_choice))