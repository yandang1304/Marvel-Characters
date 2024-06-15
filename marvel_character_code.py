import random

# Function display my details
def display_details():
    print("File     : 50537_A2.py")
    print("Author   : Dang Thi Thanh Nhan")
    print("Email ID : danty035")
    print("This is my own work as defined by the University's Academic Misconduct Policy.\n\n")    

# Function takes a file name and reads the contents of that file into a list called character_list
def read_file(filename):
    character_list = []

    infile = open(filename, 'r') #Open file in read mode

    line = infile.readline().strip('\n')
    
    while line != '':
        character = []
        character.append(line)

        # Get the secret identity
        line = infile.readline().strip()
        character.append(line)

        # Gets the battle stats which are on a single line
        line = infile.readline().split(' ')

        # Get hero_type i.e. 'h' or 'v' and Add to character
        character.append(line[0])

        # Get statistic about battles, health and add to character
        for num in range(1, 6):
            character.append(int(line[num]))

        character_list.append(character)
        line = infile.readline().strip('\n')

    infile.close()
    return character_list

# Function output the contents of the list to the screen
def display_characters(character_list, display_type):
    print('='*51)
    print("-", format("Character (heroes and villains) Summary", "^49s"), "-", sep ="")
    print('='*51)
    print("-", format("P  W  L  D  Health", ">47s"), "  -", sep="")
    print('-'*51)
    # Display all characters
    if display_type == 0:
        
        for character in character_list:
            print("-  ", format(character[0], "<25s"), sep="", end = "")
            for num in range(3, 7):
                print(format(character[num], ">3d"), sep="", end="")
            print(format(character[7], ">8d"), sep="", end="")
            print("  -")
            print('-'*51)
        print('='*51)

    #Display heroes
    elif display_type == 1:
        heroes = ["Wonder Woman", "Batman", "Superman", "Aquaman", "Iron Man", "Hulk"]
        for character in character_list:
            if character[0] in heroes:
                print("-  ", format(character[0], "<25s"), sep="", end = "")
                for num in range(3,7):
                    print(format(character[num], ">3d"), sep="", end="")
                print(format(character[7], ">8d"), sep="", end="")
                print("  -")
                print('-'*51)
        print('='*51)
        
    #Display villains
    elif display_type == 2:
        
        for character in character_list:
            if character[0] == "The Joker" or character[0] == "Catwoman" or character[0] == "Thanos":
                print("-  ", format(character[0], "<25s"), sep="", end = "")
                for num in range(3, 7):
                    print(format(character[num], ">3d"), sep="", end="")
                print(format(character[7], ">8d"), sep="", end="")
                print("  -")
                print('-'*51)
        print('='*51)

# Function output the contents of the character list (list of list) to a file in the same format as the input file
def write_to_file(filename, character_list):
    outfile = open(filename, "w") #Open file in write mode
    
    for character in character_list:
        outfile.write(character[0] + "\n")
        outfile.write(character[1] + "\n")
        outfile.write(character[2] + " " + str(character[3]) + " " + str(character[4]) + " " + str(character[5]) + " " + str(character[6]) + " " + str(character[7]) + "\n")

    outfile.close() #Closing the file

# Function find character in character list
def find_character(character_list, name):
    position = -1
    index = 0
    
    while index < len(character_list):
        
        if name == character_list[index][0]:
            position = index        
        index += 1                   
    return position # If name is not in character list, return -1

# Function add new characters into character list
def add_character(character_list, name, secret_identity, hero):

    added_character = []  # Initialize new character

    # Add new character's name
    added_character.append(name)

    # Add secret identity
    added_character.append(secret_identity)

    # Add type of character
    added_character.append(hero)

    for num in range(4):  #Loop to add statistic about battles
        added_character.append(0)

    # Add character health = 100
    added_character.append(100)

   # Add new character into character list 
    character_list.append(added_character)

    return character_list

