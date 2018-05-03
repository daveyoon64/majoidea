#!/usr/bin/python3
"""
    Find the Bacon number between two actors    
"""
import requests


def find_bacon(source, target):
    """
        Finds the path from source to target actors

        Parameters:
            source: source actor
            target: target actor

        Returns:
            List of dictonaries indicating the path
        [
            {
                id: "movie id",
                movie_poster: "link to movie poster for front end",
                source_actor: "source actor from the initial search",
                source_actor_pic: "picture of actor",
                target_actor: "actor that connects to",
                target_actor_pic: "picture fo target actor"
            },
            {
                id: "movie id",
                movie_poster: "link to movie poster for front end",
                source_actor: "actor that connects from",
                source_actor_pic: "picture of actor",
                target_actor: "actor that connects to",
                target_actor_pic: "picture fo target actor"
            },
            { 
                id: "movie id",
                movie_poster: "link to movie poster for front end",
                source_actor: "actor that connects from",
                source_actor_pic: "picture of actor",
                target_actor: "this will be the final actor, the one in the search",
                target_actor_pic: "picture fo target actor"
            }
        ]
    """


    source_movies = get_movies(source)
    target_movies = get_movies(target)
    intersection = [movie for movie in source_movies
                    if movie in target_movies]
    path = []
    #while len(intersection) == 0:
        # check for actors to find link
    #if len(intersection) != 0:
        # FOUND MOVIE
    return intersection # no path found   


def get_movies(actor):
    """
        Returns the movies the actor has been in

        Return format:
        [
            {
                "url": "link",
                "year": "year released",
                "type": "Film",
                "imdb_id": "id",
                "title": "movie title"
            }
        ]

    """
    url = "http://www.theimdbapi.org/api/find/person?name={}".format(actor.replace(' ', '+'))
    print(url)
    r = requests.get(url).json()
    if "actor" in r[0]["filmography"]:
        movies = [movie for movie in r[0]["filmography"]["actor"] if movie["type"] == "Film"]
    elif "actress" in r[0]["filmography"]:
        movies = [movie for movie in r[0]["filmography"]["actress"] if movie["type"] == "Film"]
    return movies


if __name__ == "__main__":
    print(find_bacon("will smith", "margot robbie"))
