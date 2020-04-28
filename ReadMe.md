#WELCOME TO IBrew v1.0!

####IBrew is an app designed to streamline name and drink storage and round ordering.

Built and tested on Python 3.7.

Requirements: <br/>
PyMySQL==0.9.3 <br/>
coverage==5.1 <br/>
Please see the requirements.txt and install via pip3 install -r requirements.txt. <br/> The cover.sh bash script generates the coverage reports! To use: <br/> 
1) Giver permissions via chmod +x cover.sh <br/>
2) Run from command line ./coverage.sh <br/>




If you wish to contribute, the git repository can be cloned at: <br/> git@github.com:AlexanderInfinity/project.git<br/> 
IBrew is an open source project! Please get in touch with feedback, bug reporting and project development via: Alex.Wallwork@fake.email.com
 


                           Welcome to Alex Brewᵀᴹ

            Please, select an option below by entering a number:
            
            [1] Get all or search people 
            [2] Get all or search drinks
            [3] Add person to database
            [4] Add drink to database 
            [5] Delete person from database
            [6] Delete drink from database
            [7] Round Creater
            [8] Get all or search rounds 
            [Ex] Exit
            
[1] Returns all stored people or allows you to search for them by firstname, lastname or age. 

[2] Returns all stored drinks or allows you to search. 

[3] Add a person to the database and generate their unique ID.

[4] Add a drink to the database and generate a unique. 

[5] Delete person and their unique ID from the database

[6] Delete drink and their unique ID from the database

[7] Allows you to generate a round recording a brewer, drinkers and their respective drinks! <br/>
&nbsp;&nbsp;&nbsp;The round can be saved in a CSV format of: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Brewer Name" "Round Date" "Round Unique ID" <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Drinker1" "Drinker1_Drink" <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Drinker2" "Drinker2_Drink"           
&nbsp;&nbsp;&nbsp;Or Directly to the database!

[8] Returns all stored drinks or allows you to search. 

[Ex] Returns all stored people or allows you to search for them by firstname, lastname or age. 


