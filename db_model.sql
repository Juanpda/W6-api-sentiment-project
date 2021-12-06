DROP DATABASE IF EXISTS got_script;
CREATE DATABASE got_script;
USE got_script;

CREATE TABLE characters(
    ID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(30)
);
CREATE TABLE seasons(
    ID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(100)
);
CREATE TABLE episodes(
    ID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    season_id int,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id) ON DELETE SET NULL
);

CREATE TABLE dialog(
    ID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    character_id int,
    episode_id int,
    phrase VARCHAR NOT NULL,
    FOREIGN KEY (episode_id) REFERENCES episodes(episode_id) ON DELETE SET NULL,
    FOREIGN KEY (character_id) REFERENCES characters(character_id) ON DELETE SET NULL
);