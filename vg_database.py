#Video Game Database
#by Steven Partlow
#This was a project that was part of the 2022 Complete Python Bootcamp from Zero to Hero in Python Course on Udemy
#https://www.udemy.com/course/complete-python-bootcamp/
#In addition to doing this python bootcamp I am also studying a full software and web developer diploma with Pitman Training in the UK. So for my final project on this python bootcamp I
#like to work in some the things I have learned on my diploma as that is a fully graded course. I would like this project to mainly focus on developing a data structure using OOP
#(Object-Orientated Programming) as these are key parts of my diploma, so for my project I wanted to create a simple database that hold records of all the computer games I own, I
#plan to have each game be it's own object with a defined base class and create a data structure of those objects and be able to add, edit, delete and sort them by certain criteria
#and then save it to a simple text file.

# FUNCTION FOR CLEARING THE CONSOLE SCREEN

import os

def cls():
    # This will clear the console screen everytime it is run
    os.system('cls' if os.name=='nt' else 'clear')

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
        
        return "%s" %(self.name)

# FUNCTIONS FOR FILE HANDLING

filepath = 'C:\\Users\\ProfS\\OneDrive\\Personal\\Learning\\2022 Complete Python Bootcamp from Zero to Hero in Python\\19. Capstone Project\\Videogame Database Project\\'

from ast import Pass
import pickle # We will use the pickle module for file-handling as this allows us to save objects, list and dictionaries to a binary file.

def load__platform_database():
    #LOAD PLATFORM DATABASE

    with open(filepath+'platforms.db', 'rb') as f_platforms:
        return pickle.load(f_platforms)

def save_platform_database():
    #SAVE PLATFORM DATABASE
    pass

def load__genre_database():
    #LOAD GENRE DATABASE
    with open(filepath+'genre.db', 'rb') as f_genre:
        return pickle.load(f_genre)

def save_genre_database():
    #SAVE GENRE DATABASE
    pass

def load_game_database():
    #LOAD GAME DATABASE        
    with open(filepath+'videogame.db', 'rb') as f_videogame:        
        return pickle.load(f_videogame)

def save_game_database():
    #SAVE GAME DATABASE
    with open(filepath+'videogame.db', 'wb') as handle:
        pickle.dump(my_games, handle, protocol=pickle.HIGHEST_PROTOCOL)

# FUNCTIONS FOR ADDING, EDITING, DELTEING FROM DATABASE

def new_game_genre_choice():
    
    index = 1
    print("\nGenre's available")
    for g in genre:
        print(str(index)+' '+genre[index-1])
        index +=1
    
    while True:
        try:    
            genre_choice = int(input("\nPlease enter the number for the genre you want:"))
        except:
            print("\nPlease enter a number matching a genre")
            continue
            
        if genre_choice < 1 or genre_choice > len(genre):
            print("\nPlease enter a number matching a genre")
            continue
        else:
            break
            
    return genre[genre_choice-1]

def new_game_platform_choice():
    
    print("\nPlatforms available\n")
    for k,v in platforms.items():
        print(k,v)

    while True:
        in_plat = input("\nEnter platform initals:")

        for k in platforms.keys():
            if in_plat.upper() == k:
                plat_exists = True
                break
            else:
                plat_exists = False
                continue
    
        if plat_exists:
            return in_plat.upper()
            break
        else:
            print("\nPlatform does not exists in database!")
            continue

def add_game():
    
    while True:
        cls()
        new_game_name = input("NEW GAME NAME:")
        new_game_dev = input("NEW GAME DEVELOPER:")
        new_game_pub = input("NEW GAME PUBLISHER:")
        new_game_gen = new_game_genre_choice()
        new_game_plat = new_game_platform_choice()
        new_game_frmt = str.upper(input("NEW GAME FORMAT CARTRIDGE/DISC/DIGITAL:"))
     
        while True:
            try:
                new_game_year = int(input("NEW GAME RELEASE YEAR:"))
            except:
                print("\nPlease enter relase year in 2XXX format")
                continue
            else:
                break
            
        new_game_comp = input("NEW GAME COMPOSER:")
        new_game_note = input("NEW GAME NOTES:")
    
        print("\n")
        print(color.BOLD + "GAME" + color.END) 
        print("====")
        print(color.BOLD + "NAME: "+color.END +new_game_name)
        print(color.BOLD + "DEVELOPER: "+color.END +new_game_dev)
        print(color.BOLD + "PUBLISHER: "+color.END +new_game_pub)
        print(color.BOLD + "GENRE: "+color.END +new_game_gen)
        print(color.BOLD + "PLATFORM: "+color.END +str(new_game_plat))
        print(color.BOLD + "FORMAT: "+color.END +new_game_frmt)
        print(color.BOLD + "YEAR OF RELEASE: "+color.END +str(new_game_year))
        print(color.BOLD + "COMPOSER: "+color.END +new_game_comp)
        print(color.BOLD + "NOTE: "+color.END +new_game_note)
        print("\n")
        
        while True:
            try:
                print("Do you want to add the above entry to the database or re-enter the whole entry")
                confirm_add = int(input("1 to confirm, 2 to re-enter:"))
            except:
                print("\nYou must enter either 1 or 2, please re-enter")
                continue
            if confirm_add < 1 or confirm_add > 2:
                print("\nYou must enter either 1 or 2, please re-enter")
                continue
            else:
                break
            
        if confirm_add == 1:
            print("\nAdded game to database")
            my_games.append(Game(new_game_name,new_game_dev,new_game_pub,new_game_gen,new_game_plat,new_game_frmt,new_game_year,new_game_comp,new_game_note))
            save_game_database()
            input("\nPress ENTER to return to menu")
            break
        elif confirm_add == 2:
            print("\nPlease re-enter entry\n")
            continue

