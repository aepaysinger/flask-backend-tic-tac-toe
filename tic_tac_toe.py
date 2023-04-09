from flask import Flask, request
from flask_cors import CORS

from logic_functions import calculate_winner, get_fresh_board, get_next_board


app = Flask(__name__)
cors = CORS(app)


@app.route("/winner/", methods=["POST"])
def winner():
    data = request.json
    return {
        "winner": calculate_winner(data["squares"]),
    }


@app.route("/board/", methods=["GET", "POST"])
def board():
    if request.method == "POST":
        data = request.json
        return {
            "squares": get_next_board(data["squares"], data["i"], data["x_is_next"])
        }

    elif request.method == "GET":
        return {"squares": get_fresh_board()}


PLAYER = "X"


@app.route("/test", methods=["POST"])
def proto():
    global PLAYER
    data = request.json
    if PLAYER == data["player"]:
        PLAYER = "O" if data["player"] == "X" else "X"
        return "ok", 200
    return "no good", 400
