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

   ### Game instructions
<details><summary>Click here to view instructions</summary>

#### Load Game

 - Upon launching the Noughts and Crosses game, users are given two options: to log in if they are 
   returning players, or to register if they are new to the game.

   #### Register

   - If you're new to Noughts and Crosses, you'll need to make an account.
   - You'll just need to pick a name and email address for your account.
   - After you're done signing up, you can log in and start playing.
   - Here's what you do:
     - Pick a username you like.
     - Choose a email address to keep your account safe.

   #### Login

   - If they have played Noughts and Crosses before, they'll enter their username and password.
   - If the details match with the data, they will be logged in immediately.
   - They will be greeted with a welcome message displaying their name on the screen.
   - If they make an error while inputting their details, there's no problem. They can try again.
   - If their account isn't recognized, they'll be asked:
     - "register or login, please choose option 1 or 2". 
   - You will choose option 1:
     - They input their username.
     - They input their email address .

#### Player's welcome

- After they successfully log in, the Noughts and Crosses game welcomes them with a greeting message, 
  displaying their username.

#### Rules

- Once players have been logged in, they will be shown the rules.

#### Start Game Mode

 - After the users read the rules, the game begins without delay.

 #### Game Mode

  - When the game begins, an empty 3x3 grid is displayed.
  - The game will instruct the players:"Enter the row and column numbers (0-2), separated by a space"
  - The player must input a row and a column number to place their mark.
  - If the chosen cell is already occupied or if the input is invalid, an error is displayed.
  - The game continues until one player gets three of their marks in a row, column, or diagonal, at which 
     point they win.
  - If all cells are filled and no player has won, the game is a draw.

  #### Restart Game Mode

   - When a game ends, either through a victory or a tie, a question will appear: "Do you want to play 
     again: Y/N". This is to ask if players want to start a new game.
   - To answer, players should type "Y" for Yes to play again, or "N" for No to end the session.
   - If "Y" is chosen, a new game starts immediately, returning to the initial blank game board.
   - If "N" is chosen, the game session will end, and the players will be logged out.
   - If the input is not "Y" or "N", it's considered invalid. The game will show an error message and ask 
     the question again until a valid response is provided. It's important to input the right letter to ensure smooth gameplay.

</details>

## User Stories

### Users

1.  I want users to be able to sign up easily if they are new.
2.  I want users to be able to log in smoothly if they are returning players.
3.  I want users to be promptly informed of any errors in an understandable way.
4.  I want users to easily grasp how to play the game.
5.  I want users to have access to comprehensive game rules
6.  I want users to have the option to restart the game whenever they wish.

### Site Owner

7.  As a site owner, I wish for users to enjoy their gaming experience.
8.  As a site owner, I aim to store usernames and passwords securely in Google Spreadsheet.
9.  As a site owner, I desire to provide clear error messages for incorrect user input.
10. As a site owner, I strive to validate input data for correct user entry formatting.
11. As a site owner, I want users to be greeted by their own names after they log in.

## Technical Design

## FlowChart