def edit_game():
    print("\nEditing game")
    pass

# FUNCTIONS FOR VIEWING DATABSE

def view_all_games():
    cls() # Clear the console screen
    for i in my_games:
        print("\n")
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
    input("\nPress ENTER to continue")

def view_all_platforms():
    cls() # Clear the console screen
    for v in platforms.values():
        print(v)
    input("\nPress ENTER to continue")

# FUNCTIONS FOR MENUS

# VIEW MENU FUNCTIONS

def view_menu():
    # View menu function
    while True:
        cls() # Clear the console screen
        # Display the view menu
        print("\n1VIDEOGAME COLLECTION DATABASE")
        print("================================\n")
        print("1. View all games")
        print("2. View all platforms")
        print("3. Return to main menu")
        
        try: # Ask the user to enter a number between 1 and 3
            option = int(input("\nChoose option 1, 2, or 3:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 3: # If they enter a number other and 1, 2, or 3 ask them to enter a number between 1 and 3
            print("Please enter 1, 2, or 3\n")
            continue # Restart the loop
        if option == 1:
            view_all_games() # Run view_all_games function
        elif option == 2:
            view_all_platforms() # Run view_all_platforms function
        elif option == 3:
            break # Exit view menu and break the loop

# EDIT MENU FUNCTIONS

def edit_games_menu():
    # Edit games menu function
    while True:
        cls() # Clear the console screen
        # Display the games edit menu
        print("\n1VIDEOGAME COLLECTION DATABASE")
        print("================================\n")
        print("1. Add a game")
        print("2. Edit a game")
        print("3. Delete a game")
        print("4. Return to the main menu")
        
        try: # Ask the user to enter a number between 1 and 4
            option = int(input("\nChoose option 1, 2, 3, or 4:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 4: # If they enter a number other and 1, 2, ,3 or 4 ask them to enter a number between 1 and 4
            print("Please enter 1, 2,3, or 4\n")
            continue # Restart the loop
        if option == 1:
            add_game()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            break # Exit game edit menu and return to main menu

def edit_platforms_menu():
    # Edit platforms menu function
    while True:
        cls() # Clear the console screen
        # Display the platforms edit menu
        print("\n1VIDEOGAME COLLECTION DATABASE")
        print("================================\n")
        print("1. Add a platform")
        print("2. Edit a platform")
        print("3. Delete a platform")
        print("4. Return to the main menu")
        
        try: # Ask the user to enter a number between 1 and 4
            option = int(input("\nChoose option 1, 2, 3, or 4:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 4: # If they enter a number other and 1, 2, ,3 or 4 ask them to enter a number between 1 and 4
            print("Please enter 1, 2,3, or 4\n")
            continue # Restart the loop
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            break # Exit platform edit menu and return to main menu

def edit_genres_menu():
    # Edit genres menu function
    while True:
        cls() # Clear the console screen
        # Display the genres edit menu
        print("\n1VIDEOGAME COLLECTION DATABASE")
        print("================================\n")
        print("1. Add a genre")
        print("2. Edit a genre")
        print("3. Delete a genre")
        print("4. Return to the main menu")
        
        try: # Ask the user to enter a number between 1 and 4
            option = int(input("\nChoose option 1, 2, 3, or 4:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 4: # If they enter a number other and 1, 2, ,3 or 4 ask them to enter a number between 1 and 4
            print("Please enter 1, 2,3, or 4\n")
            continue # Restart the loop
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            break # Exit genre edit menu and return to main menu

def edit_menu():
    # Edit menu function
    while True:
        cls() # Clear the console screen
        # Display the edit menu
        print("\n1VIDEOGAME COLLECTION DATABASE")
        print("================================\n")
        print("1. Add / Edit / Delete games")
        print("2. Add / Edit / Delete platforms")
        print("3. Add / Edit / Delete genres")
        print("4. Return to the main menu")
        
        try: # Ask the user to enter a number between 1 and 4
            option = int(input("\nChoose option 1, 2, 3, or 4:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 4: # If they enter a number other and 1, 2, ,3 or 4 ask them to enter a number between 1 and 4
            print("Please enter 1, 2,3, or 4\n")
            continue # Restart the loop
        if option == 1:
            edit_games_menu() # Load edit games menu
        elif option == 2:
            edit_platforms_menu() # Load edit platforms menu
        elif option == 3:
            edit_genres_menu() # Load edit genre platforms menu
        elif option == 4:
            break # Exit edit menu and return to main menu

def main_menu():
    # Main menu function
    while True:
        cls() # Clear the console screen
        # Display the main menu
        print("\nVIDEOGAME COLLECTION DATABASE")
        print("===============================\n")
        print("1. View the database")
        print("2. Add / Edit / Delete from the database")
        print("3. Exit the database")

        try: # Ask the user to enter a number between 1 and 3
            option = int(input("\nChoose option 1, 2, or 3:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 3: # If they enter a number other and 1, 2, or 3 ask them to enter a number between 1 and 3
            print("Please enter 1, 2, or 3\n")
            continue # Restart the loop
        if option == 1:
            view_menu() # Load the view menu
            continue # Restart the loop
        elif option == 2:
            edit_menu() # Load the edit menu
            pass
        elif option == 3:
            print("\nExiting database") # Exiting program
            break # Break the loop

# MAIN SCRIPT

if __name__ == "__main__":

    cls() # Clear the console screen

    platforms = load__platform_database() # Load the plaforms database into memory
    print('Platform database loaded')
    genre = load__genre_database() # Load the genre database into memory
    print('Genre database loaded')
    my_games = load_game_database() # Load the games database into memory
    print('Game database loaded')

    main_menu() # Load the main menu