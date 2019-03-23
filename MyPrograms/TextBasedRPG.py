#Python Text RPG
#Sameer Dhuri
#14 March, 2019


screen_width = 100

import sys
import os
import time

## Game Constants ##


ZONENAME    = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED      =  False
UP          = 'up','north'
DOWN        = 'down','south'
LEFT        = 'left','west'
RIGHT       = 'right','east'


solved_places = {
                'a1': False,'a2': False, 'a3': False, 'a4': False,
                'b1': False,'b2': False, 'b3': False, 'b4': False,
                'c1': False,'c2': False, 'c3': False, 'c4': False,
                'd1': False,'d2': False, 'd3': False, 'd4': False
                }

zonemap = {
    'a1':{
    ZONENAME:"a1",
    DESCRIPTION: 'a1',
    EXAMINATION: 'a1',
    SOLVED: False,
    UP:'',
    DOWN:'b1',
    LEFT:'',
    RIGHT:'a2'
    },
    'a2':{
    ZONENAME:"a2",
    DESCRIPTION: 'a2',
    EXAMINATION: 'a2',
    SOLVED: False,
    UP:'',
    DOWN:'b2',
    LEFT:'a1',
    RIGHT:'a3'
    },
    'a3':{
    ZONENAME:"a3",
    DESCRIPTION: 'a3',
    EXAMINATION: 'a3',
    SOLVED: False,
    UP:'',
    DOWN:'b3',
    LEFT:'a2',
    RIGHT:'a4'
    },
    'a4':{
    ZONENAME:"a4",
    DESCRIPTION: 'a4',
    EXAMINATION: 'a4',
    SOLVED: False,
    UP:'',
    DOWN:'b4',
    LEFT:'a3',
    RIGHT:''
    },
    'b1':{
    ZONENAME:"b1",
    DESCRIPTION: 'b1',
    EXAMINATION: 'b1',
    SOLVED: False,
    UP:'a1',
    DOWN:'c1',
    LEFT:'',
    RIGHT:'b2'
    },
    'b2':{
    ZONENAME:"Home",
    DESCRIPTION: 'This is your home',
    EXAMINATION: 'It is awful',
    SOLVED: True,
    UP:'a2',
    DOWN:'c2',
    LEFT:'b1',
    RIGHT:'b3'
    },
    'b3':{
    ZONENAME:"Hogwarts",
    DESCRIPTION: 'Magic begins here',
    EXAMINATION: 'There is Voldemort in front of you',
    SOLVED: False,
    UP:'a3',
    DOWN:'c3',
    LEFT:'b2',
    RIGHT:'b4'
    },
    'b4':{
    ZONENAME:"Hidden Leaf",
    DESCRIPTION: 'Land of fire and Naruto\'s birth place',
    EXAMINATION: 'Orachimaru will be stealing your soul',
    SOLVED: False,
    UP:'a4',
    DOWN:'c4',
    LEFT:'b3',
    RIGHT:''
    },
    'c1':{
    ZONENAME:"Fiore",
    DESCRIPTION: 'Welcome to the fairy land',
    EXAMINATION: 'Say hii to Natsu',
    SOLVED: False,
    UP:'b1',
    DOWN:'c1',
    LEFT:'',
    RIGHT:'c2'
    },
    'c2':{
    ZONENAME:"Tokyo Gym",
    DESCRIPTION: 'Ippo is training for a new move',
    EXAMINATION: 'Takamura has gone crazy ',
    SOLVED: False,
    UP:'b2',
    DOWN:'d2',
    LEFT:'c1',
    RIGHT:'c3'
    },
    'c3':{
    ZONENAME:"Soul Society",
    DESCRIPTION: 'Here the soul reapers rest',
    EXAMINATION: 'Kenpachi is furious',
    SOLVED: False,
    UP:'b3',
    DOWN:'d3',
    LEFT:'c2',
    RIGHT:'c4'
    },
    'c4':{
    ZONENAME:"Britannia",
    DESCRIPTION: 'Welcome to kingdom of Britannia',
    EXAMINATION: 'There is a revolt underway save your life and run',
    SOLVED: False,
    UP:'b4',
    DOWN:'d4',
    LEFT:'c3',
    RIGHT:''
    },
    'd1':{
    ZONENAME:"Tokyo Town",
    DESCRIPTION: 'City looks suspiciously quiet',
    EXAMINATION: 'Ghouls have taken over. Run for your life!!!',
    SOLVED: False,
    UP:'c1',
    DOWN:'',
    LEFT:'',
    RIGHT:'d2'
    },
    'd2':{
    ZONENAME:"d2",
    DESCRIPTION: 'd2',
    EXAMINATION: 'd2',
    SOLVED: False,
    UP:'c2',
    DOWN:'',
    LEFT:'d1',
    RIGHT:'d3'
    },
    'd3':{
    ZONENAME:"d3",
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP:'c3',
    DOWN:'',
    LEFT:'d2',
    RIGHT:'d4'
    },
    'd4':{
    ZONENAME:"",
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP:'c4',
    DOWN:'',
    LEFT:'d3',
    RIGHT:''
    }
    }


