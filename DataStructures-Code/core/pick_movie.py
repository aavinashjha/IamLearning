# Write a function that takes an integer flight_length (in minutes) and 
# a list of integers movie_lengths (in minutes) and returns a boolean 
# indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

def will_i_be_able_to_see_two_movies(flight_length, movie_lengths):
    print('Flight Length is ', flight_length)
    print('Movie Lengths are ', movie_lengths)
    possible = False
    for first_movie in movie_lengths:
        for second_movie in movie_lengths[movie_lengths.index(first_movie) + 1:]:
            if first_movie + second_movie == flight_length:
                print('First:', first_movie, 'Second:', second_movie)
                possible = True

    return possible




if __name__ == '__main__':
    flight_length = int(input('Enter flight length'))
    movie_lengths = [int(movie) for movie in input('Enter space separated movie lengths').split(' ')]
    print(will_i_be_able_to_see_two_movies(flight_length, movie_lengths))
