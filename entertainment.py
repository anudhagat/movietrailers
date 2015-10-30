import media
import fresh_tomatoes

# Instantiate 6 of my favorite movies
star_wars = media.Movie("Star Wars: Episode VII", "The further adventures of Luke Skywalker, Han Solo and Princess Leia", "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg","https://www.youtube.com/watch?v=wCc2v7izk8w")

star_trek = media.Movie("Star Trek", "The story of how Kirk, Spock, and McCoy come to be together on the Enterprise", "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg", "https://www.youtube.com/watch?v=iGAHnZ555nI")

star_trek_into_darkness= media.Movie("Star Trek Into Darkness", "Kirk takes on Khan", "https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg", "https://www.youtube.com/watch?v=r5gdbUC9mWU")

inception = media.Movie("Inception", "World where corporate secrets are stolen from people's dreams", "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")

gladiator = media.Movie("Gladiator", "A former Roman Army General is sold into slavery and the hard life of a gladiator", "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg", "https://www.youtube.com/watch?v=owK1qxDselE")

incredibles = media.Movie("The Incredibles", "Superheros try to lead ordinary lives", "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg", "https://www.youtube.com/watch?v=eZbzbC9285I")

# Store these Movie variables in a movies list
movies = [star_wars, star_trek, star_trek_into_darkness,inception, gladiator, incredibles]
# Use fresh tomatoes to write an html page using the movies var and open the page
fresh_tomatoes.open_movies_page(movies)