###  Player Setup  ###
class player:
    def __init__(self):
        self.name = ''
        self.job  = ''
        self.hp   = 0
        self.mp   = 0
        self.status_effects = []
        self.location = 'a1'
        self.game_over = False

myPlayer = player()

##### Title Screen #####
def title_screen_selections():
    option = raw_input("> ")
    if option.lower() == "play":
        #start_game()  #To be written
        setup_game()
        prompt()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    else:
        print "You entered wrong direction"
        title_screen_selections()


def title_screen():
    os.system('clear')
    print '#'*50
    print "#Welcome to Adventure RPG#"
    print '#'*50
    print '-        Play        -'
    print '-        Help        -'
    print '-        Quit        -'
    print '-        By Sameer Dhuri        -'
    title_screen_selections()

def help_menu():
    print '#'*50
    print "#Welcome to Adventure RPG#"
    print '#'*50
    print '-        Use Up,Down,Left,Right to move        -'
    print '-        Type your commands to do them        -'
    print '-        Use "look" to inspect something        -'
    print '-        Good luck and have fun!!        '


#### Game Functionality ####

#def start_game():


###Game Interactivity

def printlocation():
    print "\n" + ('#'* (4 + len(myPlayer.location))) 
    print '# '+ myPlayer.location.upper() + ' #'
    print '# '+ zonemap[myPlayer.location][DESCRIPTION] + ' #'
    print "\n" + ('#'* (4 + len(myPlayer.location)))
    prompt()

def prompt():
    print "\n" + "========================="
    print "What would you like to do ?"
    action = raw_input("> ")
    acceptable_action =  ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_action:
        print "Unknown action. Please try again."
        action = input("> ")

    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

####### Game Functionality #######

def player_move(myAction):
    ask = "Where do you want to move?"
    dest = raw_input(ask)
    if  dest in ['up','north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left','west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['east','right']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south','down']:
        print myPlayer.location
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    
def movement_handler(destination):
    game_conv("You have moved to " + destination + "\n") 
    myPlayer.location = destination
    printlocation()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print "You have exhausted this zone"
        print "Congratulations !!!!"
        sys.exit()
    else:
        print zonemap[myPlayer.location][EXAMINATION]
        prompt()

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def game_conv(dialogue):
    for character in dialogue:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def setup_game():
    os.system('cls')
    
    question1 = "Hello, what's your name?"
    game_conv(question1)
    
    player_name = raw_input("> ")
    myPlayer.name = player_name
    
    question2 = "Hello, what's your job?"
    question2A = "You can play a warrior, priest or mage"
    game_conv(question2)
    
    game_conv(question2A)
    
    player_job = raw_input("> ")
    valid_jobs = ['warrior','priest','mage']

    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        game_conv( "Your job in the game is " + player_job + "\n")


    while player_job.lower() not in valid_jobs:
        print "You have made an incorrect entry"
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
        print "Your job in the game is " + player_job + "\n"

    

    #### Player Stats
    
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 60
        self.mp = 60
    
    game_conv("######################################################################\n")
    game_conv("Welcome to the Anime Land Mr."+ myPlayer.name + ". You are known to be the top " + myPlayer.job +"\n")
    game_conv("Your skills will be tested here in different anime worlds. Let's see if you survive.\n")
    game_conv("######################################################################\n")
    game_conv("Let's begin")
    
    
title_screen_selections()
    
        
    
    