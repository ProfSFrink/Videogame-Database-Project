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
        
        return "TITLE: %s DEVELOPER: %s PLATFORM: %s" %(self.name, self.developer, self.platform)
    
    def edit_game(self,index): # A built in function that allows us to edit an instance of the game object
        
        while True:
            edit_game_name = input("UPDATE GAME NAME:")
            edit_game_dev = input("UPDATE GAME DEVELOPER:")
            edit_game_pub = input("UPDATE GAME PUBLISHER:")
            edit_game_gen = new_game_genre_choice()
            edit_game_plat = new_game_platform_choice()
            edit_game_frmt = str.upper(input("UPDATE GAME FORMAT CARTRIDGE/DISC/DIGITAL:"))
     
            while True:
                try:
                    edit_game_year = int(input("UPDATE GAME RELEASE YEAR:"))
                except:
                    print("\nPlease enter relase year in 2XXX format")
                    continue
                else:
                    break
            
            edit_game_comp = input("UPDATE GAME COMPOSER:")
            edit_game_note = input("UPDATE GAME NOTES:")
    
            print("\n")
            print(color.BOLD + "GAME" + color.END) 
            print("====")
            print(color.BOLD + "NAME: "+color.END +edit_game_name)
            print(color.BOLD + "DEVELOPER: "+color.END +edit_game_dev)
            print(color.BOLD + "PUBLISHER: "+color.END +edit_game_pub)
            print(color.BOLD + "GENRE: "+color.END +edit_game_gen)
            print(color.BOLD + "PLATFORM: "+color.END +str(edit_game_plat))
            print(color.BOLD + "FORMAT: "+color.END +edit_game_frmt)
            print(color.BOLD + "YEAR OF RELEASE: "+color.END +str(edit_game_year))
            print(color.BOLD + "COMPOSER: "+color.END +edit_game_comp)
            print(color.BOLD + "NOTE: "+color.END +edit_game_note)
            print("\n")
        
            while True:
                try:
                    print("Do you want to update the above entry to the database or re-enter the whole entry")
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
                print("\nGame entry updated in database")
                self.name = edit_game_name
                self.developer = edit_game_dev
                self.publisher = edit_game_pub
                self.genre = edit_game_gen
                self.platform = edit_game_plat
                self.media = edit_game_frmt
                self.year = edit_game_year
                self.soundtrack = edit_game_comp
                self.note = edit_game_note
                save_game_database()
                break
            elif confirm_add == 2:
                print("\nPlease re-enter entry\n")
                continue
                
    def view_game(self):
        print("\n")
        print(color.BOLD + "GAME" + color.END)
        print("====")
        print(color.BOLD + "NAME: "+color.END +self.name)
        print(color.BOLD + "DEVELOPER: "+color.END +self.developer)
        print(color.BOLD + "PUBLISHER: "+color.END +self.publisher)
        print(color.BOLD + "GENRE: "+color.END +self.genre)
        print(color.BOLD + "PLATFORM: "+color.END +str(platforms[self.platform]))
        print(color.BOLD + "FORMAT: "+color.END +self.media)
        print(color.BOLD + "YEAR OF RELEASE: "+color.END +str(self.year))
        print(color.BOLD + "COMPOSER: "+color.END +self.soundtrack)
        print(color.BOLD + "NOTE: "+color.END +self.note)
        print("\n")

# PLATFORM OBJECT

