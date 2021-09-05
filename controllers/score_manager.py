import json
import os

from models import Score

class ScoreManager:
    def __init__(self,filename="example.json"):

        self._filename = filename
        self._players2=dict()

        #check the file path, if None stop doing the rest of the code in the __init__
        if not os.path.exists(filename):
            
            return None

        #read the file, translate data and save them to a dict
        with open(filename, "r") as fp:
            json_data = json.load(fp)

            for obj in json_data:
                player = Score.from_json(obj)
                self._players2[player.id]=player

    #find the data in dict by id
    def get_score_by_id(self, score_id):

        if type(score_id) != int:
            return ValueError("id must be a int number")

        
        if score_id in self._players2:
            return self._players2[score_id]

        
        return None
    
    #return the dict
    @property
    def get_players(self):
        return self._players2.values()

    #add a new player with their name and score.
    def add_score(self,name,score):
        if len(self.get_players) == 0:
            set_id=1
        else:
            for i in range(len(self.get_players)+1):
                if i not in self._players2:
                    set_id = i
                    break
        Player=Score(set_id,name,score)
        self._players2[set_id]=Player
        return True

    #delete the player by their id
    def remove_score_by_id(self,score_id):
        if type(score_id) != int:
            return ValueError("id must be a int number")


        if score_id not in self._players2:
            return False

        del self._players2[score_id]
        return True
        
    #save the dict attributes to JSON file and change them to JSON format.
    def save(self):
        #save score as a list so we can use sort to sort the score before show on the html
        new_list=[player for player in self._players2.values()]
        new_list= sorted(new_list, reverse = True)

        with open(self._filename, "w") as fp:
            json.dump([player.to_json() for player in new_list], fp)

    
