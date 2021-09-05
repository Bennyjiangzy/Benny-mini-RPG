import json
from datetime import datetime

class Score:
    def __init__(self,identifier,name,score,date=None):
        self._id=identifier
        self._name=name
        self._score=score
        
        #if the there is no date, use the current time
        if date ==None:
            self._time=datetime.now().strftime("%H:%M:%S, %Y-%m-%d")
        else:
            self._time=date

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def score(self):
        return self._score
    
    @property
    def date(self):
        return self._time

    #change the data to JSON format
    def to_json(self):

        return {"id": self._id,"name":self._name,"score":self._score,"date":self._time}
    
    #create a customize comparison rule
    
    def __lt__(self,other):
        if isinstance(self,Score) and isinstance(other,Score):
            #if score are equal, the old time win
            if self._score != other._score:
                return self._score < other._score
            #else high score win
            else:
                return self._time > other._time
        else:
            raise TypeError("wrong value")


    # re-create the objects when we extract data from JSON and after change the format
    @classmethod
    def from_json(cls, data):

        return cls(identifier=data["id"], name=data["name"], score=data["score"], date=data["date"] )
