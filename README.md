#WELCOME TO AlexBrew v1.0!

##Welcome

AlexBrew is an app designed to streamline name and drink storage and allows the production of new and persistence of historic rounds.

Built and tested on Python 3.7.

##Setup

Requirements: <br/>
>PyMySQL==0.9.3 <br/>
>coverage==5.1 <br/>

Please see the requirements.txt and install via:
>pip3 install -r requirements.txt. 

The cover.sh bash script generates the coverage reports! To use:  

>1) Giver permissions via chmod +x cover.sh <br/>
>2) Run from command line ./coverage.sh <br/>

##Contribute


AlexBrew is an open source project! 
If you wish to contribute to this open source project, the git repository can be cloned at: <br/> 
>git@github.com:AlexanderInfinity/project.git<br/> 

Please get in touch with feedback, bug reporting and project development via: 
>Alex.Wallwork@AlexBrew.com

##Manual 
 


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
    The round can be saved into a database or as a CSV of format: <br/>
    
        "Brewer Name" "Round Date" "Round Unique ID" <br/>
        "Drinker1" "Drinker1_Drink" <br/>
        "Drinker2" "Drinker2_Drink"           

[8] Returns all stored drinks or allows you to search. 

[Ex] Returns all stored people or allows you to search for them by firstname, lastname or age. 


