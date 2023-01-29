# Sqllite is lightweight db
# create table in sqlite
# https://sqlitebrowser.org/


import sqlite3
import json
from pathlib import Path
# readtext() will return string, using loads method to convert to list of dict
movies = json.loads(Path("movies.json").read_text())
print(movies)
# [{'id': 1, 'title': 'Terminator', 'year': 1984}, {'id': 2, 'title': 'Kindergarten Cop', 'year': 1990}]


# WRITE DATA TO DATABASE
# create db if db.sqlite3 file donot have and connect it , if have connetct it
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     # save the changes to database
#     conn.commit()


# READ DATA FROM DB
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
# (1, 'Terminator', 1984)
# (2, 'Kindergarten Cop', 1990)
    movies = list(cursor.fetchall())
    print(movies)  # [(1, 'Terminator', 1984), (2, 'Kindergarten Cop', 1990)]
