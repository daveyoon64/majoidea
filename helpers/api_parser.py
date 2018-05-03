import json


def parse_movie(json):
    movie = json.loads(json)
    return {
        "cast": [o['name'] for o in movie['cast'] if o['name'] != ""],
        "title": movie['title'],
        "id": movie['imdb_id'],
        "poster": movie['poster']['large']
    }

def parse_actor(json):
#    actor = json[0].loads(json[0])
    actor = json[0]
    if "actor" in actor['filmography']:
        act = "actor"
    else:
        act= "actress"
    films = [ o for o in actor['filmography'][act] if o['type'] == "Film"]
    return { 
        "name": actor['title'],
        "id": actor['person_id'],
        "image": actor['image']['poster'],
        "filmography": films
        # [{
        #    "id": o['imbd_id'],
        #    "title": o['title'],
        #    "year": o['year']
        #} for o in actor['filmography'][act] if o['type'] == "Film"]
    }