class Platform(): # A platform object - every platform in the database will be an instance of this object
    
    def __init__(self,name,manufacturer,media_format,release,note='None'):
        
        self.name = name # Platform name
        self.manufacturer = manufacturer #Platform maufacturer
        self.media_format = media_format #Physical media format used if any
        self.release = release #Year of release
        self.note = note #Any additional information goes here
        
    def edit_platform(self, init): # A built in function that allows us to edit an instance of the platform object
        
        while True:
            # Ask user to enter updated platform name, manufacturer and media format
            edit_plat_name = input("\nUPDATE PLATFORM NAME:")
            edit_plat_manu = input("UPDATE MANUFACTURER:")
            edit_plat_media = input("UPDATE MEDIA FORMAT:")
            
            # Ask user to enter udpdated platform release year
            while True:
                try:
                    edit_plat_release = int(input("UPDATE PLATFORM RELEASE YEAR:"))
                except: # If they enter a letter ask them to try again
                    print("\nPlease enter relase year in 2XXX format")
                    continue
                else:
                    break
            
            # Ask the user for updated platform notes
            edit_plat_note = input("UPDATE PLATFORM NOTES:")
            
            # Ouput the updated platform entry to the display
            print(color.BOLD+ "\nINIT: " +color.END+ init)
            print(color.BOLD+ "NAME: " +color.END+ edit_plat_name)
            print(color.BOLD+ "MANUFACTURER: " +color.END+ edit_plat_manu)
            print(color.BOLD+ "MEDIA FORMAT: " +color.END+ edit_plat_media)
            print(color.BOLD+ "RELEASE YEAR: " +color.END+ str(edit_plat_release))
            print(color.BOLD+ "NOTES: " +color.END+ edit_plat_note)
            
            # Ask the user to confirm they wish to update the platform entry
            while True:
                try:
                    print("\nDo you want to update the above entry to the database or re-enter the whole entry")
                    confirm_add = int(input("\n1 to confirm, 2 to re-enter, 0 to exit without making changes:"))
                except: # If they do not enter a number ask them to try again
                    print("\nYou must enter either 0, 1 or 2, please re-enter")
                    continue
                if confirm_add < 0 or confirm_add > 2: # If they don't enter 1 or 2 again ask them to try again
                    print("\nYou must enter either 0, 1 or 2, please re-enter")
                    continue
                else:
                    break
                            
            # If they enter 0 we break out without making any changes
            if confirm_add == 0:
                break
            # If they confirm they want to update the platform entry, we do
            elif confirm_add == 1:
                print("\nPlatform entry updated in database")
                self.name = edit_plat_name
                self.manufacturer = edit_plat_manu
                self.media_format = edit_plat_media
                self.release = edit_plat_release
                self.note = edit_plat_note
                break
            # If they don't we ask them to re-enter the entry
            elif confirm_add == 2:
                print("\nPlease re-enter entry\n")
                continue
        
    def __str__(self):
        
        return "NAME: %s MANUFACTURER: %s" %(self.name, self.manufacturer)

# FUNCTIONS FOR FILE HANDLING

filepath = 'C:\\Users\\ProfS\\OneDrive\\Personal\\Learning\\2022 Complete Python Bootcamp from Zero to Hero in Python\\19. Capstone Project\\Videogame-Database-Project\\'

from ast import Pass
import pickle # We will use the pickle module for file-handling as this allows us to save objects, list and dictionaries to a binary file.

def load__platform_database():
    # LOAD PLATFORM DATABASE
    with open(filepath+'platforms.db', 'rb') as f_platforms:
        return pickle.load(f_platforms)

def save_platform_database():
    # SAVE PLATFORM DATABASE
    with open(filepath+'platforms.db', 'wb') as f_platforms:
        pickle.dump(platforms, f_platforms, protocol=pickle.HIGHEST_PROTOCOL)

def load__genre_database():
    # LOAD GENRE DATABASE
    with open(filepath+'genre.db', 'rb') as f_genre:
        return pickle.load(f_genre)

def save_genre_database():
    # SAVE GENRE DATABASE
    with open(filepath+'genre.db', 'wb') as f_genre:
        pickle.dump(genre, f_genre, protocol=pickle.HIGHEST_PROTOCOL)

def load_game_database():
    # LOAD GAME DATABASE        
    with open(filepath+'videogame.db', 'rb') as f_videogame:        
        return pickle.load(f_videogame)

def save_game_database():
    # SAVE GAME DATABASE
    with open(filepath+'videogame.db', 'wb') as f_videogame:
        pickle.dump(my_games, f_videogame, protocol=pickle.HIGHEST_PROTOCOL)

def sort_platforms():
    # SORT PLATFORM DICTIONARY
    import collections

    od = collections.OrderedDict(sorted(platforms.items()))
    platforms = od

# FUNCTIONS FOR ADDING, EDITING, DELTEING GAMES FROM THE DATABASE

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

def edit_game_entry():

    index = 0
    display_count = 0
    choice = -1

    for g in my_games:
        print(color.RED +str(index+1)+ color.END+" "+g.name)
        index += 1
        display_count += 1
        
        if display_count == 10:
            display_count = 0
            
            while True:
                try:
                    choice = int(input("\nPlease enter the number of the game you wish to edit, or 0 to display next 10 games:"))
                except:
                    print("\nYou must enter a whole number, please re-enter")
                    continue
                if choice < 0 or choice > len(my_games):
                    print("\nYou must enter a number that corresponds to an entry in the database or zero")
                    continue
                elif choice == 0:
                    break
                else:
                    break
        
        if choice > 0 and choice <= len(my_games):
            my_games[choice-1].view_game()
            my_games[choice-1].edit_game(choice-1)
            save_game_database()
            break