- [Lucidchart](https://www.lucidchart.com) help construct the flowchart below:


    ![Nought and Crosses Flowchart](/assets/screen_images/Lucid_Flow_Chart.JPG)


## Technology Used
### Language Used

  - Python

### Built-in Python Libraries

   - sys -    Provides access to some variables used or maintained by the Python interpreter and to 
              functions that interact strongly with the interpreter.
   - time -   Used for time-related tasks. 
   - os     - Provides a way of using operating system dependent functionality. os.system is used to 
              clear the terminal screen.
   - random -  Used to generate random numbers. In your script, it's used to randomly select the starting 
               player.

### 3rd Party Python Libraries

   - gspread -  It's a Python library that helps us work with Google Sheets. We can read, write, and 
                manipulate data in Google Sheets using this library.
   - google.oauth2.service_account.Credentials -  to authenticate using service account credentials and 
                                                  access Google services like Sheets.
   - email_validator -  checks if email addresses are real and correctly written


###  Websites and applications

 - GitHub     -  File storage and version control.
 - GitPod     -  Coding environment.
 - Lucidchart -   Flowchart creation.
 - Heroku     -  Website deployment.

 ## Features

 ### Main Page

  - Upon program activation, Player 1 is prompted to choose between logging in as an existing user or 
    registering as a new user.
   
   User stories covered: 1 and 2

  ![Main](/assets/screen_images/Main_page.JPG)

  ### User login/register page

 - Users are presented with two options: log in with existing details (Option 1) or register with new 
   username and email address (Option 2).

   User stories covered: 1 and 2

![User login ](/assets/screen_images/user%20login_register1.JPG)
![User Register](/assets/screen_images/user%20login_register2.JPG)


### Selection of options

 - Error messages displayed for incorrect options or input information.

User stories covered: 3, 9, 10

![User error message ](/assets/screen_images/user_login_register_error1.JPG)
![User error message 2 ](/assets/screen_images/user_login_register_error2.JPG)

### User welcome

  - User greeted with welcome message displaying their name.
 
 User stories covered: 7, 11

 ![User welcome  ](/assets/screen_images/welcome_back_login.JPG)

 ### New User

   - Notification and update message displayed after adding a new user and added to google sheet

 User stories covered: 8

  ![New User  ](/assets/screen_images/New_user_register.JPG)
  ![Updating google spreadsheet  ](/assets/screen_images/add_new%20_users.JPG)


   ### Rules

   - Clear and user-friendly rules presentation with a simple and structured layout.

User stories covered: 4, 5, 7

  ![Rules for the game](/assets/screen_images/rules_game.JPG)


   ### Game mode

   - During the game, if players do not follow the correct conventions for making moves, error messages 
     will appear to indicate the invalid input.
     
User stories covered: 3, 4, 5, 9, 10

  ![Game mode](/assets/screen_images/errors_game_mode.JPG)


  ### Restart Game

  Once the game finished, user will give the option to replay. if yes is selected, game will restart. if no is selected the game returns to the login/register page

User stories covered: 6

   ![Restart game](/assets/screen_images/restart_game.JPG)


## Testing

 - Performed testing of user stories to ensure proper implementation and functionality.
 - Tested the application on different browsers and devices to ensure compatibility.
 - Conducted validator testing to validate code compliance and identify any issues.


 ###  Testing

 1.  I want users to be able to sign up easily if they are new.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Option 2: login for new users | Choose option 2 | User will be asked username and email address| Works as expected

   ![login option 2](/assets/screen_images/testing_user_stories2.JPG)


2.  I want users to be able to log in smoothly if they are returning players.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Option 1: login for existing users | Choose option 1 | User will be asked username and email address| Works as expected

   ![login option 1](/assets/screen_images/user%20login_register1.JPG)


3.  I want users to be promptly informed of any errors in an understandable way.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| error message highlight what went wrong| error message shown | User will know how to correct the error message| Works as expected

   ![error message](/assets/screen_images/errors_game_mode.JPG)


4.  I want users to easily grasp how to play the game.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| image of noughts and crosses with clear and concise instructions| users will know how to play the game | users will play the game correctly| Works as expected

   ![rules](/assets/screen_images/rules_game.JPG)


5.  I want users to have access to comprehensive game rules

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| rules are explain in simple and stucture layout| users will know how to play the game | users will play the game correctly| Works as expected

   ![rules](/assets/screen_images/rules_game.JPG)


6.  I want users to have the option to restart the game whenever they wish.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| users will be given the option to play again or leave the game| users will press Y for playing again or N for leaving the game | users will be able to play again or leave the game | Works as expected

   ![restarting the game](/assets/screen_images/restart_game.JPG)


7.  As a site owner, I wish for users to enjoy their gaming experience.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Engaging visual for Noughts and Crosses game| View the game board | Game board is visually engaging| Works as expected

   ![Game board](/assets/screen_images/game_board.JPG)


8.  As a site owner, I aim to store usernames and passwords securely in Google Spreadsheet.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| User Data Storage in Google Sheet| User logs in or registers for the first time | Data stored in Google Sheet | Works as expected

   ![google sheet data ](/assets/screen_images/add_new%20_users.JPG)


9.  As a site owner, I desire to provide clear error messages for incorrect user input.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Error Handling | Input invalid data | Clear error message displayed | Works as expected

   ![clear error message ](/assets/screen_images/errors_game_mode.JPG)


10. As a site owner, I strive to validate input data for correct user entry formatting.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Input Validation | User enters data | System validates data format correctly | Works as expected

   ![system validation message ](/assets/screen_images/validation_input_correct.JPG)


11. As a site owner, I want users to be greeted by their own names after they log in.

 | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Personalized Greeting | User logs in | User greeted by name | Works as expected

   ![welcome message ](/assets/screen_images/welcome_message.JPG)

   ### Testing on Web Browsers and devices

Game tested and deployed successfully on the following devices and browsers:

 - Chrome and Safari browsers.
 - iPhone 13: Safari
 - Microsoft Surface Pro 7

### Validation
#### PEP8 Python Validator

 - Code validation was done using the PEP8 Python Validator available at https://pep8ci.herokuapp.com/

  - The code was validated using the PEP8 Python Validator, a tool offered by Code Institute. No errors 
    were found during the validation process.

       ![run file  ](/assets/screen_images/pep8%20validation%20run.py%20file.JPG)

       ![vaildation2 file ](/assets/screen_images/pep8%20validation%20run.py%20file.JPG)


### Bugs and Fixes

| **Bugs** | **Fixes** |
| ------- | ------- |
| Invalid input in Noughts and Crosses (missing space)| Add input validation for correct format|

### Unfixed Bugs

- all bugs fixed

## Deployment

### Deploying in Heroku

- The website was deployed to Heroku using following stages

#### create an account at Heroku then login

1. create an account at Heroku then login

       ![login heroku  ](/assets/heroku/login_heroku.JPG)


