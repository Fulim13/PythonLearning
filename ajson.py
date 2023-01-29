import json
from pathlib import Path


movies = [
    {
        "id": 1,
        "title": "Terminator",
        "year": 1984
    },
    {
        "id": 2,
        "title": "Kindergarten Cop",
        "year": 1990
    }
]

# convert to json data
data = json.dumps(movies)
print(data)

# [{"id": 1, "title": "Terminator", "year": 1984}, {"id": 2, "title": "Kindergarten Cop", "year": 1990}]

# write data to json
# write as stirng
# Path("movies.json").write_text(data)


# read data form json file
# return a string
data = Path("movies.json").read_text()
# load method will return list of dictionary
movies = json.loads(data)
print(movies)


# [{'id': 1, 'title': 'Terminator', 'year': 1984}, {'id': 2, 'title': 'Kindergarten Cop', 'year': 1990}]

print(movies[0]["title"])  # Terminator
