from CsvParser import getListOfMovies
from inference_machine import UserInteraction

if __name__ == '__main__':

    movie_list = getListOfMovies(r'Data/movies_metadata.csv')

    UserInteraction(movie_list)



