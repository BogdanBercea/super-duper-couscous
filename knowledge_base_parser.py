import json


def getGenresFromKnowledgeBase():
    genres = []

    with open(r'knowledge_bases/genre_knowledge_base.json') as f:
        data = json.load(f)

        for item in data:
            for key, value in item.items():
                if key == 'genre':
                    genres.append(value)

    return genres


def getLanguagesFromKnowledgeBase():
    languages = []

    with open(r'knowledge_bases/language_knowledge_base.json') as f:
        data = json.load(f)

        for item in data:
            for key, value in item.items():
                if key == 'language':
                    languages.append(value)

    return languages


def getCountriesFromKnowledgeBase():
    countries = []

    with open(r'knowledge_bases/countries_knowledge_base.json') as f:
        data = json.load(f)

        for item in data:
            for key, value in item.items():
                if key == 'country':
                    countries.append(value)

    return countries


def getLengthsFromKnowledgeBase():
    lengths_dict = {}

    with open(r'knowledge_bases/length_knowledge_base.json') as f:
        data = json.load(f)

        for item in data:
            lengths_dict.setdefault(item['length'], [item['low_limit'], item['top_limit']])

    return lengths_dict


def getVotesFromKnowledgeBase():
    votes_dict = {}

    with open(r'knowledge_bases/vote_average_knowledge_base.json') as f:
        data = json.load(f)

        for item in data:
            votes_dict.setdefault(item['vote'], [item['low_limit'], item['top_limit']])

    return votes_dict