# Function remove character in character list 
def remove_character(character_list, name):
    removed_list = []
    index = 0
    
    if find_character(character_list, name) == -1:
        print("")
        print(name, "is not found in characters.\n") #Display error message
        return character_list
    else:
        while index < len(character_list):
            if index != find_character(character_list, name):
                removed_list. append(character_list[index])
          
            index += 1
        print("\nSuccessfully removed", name, "from character list.\n")
    
    return removed_list

# Function display character's information with highest won battles
def display_highest_battles_won(character_list):
    battles = character_list[0][3]
    index = 0
    character_name = character_list[0][0]
    max_battles_won = character_list[0][4]
    
    for character in character_list:
        if max_battles_won < character[4]:
            max_battles_won = character[4]
            character_name = character[0]
            battles = character[3]
           
        elif max_battles_won == character[4] and battles > character[3]:
            max_battles_won == character[4]
            character_name = character[0]
            battles = character[3]

    #Display the highest number of battles won
    print("\nHighest number of battles won =>", character_name, "with", max_battles_won, "opponents defeated!\n") 

# Function allow the heroes/villains to battle    
def do_battle(character_list, opponent1_pos, opponent2_pos):
    rounds = int(input("Please enter number of battle rounds: "))

    #Round have to be between 1-5
    while rounds > 5 or rounds < 1:
        print("Must be between 1-5 inclusive.\n")
        
        #Ask user to enter number of battle rounds again
        rounds = int(input("Please enter number of battle rounds: "))

    opponent1 = character_list[opponent1_pos]
    opponent2 = character_list[opponent2_pos]

    print("\n\n-- Battle --\n")

    #Display battle rounds
    print(opponent1[0], "versus", opponent2[0],"-", rounds, "rounds\n")

    battle_round = 0

    while battle_round < rounds and opponent1[7] > 0 and opponent2[7] > 0:
        print(f"Round: {battle_round+1}")

    # Opponent One
        damage = random.randint(0, 50) # Generate the random number that damage the first character's health
        health = opponent1[7] - damage

        if health < 0:
            opponent1[7] = 0
        else:
            opponent1[7] -= damage # The current health of the first character after being damaged
        # Display current health of opponent 1
        print("  >", opponent1[0], "- Damage:", damage,"- Current health:", opponent1[7])

        # Opponent 2
        damage = random.randint(0, 50) # Generate the random number that damage the second character's health
        health = opponent2[7] - damage

        if health < 0:
            opponent2[7] = 0
        else:
            opponent2[7] -= damage
        #Display current health of opponent 2
        print("  >", opponent2[0], "- Damage:", damage,"- Current health:", opponent2[7])
        print()
        battle_round += 1
    # Display the result after battles and update statistic
    print("-- End of battle --\n")
    if opponent1[7] == 0:
        print("--", opponent1[0], "has died! :(\n")
    if opponent2[7] == 0:
        print("--", opponent2[0], "has died! :(\n")
    if opponent1[7] > opponent2[7]:
        print(f"** {opponent1[0]} wins! **\n")
        opponent1[4] += 1
        opponent2[5] += 1
    elif opponent1[7] < opponent2[7]:
        print(f"** {opponent2[0]} wins! **\n")
        opponent1[5] += 1
        opponent2[4] += 1
    else:
        print("** Draw! **\n")
        opponent1[6] += 1
        opponent2[6] += 1
    opponent1[3] += 1
    opponent2[3] += 1
# This function returns a copy of the character list sorted in descending order of health            
def sort_by_health(character_list):
    health_character_list = []
    for character in character_list:
        health_character_list.append(character)

    for num in range(0, len(health_character_list)): # Iterate over indices of health_character_list
        for num2 in range (num + 1, len(health_character_list)): # Compare each character with the subsequent characters
            if health_character_list[num][7] < health_character_list[num2][7]:
                health_character_list[num], health_character_list[num2] = health_character_list[num2], health_character_list[num]

            elif health_character_list[num][7] == health_character_list[num2][7]:
                if health_character_list[num][3] < health_character_list[num2][3]:
                    health_character_list[num], health_character_list[num2] = health_character_list[num2], health_character_list[num]

     #Display new list
    display_characters(health_character_list, 0) 
          
