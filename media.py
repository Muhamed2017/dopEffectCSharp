import webbrowser

class Movie():
    """This class is a piece of a movie trailer website model
    where movie are listed and sorted .
    Each movie should have title and storyline and poster image
    and a url that leads to the trailer of the movie .
    """
    # creating a local variable which indicate the rating of the movie
    VALID_RATINGS = ["G","PG","PG-13","R"]

    # init method to construct a space in the memory for objects
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # defining function that shows a trailer of the movie
    def show_trailer(self):
        """this method is using a webbrwoser file which contain
        method open that open a url in a web page to show
        the trailer of the movie.
        """
        webbrowser.open(self.trailer_youtube_url)
        open(self.trailer)