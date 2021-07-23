"""
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, but they 
complain that the plane usually lands before they can see the ending. So you're building a 
feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers 
movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in 
movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""

flight_length = 120
movie_lengths = [40, 70, 60, 110, 60]

movie_length_seen = set()


def two_number_sum(flight_lenght, movie_lengths):

    for first_movie_lenght in movie_lengths:

        matching_second_movie_length = flight_lenght - first_movie_lenght

        print(first_movie_lenght, matching_second_movie_length)
        print(movie_length_seen)

        if matching_second_movie_length in movie_length_seen:
            return True

        movie_length_seen.add(first_movie_lenght)

    return False


print(two_number_sum(flight_length, movie_lengths))