display_details()
character_list = read_file("characters.txt") 
    
#Menu of choice
menu = ["list", "heroes", "villains", "search", "reset", "add", "remove", "high", "battle", "health", "quit"]

# Ask user to choose command from menu commands
choice = input("Please enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")

while choice != "quit":

    # Loop until a valid choice is entered
    while choice not in menu:
        print("\nNot a valid command - please try again.\n\n")
        
        #Ask again
        choice = input("Please enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")

    if choice == "list": # Display list of all characters
        print("")
        display_characters(character_list, 0)   
    elif choice == "heroes": # Display list of heroes
        print("")
        display_characters(character_list, 1)
   
    elif choice == "villains": # Display list of villains
        print("")
        display_characters(character_list, 2)
        
    elif choice == "search": # Search for a specific character
        name = input("\nPlease enter name: ")
        
        if find_character(character_list, name) == -1: # If name is not in character list
            print("")
            print(name, "is not found in character (heroes and villains) list.\n")

        else:      # If name is in character list 
            if character_list[find_character(character_list, name)][2] == "h":
                print("\nAll about", name, "--> HERO")
            else:
                print("\nAll about",name , "--> VILLAINS")
                
            # Display Secret identity of character
            print("\nSecret identity:", character_list[find_character(character_list, name)][1])
            
            # Display battles fought
            print("\nBattles fought:", character_list[find_character(character_list, name)][3])
            
            #Display battles won
            print("  > No won:  ", character_list[find_character(character_list, name)][4])
            
            # Display battles lost
            print("  > No lost: ", character_list[find_character(character_list, name)][5])
            
            # Display battles drawn
            print("  > No drawn:", character_list[find_character(character_list, name)][6])

            # Display current health
            print("\nCurrent health: ", character_list[find_character(character_list, name)][7], "%","\n", sep ="")
                
    elif choice == "reset": # Reset character's health
        name = input("\nPlease enter name: ")
        print("")
        
        if find_character(character_list, name)  == -1: # If name is not in character list
            print(name, "is not found in character (heroes and villains) list.\n")
        else:
            character_list[find_character(character_list, name)][7] = 100
            print("Successfully updated ", name, "'s health to 100\n")
                  
    elif choice == "add": # Add a new character
        name = input("\nPlease enter name: ")
        secret_identity = input("Please enter secret_indentity: ")
        hero = input("Is this character a hero or a villain [h|v]? ")
        
        if find_character(character_list, name) != -1: #If name is in character list
            print("")
            print(name, "already exists in character list.\n")
        else:
            character_list = add_character(character_list, name, secret_identity, hero)
            print("\nSuccessfully added", name, "to character list.\n")
       
    elif choice == "remove": # Remove a character
        
        name = input("\nPlease enter name: ") 
        character_list = remove_character(character_list, name)

    elif choice == "high": # Display character with highest battles won
        display_highest_battles_won(character_list)
                  
    elif choice == "battle": # Conduct a battle between two characters
        opponent1 = input("\nPlease enter opponent one's name: ")

        while find_character(character_list, opponent1) == -1: #If name is not in character list
                print(opponent1, "is not found in character list - please enter another opponent!")
                opponent1 = input("\nPlease enter opponent one's name: ")
                
        opponent2 = input("Please enter opponent two's name: ")
        while find_character(character_list, opponent2) == -1: #If name is not found in character list
                print(opponent2, "is not found in character list - please enter another opponent!")
                opponent2 = input("\nPlease enter opponent one's name: ")

        do_battle(character_list, find_character(character_list, opponent1), find_character(character_list, opponent2))
    elif choice == "health": # Sort characters by health
        sort_by_health(character_list)
    # Ask for choice again
    choice = input("\nPlease enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ") 

# Update new infomation about character list
write_to_file("new_characters.txt", character_list)

print("\n\n--  Program terminating --")