import db
import json
import data_import  as di
import controller as ctrl
from app import run_server
def run():
    #di.read_data("./data/Game_of_Thrones_Script.csv")
    run_server()

    #Obtain all the characters of Game Of Thrones
    # characters = ctrl.get_all_characters()
    # print(characters)

    #Get all phrases from jhon snow:
    # phrases = ctrl.filter_phrase_by_episode("5")
    # print(phrases)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()