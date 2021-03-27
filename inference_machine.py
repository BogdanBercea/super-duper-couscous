from knowledge_base_parser import getGenresFromKnowledgeBase
from knowledge_base_parser import getLanguagesFromKnowledgeBase
from knowledge_base_parser import getCountriesFromKnowledgeBase
from knowledge_base_parser import getVotesFromKnowledgeBase
from knowledge_base_parser import getLengthsFromKnowledgeBase
import random


def UserInteraction(movie_list):

    print("##################################################")
    print()
    print('*************** MOVIE RECOMMENDER ****************')
    print()
    print("##################################################\n\n\n")

    print('*** I guess you want to watch a movie and you don\'t have many ideas ***\n')
    print('*** Let me help you ***\n')
    print('*** I will ask you a series of questions and based on your answers I will suggest you some movies ***\n\n\n')

    print('*** Ok, if you want to go further press \'y\', otherwise press anything ***')

    user_start = input();

    if(user_start == 'y'):

        movie_filtered_by_genre = []
        movie_filtered_by_languages = []
        movie_filtered_by_length = []
        movie_filtered_by_production_countries = []
        final_conclusion = []

        knowledge_base_genres = getGenresFromKnowledgeBase()
        knowledge_base_genres.append('Doesn\'t matter')

        knowledge_base_languages = getLanguagesFromKnowledgeBase()
        knowledge_base_languages.append('Doesn\'t matter')

        knowledge_base_countries = getCountriesFromKnowledgeBase()
        knowledge_base_countries.append('Doesn\'t matter')

        knowledge_base_lengths = getLengthsFromKnowledgeBase()
        knowledge_base_vote_average = getVotesFromKnowledgeBase()


        # =========== FIRST QUESTION ===============

        print('\nFirst Question: What Movie Genre do you prefer?')
        print('Choose one of the options below: \n')

        for genre in knowledge_base_genres:
            print('--> {}'.format(genre))

        flag = 0
        user_genre = input('Type here (Genre): ')

        while flag == 0:
            if user_genre in knowledge_base_genres or user_genre == 'Doesn\'t matter':
                flag = 1
            else:
                print('\n*** Typo in your input! Please try again ***\n')
                user_genre = input('Type here (Genre): ')

        if user_genre == 'Doesn\'t matter':
            movie_filtered_by_genre = movie_list
        else:
            for movie in movie_list:
                if user_genre in movie.genres:
                    movie_filtered_by_genre.append(movie)

        # =========== SECOND QUESTION ===============

        print('\nSecond Question: What do you want to be the original language of the film?')
        print('Choose one of the options below: \n')

        for language in knowledge_base_languages:
            print('--> {}'.format(language))

        flag = 0
        user_language = input('Type here (Language): ')

        while flag == 0:
            if user_language in knowledge_base_languages or user_language == 'Doesn\'t matter':
                flag = 1
            else:
                print('\n*** Typo in your input! Please try again ***\n')
                user_language = input('Type here (Language): ')

        if user_genre == 'Doesn\'t matter':
            movie_filtered_by_languages = movie_filtered_by_genre
        else:
            for movie in movie_filtered_by_genre:
                if user_language in movie.original_language:
                    movie_filtered_by_languages.append(movie)

        # =========== THIRD QUESTION ===============

        print('\nThird Question: What do you want the film production country to be?')
        print('Choose one of the options below: \n')

        for country in knowledge_base_countries:
            print('--> {}'.format(country))

        flag = 0
        user_country = input('Type here (Production Country): ')

        while flag == 0:
            if user_country in knowledge_base_countries or user_country == 'Doesn\'t matter':
                flag = 1
            else:
                print('\n*** Typo in your input! Please try again ***\n')
                user_country = input('Type here (Production Country): ')

        if user_genre == 'Doesn\'t matter':
            movie_filtered_by_production_countries = movie_filtered_by_languages
        else:
            for movie in movie_filtered_by_languages:
                if user_country in movie.production_countries:
                    movie_filtered_by_production_countries.append(movie)

        # =========== FOURTH QUESTION ===============

        print('\nFourth Question: How long do you want the movie to be?')
        print('Choose one of the options below: \n')

        lengthValidationList = []
        for item, values in knowledge_base_lengths.items():
            print('--> {0} (between {1} and {2} minutes)'.format(item, values[0], values[1]))
            lengthValidationList.append(item)
        print('Doesn\'t matter')

        flag = 0
        user_length = input('Type here (Movie Length): ')

        while flag == 0:
            if user_length in lengthValidationList or user_length == 'Doesn\'t matter':
                flag = 1
            else:
                print('\n*** Typo in your input! Please try again ***\n')
                user_length = input('Type here (Movie Length): ')

        if user_length == 'Doesn\'t matter':
            movie_filtered_by_length = movie_filtered_by_production_countries
        else:
            length_values = knowledge_base_lengths[user_length]
            for movie in movie_filtered_by_production_countries:
                if length_values[0] <= float(movie.runtime) <= length_values[1]:
                    movie_filtered_by_length.append(movie)


        # =========== FIFTH QUESTION ===============

        print('\nFourth Question: How high do you want the vote to be for the movie?')
        print('Choose one of the options below: \n')

        voteValidationList = []
        for key, values in knowledge_base_vote_average.items():
            print('--> {0} (between {1} and {2})'.format(key, values[0], values[1]))
            voteValidationList.append(key)
        print('Doesn\'t matter')

        flag = 0
        user_vote = input('Type here (Movie Vote Average): ')

        while flag == 0:
            if user_vote in voteValidationList or user_vote == 'Doesn\'t matter':
                flag = 1
            else:
                print('\n*** Typo in your input! Please try again ***\n')
                user_vote = input('Type here (Movie Vote Average): ')

        if user_vote == 'Doesn\'t matter':
            final_conclusion = movie_filtered_by_length
        else:
            vote_average_values = knowledge_base_vote_average[user_vote]
            for movie in movie_filtered_by_length:
                if vote_average_values[0] <= float(movie.vote_average) <= vote_average_values[1]:
                    final_conclusion.append(movie)

        if len(final_conclusion) > 10:
            print('\n\n *** Our movie recommendations ***\n\n')
            for index in range(20):
                random_movie = random.randint(0, len(final_conclusion))
                print('--> {}'.format(final_conclusion[random_movie].title))
            print('\n\n')
        elif 10 >= len(final_conclusion) > 0:
            print('\n\n *** Our movie recommendations ***\n\n')
            for movie in final_conclusion:
                print('--> {}'.format(movie.title))
            print('\n\n')
        else:
            print('\n\n *** We could not recommend movies based on your input. Please try again with different inputs ***\n\n')



    else:
        print('\n\n*** GOODBYE ***\n\n')
