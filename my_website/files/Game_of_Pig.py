import random
import pickle

#Setting up high score and high scorer globabl variables
globhigh_score=0
globhigh_scorer=str('')

# load the previous high score if it exists
#creates a file called 'score.dat' where the high score information is saved
#this is a text file that can be edited
#if you want to reset the high score just delete the text in the file and re-run the program
try:
    with open('score.dat', 'rb') as file:
        globhigh_score = pickle.load(file)
        globhigh_scorer = pickle.load(file)
except:
    globhigh_score = 0

def introduction():
    #Title of the Game
    #Directions, scoring, and current high score introducted
    print('')
    print('')
    print ('Welcome to the Game of Pig!')            
    print('')
    print('The object of the game is to score the highest total.')
    print('')
    print('On each turn you will roll 2 dice and tally the SUM.')
    print('Your score will accumulate on each turn you have.')
    print('If a 1 is rolled on EITHER dice, the game ends and your score is zero.')
    print('')
    print('')
    print('IMPORTANT:')
    print('If you roll DOUBLES you receive a 15 point bonus (in addition to the total of the dice).')
    print('If the sum of your dice is 7 you will LOSE 7 points.')
    print('')
    print('You may stop at any time or continue to press your luck for more points.')
    print('')
    print('')
    print('THE CURRENT HIGH SCORE TO BEAT IS "'+ str(globhigh_score)+ '" AND BELONGS TO "'+ str(globhigh_scorer)+'".') 
    print('')
    print('')
    
def roll(sides):
    #This represents the player rolling 2 dice
    
    #d1 is dice 1, this randomly selects a number from 1 to 6 to model a dice roll
    d1=random.randrange(1,sides+1)             
    return d1
    #d2 is dice 2, performs same function as d1
    d2=random.randrange(1,sides+1)              
    return d2
    
def turn():
    #This is the beginning of a player's turn
    #There score is 0 to start and they may begin by rolling
    
    score=0
    keep_rolling=1
    raw_input("Press Enter to Begin")            #When Keep_rolling==1 allows the user to continue rolling if they choose
    while keep_rolling==1:                       #Keep_rolling can have two values '1' or '0'
        d1=roll(6)                               #This acts as an On/Off switch
        d2=roll(6)
        print "You rolled a" ,d1, "and", d2
        if d1==1 or d2 ==1:
            score=0                               #As in the rules, a '1' is rolled, you turn ends
            keep_rolling=0                     #When keep_rolling is '0' the player is then given their score
                                                
        elif (d1==1 and d2==1) or (d1==2 and d2==2) or (d1==3 and d2==3) or (d1==4 and d2==4) or (d1==5 and d2==5) or (d1==6 and d2==6):
            #Doubles gives the player a 10 point bonus
            score+=15+d1+d2
            print "Your New Score is", score
            y=raw_input ('Press r to roll again or press s to stop')
            if y=="r":
                keep_rolling=1                    #Here the player is given a choice to continue rolling or not. 
            else:
                keep_rolling=0
                
        elif (d1+d2==7) and ((d1 or d2) !=1):
            #A sum of 7 will result in the player losing 7 points on their total
            score-=7
            print "Your New Score is", score
            y=raw_input ('Press r to roll again or press s to stop')
            if y=="r":
                keep_rolling=1                    #Here the player is given a choice to continue rolling or not. 
            else:
                keep_rolling=0

        else:
            #Sum of their dice is added to total (if it doesn't meet the criteria above)
            score+=d1+d2
            print "Your New Score is", score
            y=raw_input ('Press r to roll again or press s to stop')
            if y=="r":
                keep_rolling=1                    #Here the player is given a choice to continue rolling or not. 
            else:
                keep_rolling=0
                 
                           
    if score>globhigh_score:
        #Determines if the Player's score is the new high score and if so, then the HIGH Score changes and they enter their name.
        print ('Congratulations! NEW HIGH SCORE=' + str(score) )
        global globhigh_score
        globhigh_score = score
        global globhigh_scorer
        globhigh_scorer=str(raw_input('Enter your name'))
        
    else:    
        print ('')
        print ('GAME OVER')
        print "Your Final Score is" , score       #Player is given their final score
    
    
introduction()                  #Initializes the directions and the gameplay 
turn()

# saves the high score
with open('score.dat', 'wb') as file:
    pickle.dump(globhigh_score, file)
    pickle.dump(globhigh_scorer, file)