# Noughts and Crosses (Tic-Tac-Toe)  

- Noughts and Crosses, also known as Tic-Tac-Toe, is a classic game played between two players.
- It's a great way to engage in friendly competition and to improve strategic thinking.

The game rules are simple:
- Players alternate turns placing their mark (nought or cross) on a 3x3 grid.
- The goal is to get three of your own marks in a row, either horizontally, vertically, or diagonally.
- The first player to achieve this wins the game. 
- If the entire grid is filled and no player has won, the game is a draw.

It's all about outsmarting your opponent and predicting their moves. Enjoy!

[Link to the website](https://tic-tac-toe12.herokuapp.com/)

![An image previewing all devices](/assets/screen_images/screen_image_responsive.JPG)

## Contents
- [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
- [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
- [Teachnical Design](#technical-design)
    - [Flowchart](#flowchart)
- [Technology Used](#technology-used)
    - [Language used](#language-used)
    -[Python Libraries used](#python-libraries-used)
    - [Other websites/tools used](#other-websitestools-used)
    - [3rd Party Python Libraries used](#3rd-party-python-libraries-used)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Tested Devices with Browsers](#tested-devices-with-browsers)
    - [Validator Testing](#validator-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Deploying in Heroku](#deploying-the-website-in-heroko)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning of Repository i GitHub](#cloning-the-repository-in-github)


    ## Project Goals
    ### User Stories

    - Play Noughts and Crosses (Tic-Tac-Toe) game
    - Be able to sign up as a new user
    - Be able to login as an existing user
    - Be able to read the rules
    - Be able to restart the game
    - Be able to use on different media (desktop, mobile, etc.)


    ## Site Owner

   - Create a Noughts and Crosses (Tic-Tac-Toe) game which is straightforward and clear to users
   - Ensure that new users can sign up successfully
   - Ensure that existing users can log in without issues
   - Handle and display any errors clearly to the user
   - Make sure users can easily understand how to play the game
   - Provide comprehensive rules of the game for user reference
   - Ensure users have the option to restart the game at any point


   ## User Experience
   ### Target Audience

   - Noughts and Crosses, also known as Tic-Tac-Toe, is a game that appeals to a broad audience.
   - The game is family-friendly, involving no inappropriate content, making it suitable for children, 
     adults, and the elderly alike.
   - While the game is simple to understand, it helps foster critical thinking and strategic skills.  
     Thus, it is not only fun but also beneficial for cognitive development.
   - It's an excellent choice for people who want to engage in a quick and casual game, whether they're 
     looking to kill time or to engage in a friendly competition.


   ### User Requirements

   - A classic and engaging game, offering a balance of strategy and fun.
   - Simple and intuitive navigation, making the game of Noughts and Crosses easy to play even for beginners.
   - Personalisation of game experience by allowing the input of players' names, adding a personal    
     competitive edge to the matches.
   - Secure and reliable log-in functionality, ensuring that only correctly authenticated users gain 
     access to their accounts for a safe and trusted gaming experience.

   ### Game instruction Manual
<details><summary>Click here to view instructions</summary>

 - Upon launching the Noughts and Crosses game, users are given two options: to log in if they are 
   returning players, or to register if they are new to the game.

   #### Register

   - If you're new to Noughts and Crosses, you'll need to make an account.
   - You'll just need to pick a name and password for your account.
   - After you're done signing up, you can log in and start playing.
   - Here's what you do:
     - Pick a username you like.
     - Choose a password to keep your account safe.

   #### Login

   - If they have played Noughts and Crosses before, they'll enter their username and password.
   - If the details match with the data, they will be logged in immediately.
   - They will be greeted with a welcome message displaying their name on the screen.
   - If they make an error while inputting their details, there's no problem. They can try again.
   - If their account isn't recognized, they'll be asked:
     - "register or login, please choose option 1 or 2". 
   - You will choose option 1:
     - They input their username.
     - They input their password.

#### Player's greeting

- After they successfully log in, the Noughts and Crosses game welcomes them with a greeting message, 
  prominently displaying their username.

#### Rules

- Once players have been logged in, they will be shown the rules.