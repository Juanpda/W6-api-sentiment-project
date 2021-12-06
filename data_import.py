import csv
import controller
def read_data(file_path):
    csvfile = open(file_path, newline='')
    row_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in list(row_reader)[1:]:
        if(len(row) == 6):
            season_number = row[1].split(" ")[1]
            episode_number = row[2].split(" ")[1]
            episode_name = row[3]
            character_name = row[4]
            phrase_text = row[5]
            season = controller.create_season(season_number)
            episode = controller.create_episode(episode_name, episode_number, season.id)
            character = controller.create_character(character_name)
            phrase = controller.create_phrase(phrase_text, character.id, episode.id)
        


