from flask import Blueprint, render_template


from controllers import ScoreManager

hiscores_bp = Blueprint("web", __name__)


#Show the index page and print all the player to that page.
@hiscores_bp.route("/")
def index():
    manager = ScoreManager()
    new_list=[player for player in manager.get_players]
    new_list= sorted(new_list, reverse = True)
    Position=len(new_list)
    return render_template("index.html", players=new_list,length=Position)