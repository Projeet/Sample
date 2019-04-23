#Step 1 Displaying the board

from IPython.display import clear_output



def display_board(board):
	clear_output()
	print('  |   |')
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('  |   |')
	print('---------')
	print('  |   |')
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('  |   |')
	print('---------')
	print('  |   |')
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('  |   |')
	
 

#Step 2 Assigning the markers to the player

def player_input():
	marker = ''
	marker = input('PLayer 1: Choose a marker between X or O').upper()
				   
	
	if marker == 'X':
		return('X','O')
	else:
		return('O','X')

#Step3 WE HAVE TO PLACE THE MARKER IN THE ASSIGNED POSITION

def place_marker(board,marker,position):
	board[position] = marker

 #Step4 Check who won the game
 
def win_check(board,marker):


	   # Check all the rows
	return((board[1] == board[2] == board[3] == marker)or
		  (board[4] == board[5] == board[6] == marker)or
		  (board[7] == board[8] == board[9] == marker)or
	   #Check the diagonals
		  (board[1] == board[5] == board[9] == marker)or
		  (board[3] == board[5] == board[7] == marker)or
	   #And offcourse the clolumns
		  (board[1] == board[4] == board[7] == marker)or
		  (board[2] == board[5] == board[8] == marker)or
		  (board[3] == board[6] == board[9] == marker))
		
			

 #Step5 Choose whoes turn will come first

import random 

def choose_first():

	if random.randint(1,2) == 1:
		return 'Player1'

	else:
		return 'Player2'


 #Step6 Check if the position entered by the player is vacant
 
def space_check(board,position):
	if board[position] == ' ':
		return True
	else:
		 return False

#Step7 Check if the board is full or not
def full_board_check(board):
	for i in range(1,10): 
		if space_check(board,i):
			return False
	else:
			return True


#Step8 Keeps taking in the input from the user untill and unless the input is a vacant position

def player_choice(board):
	
	position = 0
	
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		position = int(input('Enter a position from 1-9'))
	
	return position


#Step9 Ask the player if he or she wants to play again

def replay():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print("WELCOME TO THE TIC TAK TOE GAME!!!")

while  True:

	the_board = [' ']*10

	display_board(the_board)

	turn = choose_first()

	print(turn + ' will go first')

	player1_marker,player2_marker = player_input()

	ask_player = input("Are you ready to play: Yes or No")

	if ask_player.lower()[0] == 'y':

		game_on = 'True'
	else:
		game_on = 'False'


	while game_on:

		if turn == 'Player1':
			display_board(the_board)

			position = player_choice(the_board)

			place_marker(the_board,player1_marker,position)


			if win_check(the_board,player1_marker):

				display_board(the_board)

				print("Congratulations you have won!!!")

				game_on = False

			else:
				if full_board_check(the_board):
					display_board(the_board)
					print('The game ended up in a draw')
					break
				else:
					turn = 'Player2'
		else:
			display_board(the_board)

			position = player_choice(the_board)

			place_marker(the_board,player2_marker,position)


			if win_check(the_board,player2_marker):

				display_board(the_board)

				print("Congratulations you have won!!!")

				game_on = False

			else:
				if full_board_check(the_board):
					display_board(the_board)
					print('The game ended up in a draw')
					break
				else:
					turn = 'Player1'	

	if not replay():
		break


						











	

	









		
		
	


	
		   

