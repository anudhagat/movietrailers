import media
import movies_trailers

# Instantiate 6 of my favorite movies
star_wars = media.Movie("Star Wars: Episode VII", "2h 16m",
                        ("The further adventures of Luke Skywalker,"
                         "Han Solo and Princess Leia"),
                        ("https://upload.wikimedia.org/wikipedia/en/a/a2/"
                         "Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg"),
                        "https://www.youtube.com/watch?v=wCc2v7izk8w")
star_trek = media.Movie("Star Trek", "2h 8m",
                        ("The story of how Kirk, Spock, and McCoy"
                         " come to be together on the Enterprise"),
                        ("https://upload.wikimedia.org/wikipedia"
                         "/en/2/29/Startrekposter.jpg"),
                        "https://www.youtube.com/watch?v=iGAHnZ555nI")
star_trek_into_darkness = media.Movie("Star Trek Into Darkness", "2h 12m",
                                      "Kirk takes on Khan",
                                      ("https://upload.wikimedia.org/"
                                       "wikipedia/en/5/50/StarTrek"
                                       "IntoDarkness_FinalUSPoster.jpg"),
                                      ("https://www.youtube.com/watch"
                                       "?v=r5gdbUC9mWU"))
inception = media.Movie("Inception", "2h 28m",
                        ("World where corporate secrets are stolen "
                         "from people's dreams"),
                        ("https://upload.wikimedia.org/wikipedia/en"
                         "/7/7f/Inception_ver3.jpg"),
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
gladiator = media.Movie("Gladiator", "2h 51m",
                        ("A former Roman Army General is sold into slavery "
                         "and the hard life of a gladiator"),
                        ("https://upload.wikimedia.org/wikipedia/en"
                         "/8/8d/Gladiator_ver1.jpg"),
                        "https://www.youtube.com/watch?v=owK1qxDselE")
incredibles = media.Movie("The Incredibles", "1h 56m",
                          "Superhero Family battles the Evil Scientist",
                          ("https://upload.wikimedia.org/wikipedia/en"
                           "/e/ec/The_Incredibles.jpg"),
                          "https://www.youtube.com/watch?v=eZbzbC9285I")
# Store these Movie variables in a movies list
movies = [star_wars, star_trek, star_trek_into_darkness, inception,
          gladiator, incredibles]
# Use movies to open an html page using the movies variable
movie_trailers.open_movies_page(movies)
