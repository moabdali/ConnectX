ConnectX allows you to play connect 4 but with a custom board size.


v 0.1 - has a working GUI
	Alternates turns each time a piece is set
	Currently drops piece exactly where you click
	Correctly makes sure you can't place in an occupied location
	Does NOT have gravity yet
	Does NOT have a win condition programmed yet
	
	To do: 
		add a win condition (possibly allow player to determine the length of a win)
		add logic for the win condition
		add gravity
		consider adding a tic tac toe option as well since they're similar and the game
			currently is more well suited to tic tac toe than connect 4 anyway
		consider allowing player to choose their image
		add a minimum and max size for the game
		consider non-square game grid (i.e. 10x20 instead of only 10x10 or 20x20)
		animations for falling pieces after gravity is set
v 0.2 -
	Added proper win conditions for vertical, horizontal, and "down right/up left" conditions, but not
		for down left/up right" yet. 

v 0.3 - Glitch found and corrected in diagonal condition; properly checks for up right now.  Next version will have proper up left checking implemented

v 0.4 - yet another glitch found in diagonal check - forgot to reset count to zero after each subroutine, not just the main routine.  This has been fixed, along with a working diagonal check in all directions.  This means that as of now, we should have a working connect 4 check.  A tictactoe option will be added in next iteration of the game before adding gravity options.  


v 0.5 - shows popups asking what size you want the playing field to be, what the win length is, and a currently useless option for whether you want connect4 or tictactoe (basically a switch to see if gravity is true or not)



v 1.0 -
	Should be a fully functioning connect 4/ Tic Tac Toe game. 
	Potential improvements:
	- falling animations
	- sound
	- loop to reset game instead of exiting
	- option to pick your pieces (picture)
	- show whose turn it is via an avatar
	- more than 2 players (would require extensive recoding)
v 1.1	- added a default settings option
	- added a recommended max size for REPL repositories