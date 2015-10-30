import webbrowser


class Movie():

    # Defines the Movie class with a constructor and a show_trailer method

    def __init__(self, movie_title, duration, movie_storyline,
                 poster_image, trailer_youtube):

        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = duration

    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
