import csv
from Movie import Movie
import json
import re


def getAllMovieGenres(movie_list):
    genres = set()

    for movie in movie_list:
        for genre in movie.genres:
            genres.add(genre)

    return genres


def getAllMovieLanguage(movie_list):
    languages = set()

    for movie in movie_list:
        languages.add(movie.original_language)

    return languages


def getAllProductionCountries(movie_list):
    countries = set()

    for movie in movie_list:
        for country in movie.production_countries:
            countries.add(country)

    return countries


def getAllProductionCompanies(movie_list):
    companies = set()

    for movie in movie_list:
        for company in movie.production_companies:
            companies.add(company)

    return companies


def getListOfGenres(json_string):
    genres = []

    json_string = json_string.replace("\'", "\"")
    json_objects = json.loads(json_string)  # changing string to json

    for json_object in json_objects:
        for key, value in json_object.items():
            if key == 'name':
                genres.append(value)

    return genres


def getListOfProductionCompanies(_string):
    companies = []

    if _string:
        results = re.findall(r'\'name\': (.*?),', _string)
        for result in results:
            result = result.replace('\'', '')
            companies.append(result)

    return companies


def getListOfProductionCountries(_string):
    countries = []

    if _string:
        results = re.findall(r'\'name\': (.*?)}', _string)
        for result in results:
            result = result.replace('\'', '')
            countries.append(result)

    return countries


def getListOfMovies(csv_file):
    movie_list = []

    with open(csv_file, 'r', encoding="utf8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            movie_list.append(Movie(
                row['adult'],
                row['budget'],
                getListOfGenres(row['genres']),
                row['id'],
                row['original_language'],
                row['original_title'],
                row['popularity'],
                getListOfProductionCompanies(row['production_companies']),
                getListOfProductionCountries(row['production_countries']),
                row['release_date'],
                row['runtime'],
                row['title'],
                row['vote_average'],
                row['vote_count']
            ))

        return movie_list












