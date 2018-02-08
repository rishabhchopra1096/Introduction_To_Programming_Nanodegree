import webbrowser
class Movie():
    """This class will form the blueprint for every instance
    of this class. It will store the data of the attributes as
     well as methods to be used by the class """
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """This is the constructor of the class. Whenever we make an
        instance of this class. The __init__ function will create
        space in memory for a new instance of this class."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open webbrowser with the currrect url"""
        webbrowser.open(self.trailer_youtube_url)


"""Some Other NOTES:"""
'''New Vocabulary Words'''
#--Class : The Class keyword allows us to make classes. You can think of a class as a blueprint.
#A class can have both data(self.title=movie_title
#                           self.storyline=movie_storyline
#                           self.poster_image_url=poster_image
#                           self.trailer_youtube_url=trailer_youtube
# ) and methods (    def show_trailer(self):
        # webbrowser.open(self.trailer_youtube_url))

#--Instance : We can make multiple instances of that class, In this case
# we made instances like toy_story, avatar and hp7_ii.
# When we create an instance of a class, the class constructor gets called.

#--Constructor:When we create an instance of a class, the class constructor gets called.
# This refers to __init__ method in the class. It is here where we initialise all the data and
# methods associated with the instance. The constructor uses the keyword self.

#--self : The constructor uses the keyword self. self is the object being created, so when an instance is called
#the argument within __init__ for self is replaced with the new_instance_name. So when the instance toy_story is being
# created self is toy_story and this argument(toy_story) for the init function's parameter(self) is taken in by default.

#--instance variable: All of the variables associated with a specific instance are called
# instance variables. There are unique to the instance and can be accessed using the self keyword inside the class(self.title=movie_title)
# and the instance variable name outside the class(avatar.title="Avater").
#The self.variable_name variables that are associated with the instances
# and are unique to each instance like toy story and avatar have a different storyline:
# self.storyline=movie_storyline.

#---Instance method: A function that is defined inside a class and is associated with an instance.They all have the first instance method
# == to self.
