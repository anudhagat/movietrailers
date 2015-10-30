import webbrowser

# Declare class Movie with a Constructor and a method
class Movie():
        # Constructor: initializes the class with info supplied about the movie
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title=movie_title
		self.movie_storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	# Method that shows the trailer given the youtube url
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