# FUNCTIONS FOR ADDING, EDITING AND DELETING PLATFORMS FROM THE DATABASE

def add_platform(): #Add a new plaform to the database
    
    while True:
        cls() # Clear the console screen

        # Ask the user the new platforms name, initals, manufacturer and media format
        new_plat_name = input("NEW PLATFORM NAME:")
        new_plat_init = input("NEW PLATFORM INITALS:")
        new_plat_manu = input("NEW PLATFORM MANUFACTURER:")
        new_plat_media = input("NEW PLATFORM MEDIA FORMAT:")

        # Ask the user the new platforms release year and then error check to make sure it's an integer
        while True:
            try:
                new_plat_year = int(input("NEW PLATFORM RELEASE YEAR:"))
            except: # If they enter anything other than a whole number we ask again and restart the loop
                print("\nPlease enter relase year in 2XXX format")
                continue
            else:
                break # If the input is correct we break the loop

        # Ask the user for any additional notes about the new platform        
        new_plat_note = input("NEW PLATFORMS ADDITIONAL NOTES:")
        
        # We display the new platform on screen to make sure the entered information is correct
        print("\n")
        print(color.BOLD + "NEW PLATFORM" + color.END) 
        print("====")
        print(color.BOLD + "NAME: "+color.END +new_plat_name)
        print(color.BOLD + "INITIALS: "+color.END +new_plat_init)
        print(color.BOLD + "MANUFACTURER: "+color.END +new_plat_manu)
        print(color.BOLD + "MEDIA FORMAT: "+color.END +new_plat_media)
        print(color.BOLD + "YEAR OF RELEASE: "+color.END +str(new_plat_year))
        print(color.BOLD + "NEW PLATFORM ADDITIONAL NOTES: "+color.END +new_plat_note)
        print("\n")
        
        # We ask the user to either confirm the new platform or re-enter it
        while True:
            try:
                print("Do you want to add the above entry to the database or re-enter the whole entry")
                confirm_add = int(input("1 to confirm, 2 to re-enter:"))
            except: # If they do not enter a whole number we ask again
                print("\nYou must enter either 1 or 2, please re-enter")
                continue
            if confirm_add < 1 or confirm_add > 2: # If they don't enter a 1 or 2 we ask again
                print("\nYou must enter either 1 or 2, please re-enter")
                continue
            else:
                break
                
        if confirm_add == 1: # If they input 1 we add the new platform to the database
            
            print("\nAdded platform to database")
            platforms[new_plat_init] = Platform(new_plat_name,new_plat_manu,new_plat_media,new_plat_year,new_plat_note)
            save_platform_database()
            input("\nPress ENTER to return to menu")
            break
        elif confirm_add == 2: # If they input 2 we ask them to re-enter
            print("\nPlease re-enter entry\n")
            continue

def edit_platform(): # Edit an existing platform within database

    cls() # Clear the console display

    # First we display the current platforms within the database
    print(color.BOLD+ "PLATFORMS AVAILABLE"+ color.END)
    print("===================")
    
    # Iterate through the platform dictionary and show keys and platform names
    for k in platforms.keys():
        print("INI:"+ color.BOLD+ "{} ".format(k)+ color.END+ platforms[k].name)
    
    # Ask the user to enter the key of the platform they wish to update
    while True:
        choice = input("\nPlease enter the initals of the platform you wish to edit or 'EXIT' to quit:")
    
        # If the key exists in the dictionary we output it to the display
        if choice.upper() in platforms:
            print(color.BOLD+ "\nPLATFORM FOUND" + color.END)
            print(color.BOLD+ "INIT: " +color.END+ choice.upper())
            print(color.BOLD+ "NAME: " +color.END+ platforms[choice.upper()].name)
            print(color.BOLD+ "MANUFACTURER: " +color.END+ platforms[choice.upper()].manufacturer)
            print(color.BOLD+ "MEDIA FORMAT: " +color.END+ platforms[choice.upper()].media_format)
            print(color.BOLD+ "RELEASE YEAR: " +color.END+ str(platforms[choice.upper()].release))
            print(color.BOLD+ "NOTES: " +color.END+ platforms[choice.upper()].note)
            
            # Call the edit_platform function of the instance of the object the user has selected
            platforms[choice.upper()].edit_platform(choice.upper())
            # Save the updated platform database and return to the edit platform menu
            save_platform_database() 
            break
        # If the user enters 'EXIT' we return to the edit platform menu without making any changes
        elif choice.upper() == "EXIT":
            break
        # If they enter an invalid dictionary we ask them to try again
        else:
            print("Platform not found, please enter the initals of a valid platform")
            continue

