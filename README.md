# Facebook_operations


NOTE: SELENIUM HAS BEEN USED FOR MAKING THE BOT
===============================================================================================================================================================================

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
KEY FEATURES AND POINT:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
THE GIVEN PROJECT TAKES THE FACEBOOK USERNAME AND PASSWORD AND DOES THE FOLLOWING OPERAIONS:

1. LOGIN
2. UPDATE THE USER'S STATUS
3. ADD A FREIND WHO LIVES IN THE SAME LOCATION (CITY) AS USER
4. COMEENTS ON THE LATEST FIRST POST OF A RANDOM FRIEND (THE COMMENT IS PASSED THROUGH A FUNCITON CALL IN THE CODE)

-> THE PROJECT IS FULLY DYNAMIC. IT DOES NOT INVOLVE AANY HARDCODED URL LINKS EXCEPT FOR FACEBOOK'S HOME PAGE. 

-> THE HTML ELEMENTS LIKE TEXT AREA, BUTTONS, ETC ARRE ASSUMED TO BEGENERIC FOR DIFFERENT USERS, MEANING THAT THE HTML ELEMENT PATH FOR A PARTICULAR TEXT AREA LIKE "WHAT'S ON YOUR MIND" IS THE SAME FOR DIFFERENT USERS AS OULINE OF THE HTML PAFE REMINS CONSTANT THUS THEIR HARDCODED ELEMENT REFERENCES DOES NOT EFFEECT THE DYNAMIC NATURE OF THE APPLICATION.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ASSUMPTIONS MADE:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

a) WHEN THE FACEBOOK PAGE OF THE USER'S CURRENT CITY IS OPENED FOR SENDING FRIEND REQUEST TO A PERSON IN THE SAME LOCATION, IT IS ASSUMED THAT THE FIRST POST ON THE PAGE IS FROM A PERSON AND NOT ANY PUBLIC ORGANISATION. ONLY THEN COULD THE "ADD FRIEND" BUTTON BE ACCESS BY THE CODE. 

b) WITH REFERENCE TO THE PREVIOUS POINT, IT IS ALSO ASSUMED THAT THE PEROSN WITH THE LATEST POST ON THE CITY PAGE IS RELATED TO THE  CITY ITSELF AS THERE IS LESS CHACE THAT HE/SHE WOULD POST ABOUUT THE CITY WHEN HE IS NOT FORM THERE.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PROCEDURES CARRIED OUT FOR VARIOUS TASKS:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1> FOR ADDING FRIEND FROM THE CURRENT CITY, THE BOT FIRST GOES TO "ABOUT" SECTION OF THE CURRENT USER, BROWSES THROUGH THE CITIES HE HAS LIVED AND AS THE CURRENT CITY IS USUALLY LISTED AT TOP. IT CLICK THE CITY URL AND IS DIRECTED TO THE FACEBOOK PAGE OF THE CITY. THEN ACCORDING TO ASSUMPTIONS (a) AND (b), IT ADDS THE VERY FIRST PERSON ON THE PAGE AS THE FRIEND

2> FOR POTING ON THE TIMELINE OF A RANDOM FRIEND, THE BOT GOES TO THE "FRIENDS" SECTION OF THE USER AND PICKS THE FIRST FRIEND AND POSTS ON THEIR TIMELINE. IT IS TO BE NOTED THAT THE WAY FRIENDS ARE SHOWN ON FACEBOOK "FRIENDS" SECTION VARIES WITH TIME. THUS THE RANDOMNESS IS MAINTAINED. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
USER GUIDE:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1> THE USER WOULD NEED TO CLONE THE REPOSITORY AND ENTER HIS CREDENTIALS IN THE FILES "TEST" FOLDER (EX : LINES 24 AND 25 IN "login_test.py") 

2> Install the dependencies as mentioned in requirements.txt

3> Download the chrome driver from https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/, unxzip the file and paste the execution file the "Python Folder"
 (ex : C:\Users\user\AppData\Local\Programs\Python\Python39)
 
3> RUN THE TEST FILE FROM THE IDE INTERFACE ITSELF AND NOT THE TERMINAL

4> ENJOY!
