from flask import Blueprint, jsonify, request
from datetime import datetime

from models import Score

from controllers import ScoreManager

bp_api = Blueprint("api", __name__)

# Show the data of the players
@bp_api.route("/scores")
def show_list():
    manager= ScoreManager()
    return jsonify([p.to_json() for p in manager.get_players])

# Show the certain player data by the id
@bp_api.route("/score/<int:number>")
def show_player(number):
    manager= ScoreManager()
    player = manager.get_score_by_id(number)
    if not player:
        return "Player not found", 404
        
    
    return jsonify(player.to_json()), 200

#create a player
@bp_api.route("/score", methods=["PUT"])
def create_player():
    data = request.get_json()
    manager= ScoreManager()

    # if there is a data given do the following
    if data:
        # if there is two variables called name and score do the following
        if "name" in data and "score" in data:
            # add the player to the current dict
            manager.add_score(name=data["name"], score=int(data["score"]))
        else:
            return 'Score or Name not correct',400
    else:
        return 'Score or Name are required',400
    # save the current dict to the .JSON 
    manager.save()

    return '',204


# update the current player data by id
@bp_api.route("/score/<int:number>", methods=["POST"])
def update_player(number):
    data = request.get_json()
    manager= ScoreManager()
    player = manager.get_score_by_id(number)

    # if player ID not exist show 404
    if not player:
        return 'ID not exist', 404

    # if there is a variable called score do the following
    if data and "score" in data:
        # update the score and save the current time to the objects
        player._score=int(data['score'])
        player._time=datetime.now().strftime("%H:%M:%S, %Y-%m-%d")
    else:
        return'Score not correct', 400

    # save the updated the dict to the .JSON
    manager.save()

    return '',204


# delete the player by the ID
@bp_api.route("/score/<int:number>", methods=["DELETE"])
def remove_player(number):
    manager= ScoreManager()
    player = manager.get_score_by_id(number)

    # if player ID not exist show 404
    if not player:
        return 'ID not exist', 404
    # remove the player and save the updated dict to the .JSON
    manager.remove_score_by_id(number)
    manager.save()

    return '',204

