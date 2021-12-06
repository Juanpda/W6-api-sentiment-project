import db
from sqlalchemy import Column, Integer, String, Float, Date,ForeignKey
import json
def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except Exception:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return d

class Character(db.Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Character({self.name}, {self.id})'
    def __str__(self):
        return self.name
    @property
    def json(self):
        return to_json(self, self.__class__)        
    


class Season(db.Base):
    __tablename__ = 'season'
    id = Column(Integer,primary_key=True)
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return f'Season({self.id})'
    def __str__(self):
        return self.id
    @property
    def json(self):
        return to_json(self, self.__class__)    


class Episode(db.Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    number = Column(String)
    season_id = Column(String, ForeignKey('season.id'))
    def __init__(self, name, number, season_id):
        self.name = name
        self.season_id = season_id
        self.number = number
    def __repr__(self):
        return f'Episode({self.name}, {self.id})'
    def __str__(self):
        return self.name 
    @property
    def json(self):
        return to_json(self, self.__class__)        
    


class Phrase(db.Base):
    __tablename__ = 'phrase'
    id = Column(Integer, primary_key=True)
    phrase = Column(String, nullable=False)
    character_id = Column(String,ForeignKey('character.id'))
    episode_id = Column(String,ForeignKey('episode.id'))
    sentiment = Column(Float, nullable=False)
    sentiment_phrase_tokenized = Column(Float, nullable=False)
    def __init__(self, phrase, character_id, episode_id, sentiment, sentiment_phrase_tokenized):
        self.phrase = phrase
        self.character_id = character_id
        self.episode_id = episode_id
        self.sentiment = sentiment
        self.sentiment_phrase_tokenized = sentiment_phrase_tokenized
    def __repr__(self):
        return f'Phrase({self.phrase}, {self.id}, sentiment: {self.sentiment})'
    def __str__(self):
        return self.phrase

    @property
    def json(self):
        return to_json(self, self.__class__)        
    
