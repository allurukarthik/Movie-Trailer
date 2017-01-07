import webbrowser
"""Inits a Movie object 
        Args:
        title = a string of the movie's title
        story = a string of the movie's story
        poster_url = a string containing a URL to a poster image
        trailer_url = a string containing a youtube URL of the movie's trailer
"""

class Movie(): 
     def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
             self.title = movie_title
             self.storyline = movie_storyline
             self.poster_image_url = poster_image
             self.trailer_youtube_url = trailer_youtube


     def show_trailer(self):
           webbrowser.open(self.trailer_youtube_url)
             
