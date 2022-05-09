#Video Game Database
#by Steven Partlow
#This was a project that was part of the 2022 Complete Python Bootcamp from Zero to Hero in Python Course on Udemy
#https://www.udemy.com/course/complete-python-bootcamp/
#In addition to doing this python bootcamp I am also studying a full software and web developer diploma with Pitman Training in the UK. So for my final project on this python bootcamp I
#like to work in some the things I have learned on my diploma as that is a fully graded course. I would like this project to mainly focus on developing a data structure using OOP
#(Object-Orientated Programming) as these are key parts of my diploma, so for my project I wanted to create a simple database that hold records of all the computer games I own, I
#plan to have each game be it's own object with a defined base class and create a data structure of those objects and be able to add, edit, delete and sort them by certain criteria
#and then save it to a simple text file.

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#SETUP THE DATABASE

# GAME OBJECT

class Game(): # A game object - each game in the database will be an instance of this object

    def __init__(self,name,developer,publisher,genre,platform,media,year,soundtrack,note='None'):

        self.name = name # Game name
        self.developer = developer # Game's developer
        self.publisher = publisher # Game's publisher
        self.genre = genre # Game Genre - These will be defined in dictionary
        self.platform = platform # Platform the game runs on
        self.media = media # The type of media the game is on Digital/Cartridge/Disc
        self.year = year # Year of games release
        self.soundtrack = soundtrack # The soundtrack's composer
        self.note = note # Any additional notes about the game
        
    def __str__(self):
        
        return "TITLE: %s DEVELOPER: %s YEAR OF RELEASE: %s" %(self.name, self.developer, self.year) # This will be returned when we print the object

# PLATFORM OBJECT

class Platform(): # A platform object - every platform in the database will be an instance of this object, they will be stored in a dicionary
    
    def __init__(self,name,manufacturer,media_format,release,note='None'):
        
        self.name = name # Platform name
        self.manufacturer = manufacturer #Platform maufacturer
        self.media_format = media_format #Physical media format used if any
        self.release = release #Year of release
        self.note = note #Any additional information goes here
        
    def __str__(self):
        
        return "NAME: %s MANUFACTURER: %s YEAR OF RELEASE: %s" %(self.name, self.manufacturer, self.release)

# FUNCTIONS FOR FILE HANDLING

filepath = 'C:\\Users\\ProfS\\OneDrive\\Personal\\Learning\\2022 Complete Python Bootcamp from Zero to Hero in Python\\19. Capstone Project\\Videogame Database Project\\'

import pickle # We will use the pickle module for file-handling as this allows us to save objects, list and dictionaries to a binary file.

def load__platform_database():
    #LOAD PLATFORM DATABASE

    with open(filepath+'platforms.db', 'rb') as f_platforms:
        return pickle.load(f_platforms)

def save_platform_database(file):
    #SAVE PLATFORM DATABASE

    pass

def load__genre_database():
    #LOAD GENRE DATABASE

    with open(filepath+'genre.db', 'rb') as f_genre:
        return pickle.load(f_genre)

def save_genre_database(file):
    #SAVE GENRE DATABASE
    
    pass

def load_game_database():
    #LOAD GAME DATABASE    
    
    with open(filepath+'videogame.db', 'rb') as f_videogame:        
        return pickle.load(f_videogame)

def save_game_database(file):
    #SAVE GAME DATABASE

    pass

# HERE WE WILL DEFINE A FUNCTION THAT ADDS A NEW GAME TO THE DATABASE

def add_game():
    pass

# MAIN SCRIPT

if __name__ == "__main__":

    platforms = load__platform_database()
    print('Platform database loaded')
    genre = load__genre_database()
    print('Genre database loaded')
    my_games = load_game_database()
    print('Game database loaded')

for g in my_games:
    print(g)

for v in platforms.values():
    print(v)