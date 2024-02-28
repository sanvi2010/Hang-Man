#If they get it wrong, a head would be added or a leg would be added to the picture
#The player would keep doing this untill they gues the word
#If a full person is formed then put game over on the screen
# if they got the word and didn't form a full person, put you win on the scrreen
#Ask if they want to restart
#If they do, go to number 2, if they don't end game. 
# word = Hello

# One condiion for the while loop is that the player 
# guess all the letters correctly within the number of lives they have
#The second contidition for the while loop is that the player doesnt
#guess all the letters correctly within the number of lives they have

#the game runs while the player didn't finished the word and the player didn't finish the lives

from hangmand_drawing import hangmand_drawing
print("Welcome to HANG MAN!")
print(hangmand_drawing[0])

word = "hello"
lives = 6
under_score = ["__"] * len(word)

while ''.join(under_score) != word and lives != 1:
    player = input("Put in a letter:   ")
    
    letter_found = False
    
    for i in range(len(word)):
        if word[i] == player:
            under_score[i] = player
            letter_found = True
    if not letter_found:
        print("THATS WRONG. ")
        lives -= 1
    print(hangmand_drawing[6-lives])   
    print(' '.join(under_score))
    
    