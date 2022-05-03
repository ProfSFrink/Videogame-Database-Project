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
print("Game class initalised")

# PLATFORM OBJECT

class Platform(): # A platform object - every platform in the database will be an instance of this object, they will be stored in a dicionary
    
    def __init__(self,name,manufacturer,media_format,release,note='None'):
        
        self.name = name # Platform name
        self.manufacturer = manufacturer #Platform maufacturer
        self.media_format = media_format #Physical media format used if any
        self.release = release #Year of release
        self.note = note #Any additional information goes here
        
    def __str__(self):
        
        return self.name
print("Platform class initalised")

# HERE WE WILL DEFINE A FUNCTION THAT ADDS A NEW GAME TO THE DATABASE

def add_game():
    pass

# MAIN SCRIPT

if __name__ == "__main__":

    #LOAD THE DATABASE

    filepath = 'C:\\Users\\ProfS\\OneDrive\\Personal\\Learning\\2022 Complete Python Bootcamp from Zero to Hero in Python\\19. Capstone Project\\Videogame Database Project'

    import pickle # We will use the pickle module for file-handling as this allows us to save objects, list and dictionaries to a binary file.

    with open('platforms.db', 'rb') as f_platforms:
        platforms = pickle.load(f_platforms)
    print("platforms.db loaded successfully")

    with open('genre.db', 'rb') as f_genre:
        genre = pickle.load(f_genre)
    print("genre.db loaded successfully")

    with open('videogame.db', 'rb') as f_videogame:
        my_games = pickle.load(f_videogame)
    print("videogame.db loaded successfully")

    for i in my_games:
        print(color.BOLD + "GAME" + color.END)
        print("====")
        print(color.BOLD + "NAME: "+color.END +i.name)
        print(color.BOLD + "DEVELOPER: "+color.END +i.developer)
        print(color.BOLD + "PUBLISHER: "+color.END +i.publisher)
        print(color.BOLD + "GENRE: "+color.END +i.genre)
        print(color.BOLD + "PLATFORM: "+color.END +str(platforms[i.platform]))
        print(color.BOLD + "FORMAT: "+color.END +i.media)
        print(color.BOLD + "YEAR OF RELEASE: "+color.END +str(i.year))
        print(color.BOLD + "COMPOSER: "+color.END +i.soundtrack)
        print(color.BOLD + "NOTE: "+color.END +i.note)
        print("\n")