# FUNCTIONS FOR ADDING, EDITING AND DELETING GENRES FROM THE DATABASE

def add_genre():
    view_all_genres() # Display list of current genres
    new_genre = input("Please enter your new genre:") # Ask the user to enter there new genre

    for g in genre: # We iterate through our list of genre and check to see if the genre being added already exists
        if new_genre.upper() == g.upper():
            genre_exists = True
        else:
            genre_exists = False
        
    if genre_exists == True: # If the genre already does exits we inform the user
        print("Genre already in database")
        input("Press ENTER to continue")
    else:
        print("Genre added to database: "+new_genre) # If it does not we add to the genre list
        genre.append(new_genre)
        genre.sort() # We then resort the genre list
        save_genre_database() # Then save it to the genre file

def edit_genre():
    
    while True:
        
        cls() # Clear the console display
        for g in range(0,len(genre)): # display list of genres
            print("{} {}".format(g+1,genre[g]))
        
        # Ask the user to input the number corresponding to the genre they wish to edit and error check it
        try:
            choice = int(input("\nPlease enter the number of the genre you wish to edit, or 0 exit:"))
        except: # If they enter a letter we ask them to enter a number
            print("\nYou must enter a whole number, please re-enter")
            continue
        if choice < 0 or choice > len(my_games): # If they enter a number that is out of range we ask again
            print("\nYou must enter a number that corresponds to an entry in the database or zero")
            continue
        elif choice == 0: # If they enter zero we break out of the loop and return to the previous menu
            break
        else: # If they enter a valid chouce

            # We display the genre they have selected to edit and then ask for the new one
            print("\nThe Genre you wish to edit is:")
            print("\n"+genre[choice-1])
            edit_genre = input("\nPlease update the entry for this genre:")

            # We then display both the old and new genre on the screen
            print("\nOLD GENRE: {}".format(genre[choice-1]))
            print("\nWill be updated to")
            print("\nNEW GENRE: {}".format(edit_genre))
            
            # We then ask the user to confirm if they wish to go ahead with the update
            while True:
                try:
                    confirm = int(input("\nPlease enter 1 to confirm change or 2 to cancel:")) # We ask them to enter 1 to confirm, 2 to cancel
                except: # If they enter a letter we ask them to try again
                    print("\nYou must enter either 1 or 2, please re-enter")
                    continue
                if confirm < 0 or confirm > 2: # if they enter a number out of range we ask again
                    print("\nYou must enter either 1 or 2, please re-enter")
                    continue
                if confirm == 1: # If they enter 1 we update the genre, sort the genre list and save it to file
                    genre[choice-1] = edit_genre
                    genre.sort()
                    save_genre_database()
                    break
                elif confirm == 2: # If they enter 2 we cancel out and return to the menu
                    break

# FUNCTIONS FOR VIEWING DATABSE

def view_all_games_simple():
    cls() # Clear the console screen
    for g in my_games:
        print(g) # Iterate through the game database and print each game object
    input("\nPress ENTER to continue") # This is to pause the screen so that the user can see the output in the console window

def view_all_platforms():
    cls() # Clear the console screen
    for v in platforms.values():
        print(v) # Iterate through the game database and print each platform object
    input("\nPress ENTER to continue") # This is to pause the screen so that the user can see the output in the console window

def view_all_genres():
    cls() # Clear the console screen
    for g in genre:
        print(g) # Iterate through the game database and print each genre in the list
    input("\nPress ENTER to continue") # This is to pause the screen so that the user can see the output in the console window

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
        print("3. View all genres")
        print("4. Return to main menu")
        
        try: # Ask the user to enter a number between 1 and 4
            option = int(input("\nChoose option 1, 2, 3, or 4:"))
        except: # If they enter a character, ask the user to enter a number
            print("You must enter a number!\n")
            continue # Restart the loop
        if option < 1 or option > 4: # If they enter a number other and 1, 2, 3, or 4 ask them to enter a number between 1 and 4
            print("Please enter 1, 2, 3, or 4\n")
            continue # Restart the loop
        if option == 1:
            view_all_games_simple() # Run view_all_games function
        elif option == 2:
            view_all_platforms() # Run view_all_platforms function
        elif option == 3:
            view_all_genres() # Run view_all_genres function
        elif option == 4:
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
            edit_game_entry()
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
            # Call add_platform function
            add_platform()
        elif option == 2:
            # Call edit_platform function
            edit_platform()
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
            add_genre()
        elif option == 2:
            edit_genre()
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