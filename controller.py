from db_models import Character, Episode, Season, Phrase
import db
import controller
from sentiment_analyzer import text_tokenizer, sentiment_calculator

delete_key = '_sa_instance_state'

def create_character(name):
    try:
        character = db.session.query(Character).filter_by(name=name).first()
        if(character is not None):
            return character
        elif name != None and name != "":
            new_character = Character(name)
            db.session.add(new_character)
            db.session.commit()
            return new_character
        else:
            return None
    except Exception:
        return None

def create_season(id):
    try:
        season = db.session.query(Season).filter_by(id=id).first()
        if(season is not None):
            return season
        elif id != None:
            new_season = Season(id)
            db.session.add(new_season)
            db.session.commit()
            return new_season
        else:
            return None    
    except Exception:
        return None    


def create_episode(name, number, season_id):
    try:
        episode = db.session.query(Episode).filter_by(number=number, season_id=season_id).first()
        if(episode is not None):
            return episode
        elif (name != None and
            name != "" and
            number != None and
            season_id != None and
            season_id != "" ):
            print(number)
            new_episode = Episode(name, number, season_id)
            db.session.add(new_episode)
            db.session.commit()
            return new_episode
    except Exception:
        return None

def create_phrase(phrase, character_id, episode_id):
    try:
        tokenized_phrase = text_tokenizer(phrase)
        sentiment = sentiment_calculator(phrase)
        sentiment_phrase_tokenized = sentiment_calculator(tokenized_phrase)    
        new_phrase = Phrase(phrase, character_id, episode_id, sentiment, sentiment_phrase_tokenized)
        db.session.add(new_phrase)
        db.session.commit()
        return new_phrase
    except Exception as e:
        print(e)
        return None
def validate_character(id):
    try:
        result = db.session.query(Character).get(id)
        print(result)
        if(result != None):
            return result.json
        else:
            return None
    except Exception:
        return None
def validate_season(id):
    try:
        result = db.session.query(Season).get(id)
        if(result != None):
            return result.json
        else:
            return None
    except Exception:
        return None
def validate_episode(id):
    try:
        result = db.session.query(Episode).get(id)
        if(result != None):
            return result.json
        else:
            return None
    except Exception:
        return None

def remove_key_from_dict(data,key):
    result = data.pop(key, None)
    return result

def generate_dict_result(data):
    result = []
    for el in data:
        
        data_dict  = el.json
        result.append(data_dict)
    return result

def get_all_phrases():
    phrases = db.session.query(Phrase).all()
    result = generate_dict_result(phrases)
    return result


def get_all_characters():
    characters = db.session.query(Character).all()
    result = generate_dict_result(characters)
    return result


def get_all_seasons():
    seasons = db.session.query(Season).all()
    result = generate_dict_result(seasons)
    return result


def get_all_episodes():
    episodes = db.session.query(Episode).all()
    result = generate_dict_result(episodes)
    return result



def filter_phrase(key,val):
    phrases = db.session.query(Phrase).filter(Phrase[key] == val).all()
    result = generate_dict_result(phrases)
    return result

def filter_episodes(season):
    episodes = db.session.query(Episode).filter_by(season_id=season).all()
    result = generate_dict_result(episodes)
    return result

def filter_phrase_by_episode(episode):
    data = db.session.query(Phrase).filter_by(episode_id = episode).all()
    result = generate_dict_result(data)
    return result



def filter_phrase_by_character(character):
    data = db.session.query(Phrase).filter_by(character_id = character).all()
    result = generate_dict_result(data)
    return result


def filter_by_character_and_episode(character,episode):
    data = db.session.query(Phrase).filter(Phrase.character_id == character and Phrase.episode_id == episode)
    result = generate_dict_result(data)
    return result        



def get_phrase_by_id(id):
    result = db.session.query(Phrase).get(id).json
    return result

def get_character_by_id(id):
    result = db.session.query(Character).get(id).json
    return result    

def get_episode_by_id(id):
    result = db.session.query(Episode).get(id).json
    return result    
    