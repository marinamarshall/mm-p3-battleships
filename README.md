## Overview
## How to Play
## Features
## Testing
## Bugs

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
- Brian Conlon - Software Developer 

## Deployment

Fork and Clone Your Repository
1. On GitHub, go to the selected repositories main page
2. In the top-right corner, click the Fork button
3. Go to your fork of the repository
4. Click  the green download code button
5. Clone the repository using HTTPS, under "Clone with HTTPS", then click .
6. Or, To clone the repository using an SSH key, click Use SSH, then click .
7. Or, To clone a repository using GitHub CLI, click Use GitHub CLI, then click .
8. Open the Terminal
9. Change the current working directory to the location where you want the cloned directory
10. Type git clone
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
5. Click “Create new app”.
6. Create a name for the website to be deployed (this must be unique).
7. Select the region you are in.
8. Click the “Create app” button
9. Click on the settings tab.
10. Go to the Config Vars section and click add.
11. The key is PORT and the value is 8000
12. Scroll down to the Buildpacks section and click “Add buildpack”.
13. The first one to add is python.
14. Click save changes
15. Click “Add buildpack” again.
16. Select node.js.
17. Click “Save changes”.
18. Buildpacks need to be in this order (Python on top and node.js underneath).
19. Scroll back to the nav bar and click the “Deploy” tab.
20. Go to deployment method and select GitHub.
21. Search for the repository you want to connect to.
22. Click search.
23. Once the repository has been located, click “Connect” to link the repository to Heroku.
24. Scroll down to Automatic deploys and click “Enable Automatic Deploys”.
