from flask import Flask
from flask import request
from flask import jsonify
import controller as ctrl

app = Flask(__name__)

error_message = {"error":"Internal server error."}

@app.route('/api/phrases', methods=['GET'])
def get_phrases():
    data  = ctrl.get_all_phrases()
    response = {'result': data}
    return jsonify(response)

@app.route('/api/episodes', methods=['GET'])
def get_episodes():
    data  = ctrl.get_all_episodes()
    response = {'result': data}
    return jsonify(response)

@app.route('/api/seasons', methods=['GET'])
def get_seasons():
    data  = ctrl.get_all_seasons()
    response = {'result': data}
    return jsonify(response)

@app.route('/api/characters', methods=['GET'])
def get_characters():
    data  = ctrl.get_all_characters()
    response = {'result': data}
    print(response)
    return jsonify(response)



@app.route('/api/phrases/<id>', methods=['GET'])
def get_phrase_by_id(id):
    data  = ctrl.get_phrases_by_id(id)
    response = {'result': data}
    return jsonify(response)

@app.route('/api/episodes/<id>', methods=['GET'])
def get_episode_by_id(id):
    data  = ctrl.get_episodes_by_id(id)
    response = {'result': data}
    return jsonify(response)

@app.route('/api/seasons/<id>', methods=['GET'])
def get_season_by_id(id):
    data  = ctrl.get_seasons_by_id(id)
    response = {'result': data}
    return jsonify(response)

@app.route('/api/characters/<id>', methods=['GET'])
def get_character_by_id(id):
    data  = ctrl.get_characters_by_id(id)
    response = {'result': data}
    return jsonify(response)


#Create Routes 

@app.route('/api/new/phrase', methods=['POST'])
def create_phrase():
    data  = request.json
    valid_character = ctrl.validate_character(data["character_id"])
    valid_episode = ctrl.validate_episode(data["episode_id"])
    if(
        valid_character and
        valid_episode 
    ):
        result = ctrl.create_phrase(data["text"], data["character_id"], data["episode_id"])
        if(result != None):
            response = {'result':result.json}
            return jsonify(response)
        else:
            print("Falla")
            return error_message
    else:
        return error_message

@app.route('/api/new/episode', methods=['POST'])
def create_episode():
    data = request.json
    if(
        data["number"] != None and
        data["name"] != None and
        data["season_id"] != None
    ):

        result = ctrl.create_episode(data["name"], data["number"], data["season_id"])
        if(result != None):
            response = {'result': result.json}
            return jsonify(response)
        else:
            return error_message
    else:
        return error_message

@app.route('/api/new/season', methods=['POST'])
def create_season():
    data = request.json
    if(
        data["number"] != None
    ):

        result = ctrl.create_season( data["number"])
        if(result != None):
            response = {'result': result.json}
            return jsonify(response)
        else:
            return error_message
    else:
        return error_message

@app.route('/api/new/character', methods=['POST'])
def create_character():
    data = request.json
    if(
        data["name"] != None
    ):

        result  = ctrl.create_character(data["name"])
        if(result != None):
            response = {'result': result.json}
            return jsonify(response)
        else:
            return error_message
    else:
        return error_message



@app.route('/api/phrasesByCharacterAndEpisode/<character>/<episode>', methods=['GET'])
def filter_by_character_and_episode(character, episode):
    data  = ctrl.filter_by_character_and_episode(character,episode)
    response = {'result': data}
    return jsonify(response)

@app.route('/api/phrasesByCharacter/<character>', methods=['GET'])
def filter_phrase_by_character(character):
    data  = ctrl.filter_phrase_by_character(character)
    response = {'result': data}
    return jsonify(response)  

@app.route('/api/phrasesByEpisode/<epsiode>', methods=['GET'])
def filter_phrase_by_epsiode(epsiode):
    data  = ctrl.filter_phrase_by_episode(epsiode)
    response = {'result': data}
    return jsonify(response)   

def run_server():
    app.run(debug=True)