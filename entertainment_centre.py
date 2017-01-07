import media
import fresh_tomatoes

"""
declare favorite movies, with 4 args each:
title (movie's title)
Storyline (Story of the movie)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""

ishq = media.Movie("Ishq",
                        "A  story of love and romance",
                        "http://www.cinemaphotos.net/gallery/movies/162_ishq_telugu_movie_latest_stills/ishq_telugu_movie_latest_stills_003.jpg",
                        "https://www.youtube.com/watch?v=0Qa2QC0DQp8")

manam = media.Movie("Manam",
                        "A  story of reincarnations",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSKeF4qwvNsbPfiJGu273wvb29BIaVeABvqylgRO2ib8c_jGaVo",
                        "https://www.youtube.com/watch?v=Y4Bq4SQc_eM")

race_gurram = media.Movie("Race Gurram",
                        "A  story about brotherhood",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcTIQPdUyqcJqHphNG5cQ-k0Q-lzz2TW7axXTH8_-sJ6BwEsDkXZ",
                        "https://www.youtube.com/watch?v=nda6eGtu8DI")

Ekkadiki_Pothavu_Chinnavada  = media.Movie("Ekkadiki Pothavu Chinnavada",
                        "Haunted by love!",
                        "http://www.idlebrain.com/movie/photogallery/ekkadikipothavuchinnavada/images/ekkadikipothavuchinnavada1.jpg",
                        "https://www.youtube.com/watch?v=PkzhoU1xthk")

Pelli_Choopulu  = media.Movie("Pelli Choopulu",
                        "How two realise that they complete each other.!",
                        "http://www.idlebrain.com/images5/small-pellichoopulu2.jpg",
                        "https://www.youtube.com/watch?v=ARACR-X3oGs")

majnu = media.Movie("Majnu",
                        "Stuck in love.!",
                        "http://www.idlebrain.com/movie/photogallery/majnu/images/majnu3.jpg",
                        "https://www.youtube.com/watch?v=m5EjKoSXw00")

# assign individual movies to movies array
movies =[ishq,manam,race_gurram,Ekkadiki_Pothavu_Chinnavada,Pelli_Choopulu,majnu]
# call open_movies_page method and pass movies array
fresh_tomatoes.open_movies_page(movies)







