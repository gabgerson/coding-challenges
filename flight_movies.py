def get_movies(flight_length, movie_lengths):
    # movie lengths is a list in minutes
    #flight length is flight time in minutes
    index = 1
    first_index = 0
    two_movies = False
    keep_looping = True
    first_movie_length = movie_lengths[0]
    if len(movie_lengths) == 1:
        if movie_lengths[0] == flight_length:
            return True
        return False
    while True:
        # print("hello")
        # print(first_movie_length)
        # print("I am 1st length")
    
        if first_movie_length + movie_lengths[index] == flight_length:
            two_movies = True
            break
        if movie_lengths[index] == movie_lengths[-1]:
            # print(movie_lengths[index])
            index = 0
            first_index += 1
            first_movie_length = movie_lengths[first_index]
            break
        if first_movie_length == movie_lengths[-1]:
            
            break
        # print(first_movie_length)
        
        index +=1
    # print(first_movie_length)
    # print(movie_lengths[index])
    return two_movies
def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False


print(get_movies(120,[50, 20, 80, 70]))
print(get_movies(120,[50, 20, 80]))
print(get_movies(120,[60]))