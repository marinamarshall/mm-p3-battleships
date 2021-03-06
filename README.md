# Battleships

Battleships is a backend Python-coded game that is played in the terminal. The game runs in the CodeInstitute mock terminal on Heroku.

The game provides one board where the the user guesses where the ship is located from the command-line. The computer randomly generates where the ship is located in the game. This is a fun terminal-based game against the computer. The battleship occupies one square on the board. The user will have 10 attempts at finding the battleship and the game ends when the user has used up all of their guesses OR when they have found the battleship.

[Here is the live version of the battleships game](https://mm-p3-battleships.herokuapp.com/)

## How to Play
This battleships game is based on the original pen-and-paper game, with a few tweaks incorporated. [Read more here](https://en.wikipedia.org/wiki/Battleship_(game)). As soon as the terminal is loaded, information is provided to the user to tell them what to expect from the game. The user will be prompted to enter a guess for a row and column number they think the ship might be located at. In this terminal-based version of the game, the player will play against the computer on a single board that is marked with '-' signs to indicate columns and rows that the user has not yet guessed.

Once the user begins guessing, the correct answer will be indicated by an 'X' and incorrect answers will be marked with an 'O'. The computer randomly generates one ship for the user to locate and destroy within 10 moves. The user will be prompted to enter a guess for where they think the ship is located within the grid. This answer will be between 0 and 3 for each value (row and column). Once the user has either located and destroyed the ship OR they have used up their 10 guesses, the game will end and the user can decide if they want to play again on another randomly generated game of battleships.

## Features
The ship row and column numbers are generated at random by the computer. There is one ship that the user must find before they run out of guesses. They user cannot see where this ship is located so they must guess until they get it right.

The player plays against the computer as the computer accepts user input. The computer keeps track of how many guesses the user has used and tells the user what they have guessed with each new guess. The "-" symbol indicates areas that the user have not yet been guessed. The "O" symbols indicate misses that the user has guessed and the "X" indicates a hit. Once the ship has been hit, the game ends.

The computer generates the same size board each time (4x4) with one ship placed in the grid. The user can answer the same guess twice so that it is more challenging. The computer does not flag the duplicate guesses.

## Future Releas
- More than one ship
- User can choose grid size
- Update user with their score
- Play in a 2 player version

## Testing
- Original errors when run through [PEP8 Results](assets/images/pep8-errors.png)
- Code passed through the PEP8 linter with no issues [PEP8 Results](assets/images/clear-pep8.png)
 - Images for these results can be found in the assets/images folder
- Given invalid inputs: string when a number is expected, out of bounds inputs.
- Tested in GitPod terminal (local) and CodeInstitute Heroku Terminal

### Input Validation and Error-Checking
 - The player cannot guess coordinates outside of the board size (0-3)
 - Numbers are the input the board accepts, otherwise an error message is displayed

 ### Future Features
 - Include more than one ship
 - Allow user to determine board size
 - Generate a board for the computer to make guesses
 - Allow ships to occupy more than one square
 - Computer flags used guesses

## Data Model
The grid that is generated by the computer is the data model being used. One board is created at the beginning of the game for the user to see what it looks like and then it is updated with answers and reprinted on each round of the game (10 guesses = 10 rounds). The print_battleships_board() function simply goes through a loop to generate a 4x4 grid of "-" symbols and each symbol is then added to an array to create a 2D array thet the user sees and updates when they guess the row and column. The user can answer the same guess twice so that it is more challenging. The computer does not flag the duplicate guesses.

## Bugs
- Try/except statement did not work as expected - fixed by Jo from CodeInstitute
- String Value error crashed code - fixed
- Number out of bounds crashed code - fixed
- Pass statement not working as expected - fixed

## Credits
- CodeInstitute - Python coursework notes and videos
- CodeInstitute - Mock Terminal
- CodeInstitute - Heroku deployment steps 
- Youtube tutorials to get inspiration and ideas on how to tackle the problems
  - [Henrik Rosqvist](https://www.youtube.com/watch?v=92QRKiCldnE)
  - [Dr Codie](https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i)
  - [Dr Codie](youtube.com/watch?v=EziS2eGZGz4&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i&index=3)
  - [Dylan Israel](https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=298s)
  - [CS Students](https://www.youtube.com/watch?v=MgJBgnsDcF0)
- GitHub projects looked at
  - [Anna Lulakova](https://gist.github.com/anceque/4064737)
  - [Guimaion](https://gist.github.com/guimaion/9275543)
- [Python Fiddle project code](http://pythonfiddle.com/battleships-game-in-python/)  
- Extra Reading
  - [PYnative](https://pynative.com/python-random-randrange/)
  - [StackOverflow](https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation)  
- Python Tutor to visualize code step-by-step
- Stack Overflow for general questions
- Slack - Python Essentials Channel
- Mentor Chris
- Mentor Richard for helping to get the project foundations set up
- CodeInstitute tutor Jo
- Brian Conlon - Software Developer 

## Deployment

Fork and Clone Your Repository
1. On GitHub, go to the selected repositories main page
2. In the top-right corner, click??the Fork button
3. Go to??your fork??of the repository
4. Click????the green download code button
5. Clone the repository using HTTPS, under "Clone with HTTPS", then click .
6. Or, To clone the repository using an SSH key, click??Use SSH, then click??.
7. Or, To clone a repository using GitHub CLI, click??Use GitHub CLI, then click??.
8. Open??the Terminal
9. Change the current working directory to the location where you want the cloned directory
10. Type??git clone
11. Then paste the URL you copied earlier
12. Press Enter
13. You now have a local clone

Remote Deployment
1. On GitHub, go to your chosen repository
2. Click the green Gitpod button to deploy the repository to your machine

Local Deployment
1. Go to Gitpod
2. Select the repository to be used and click open
3. Python runs in the terminal so the live deployed version is in a mock terminal created by CodeInstitute that can be accessed through Heroku

Heroku deployment
1. Using Gitpod, create a list of requirements that the project needs to run (dependencies) - these will go in the requirements.txt file.
2. Type pip3 freeze > requirements.txt into the terminal.
3. Go to [Heroku](https://heroku.com) and login to your account.
4. From the Heroku dashboard, create a new app (tab located in the top right hand corner, below account settings image).
5. Click ???Create new app???.
6. Create a name for the website to be deployed (this must be unique).
7. Select the region you are in.
8. Click the ???Create app??? button
9. Click on the settings tab.
10. Go to the Config Vars section and click add.
11. The key is??PORT??and the value is??8000
12. Scroll down to the Buildpacks section and click ???Add buildpack???.
13. The first one to add is python.
14. Click save changes
15. Click ???Add buildpack??? again.
16. Select node.js.
17. Click ???Save changes???.
18. Buildpacks need to be in this order (Python on top and node.js underneath).
19. Scroll back to the nav bar and click the ???Deploy??? tab.
20. Go to deployment method and select GitHub.
21. Search for the repository you want to connect to.
22. Click search.
23. Once the repository has been located, click ???Connect??? to link the repository to Heroku.
24. Scroll down to Automatic deploys and click ???Enable Automatic Deploys???.
